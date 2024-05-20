#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Any, Tuple, Union, Dict

from copy_outfits.enums.copy_outfit_age import CopyOutfitsAge
from copy_outfits.enums.pie_menu_action_ids import PieMenuActionIds
from copy_outfits.utils.outfit_modifiers import OutfitModifiers
from copy_outfits.persist.outfit_store import OutfitStore
from copy_outfits.persist.sim_store import SimStore
from copy_outfits.struct.action import O19COAction
from copy_outfits.struct.internal_stbl import InternalSTBL
from copy_outfits.modinfo import ModInfo
from copy_outfits.enums.outfit_groups import OutfitGroups

from ts4lib.utils.outfit_utilities import OutfitUtilities
from ui.ui_dialog_notification import UiDialogNotification

from event_testing.results import TestResult
from interactions.context import InteractionContext
from routing.walkstyle.walkstyle_request import WalkStyleRequest
from sims.outfits.outfit_enums import OutfitCategory
from sims.sim import Sim
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims.sim_info import SimInfo
from sims4.tuning.tunable import Tunable

from sims4communitylib.enums.common_occult_type import CommonOccultType
from sims4communitylib.enums.traits_enum import CommonTraitId
from sims4communitylib.utils.sims.common_sim_gender_option_utils import CommonSimGenderOptionUtils
from sims4communitylib.utils.sims.common_sim_occult_type_utils import CommonSimOccultTypeUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils
from sims4communitylib.utils.sims.common_trait_utils import CommonTraitUtils
from sims4communitylib.classes.interactions.common_terrain_interaction import CommonTerrainInteraction
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_choose_outfit_dialog import CommonChooseOutfitDialog
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.services.sim.cas.common_sim_outfit_io import CommonSimOutfitIO
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'interactions')
log.enable()


class OutfitTools(CommonTerrainInteraction):
    INSTANCE_TUNABLES = {
        'outfit_category': Tunable(tunable_type=int, default=-1),
        'outfit_index': Tunable(tunable_type=int, default=-1),
        'clipboard_index': Tunable(tunable_type=int, default=0),
        'action': Tunable(tunable_type=int, default=0),
        'action_id': Tunable(tunable_type=int, default=0),
    }
    __slots__ = {'outfit_category', 'outfit_index', 'clipboard_index', 'action', 'action_id', }

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> TestResult:
        return TestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        if not isinstance(interaction_target, Sim):
            return False
        sim_info = CommonSimUtils.get_sim_info(interaction_target)

        action = int(self.action)
        action_id = int(self.action_id)
        outfit_category = int(self.outfit_category)
        outfit_index = int(self.outfit_index)
        clipboard_index = int(self.clipboard_index)

        update_outfit = False
        really_update_outfit = False
        _outfit_category = CommonOutfitUtils.get_current_outfit_category(sim_info)
        if outfit_category == -1 or outfit_category == _outfit_category:
            outfit_category = _outfit_category
            update_outfit = True

        _outfit_index = CommonOutfitUtils.get_current_outfit_index(sim_info)
        if outfit_index == -1 or outfit_index == _outfit_index:
            outfit_index = _outfit_index
        else:
            update_outfit = False
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)

        log.debug(f"on_started({interaction_sim}, {interaction_target}) a={action}.{action_id} o={outfit_name}[{outfit_index}] upd={update_outfit}")
        # action: 1 Copy || 2 Paste || 4 PieMenuActionIds || 8 Clear || 16 Print
        # action_id: 0..100
        # outfit_index: 0..5 | -1 Default
        # outfit_category: 0..25 | -1 Default
        # clipboard_index: 0..4

        if action == O19COAction.PRINT:
            self.print_outfit_details()
        elif action == O19COAction.CLEAR:
            self.remove_all_outfits()
        elif action == O19COAction.CLONE:
            self.clone_sim(sim_info, action, action_id, outfit_category, outfit_index, clipboard_index)
            OutfitModifiers().remove_all_outfit_appearance_modifiers(sim_info)
        elif action == O19COAction.PASTE:
            self.paste_outfit(sim_info, action, action_id, outfit_category, outfit_index, clipboard_index)
            OutfitModifiers().remove_all_outfit_appearance_modifiers(sim_info)
        elif action == O19COAction.COPY:
            self.copy_outfit(sim_info, action, action_id, outfit_category, outfit_index, clipboard_index)

        return True

    def open_outfit_picker(self, sim_info: SimInfo, action: int, outfit_list: Union[None, Tuple[OutfitCategory, int]] = None, exclude_outfit_categories: Union[None, Tuple[OutfitCategory]] = None):
        log.debug(f"show_outfit_picker({action}, {outfit_list}, {exclude_outfit_categories})")

        def _on_chosen(choice: Tuple[OutfitCategory, int], outcome: CommonChoiceOutcome):
            if outcome == CommonChoiceOutcome.CHOICE_MADE:
                self.process_pick(sim_info, action, choice)

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.TS4_SIM_NAME, tokens=(sim_info,), ),)
            if action == O19COAction.COPY:
                # InternalSTBL.O19_SOURCE = 'Source'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_SOURCE, text_color=CommonLocalizedStringColor.GREEN),)
            else:
                # InternalSTBL.O19_TARGET = 'Target'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_TARGET, text_color=CommonLocalizedStringColor.RED),)
            dialog = CommonChooseOutfitDialog(
                ModInfo.get_identity(),
                InternalSTBL.TS4_STRING,  # '{0.String}'
                InternalSTBL.O19_SELECT___OUTFIT,  # 'Select {0.String} OutfitTools
                title_tokens=title_tokens,  # '{SimName}'
                description_tokens=description_tokens  # 'Source' or 'Target'
            )

            if outfit_list and exclude_outfit_categories:
                try:
                    dialog.show(sim_info, outfit_list=outfit_list, exclude_outfit_categories=exclude_outfit_categories, on_chosen=_on_chosen)
                except Exception as e:
                    log.warn(f"It seems that no special outfit is available. ({e})")
            else:
                dialog.show(sim_info, on_chosen=_on_chosen)
        except Exception as e:
            log.warn(f"It seems that no outfits are available. ({e})")
        log.debug(f"Dialog closed.")

    def process_pick(self, sim_info: SimInfo, action: int, choice: Tuple[OutfitCategory, int]):
        co_age = CopyOutfitsAge.get_co_age(sim_info)
        clipboard_index = 0
        outfit_category, outfit_index = choice
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)
        valid_parts_ids = OutfitGroups.parts[PieMenuActionIds.CLOTH]

        if action == O19COAction.PASTE:
            log.debug(f"Paste to outfit '{outfit_name}[{outfit_index}]' for '{sim_info}' (from clipboard '{clipboard_index}')")
            new_parts = self.get_parts(co_age, clipboard_index)
            if new_parts:
                merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids, (outfit_category, outfit_index))
                log.debug(f"Updating outfit '{outfit_name}[{outfit_index}]'")
                OutfitUtilities().apply_outfit(sim_info, merged_parts, (outfit_category, outfit_index))
                OutfitModifiers().remove_all_outfit_appearance_modifiers(sim_info)

        elif action == O19COAction.COPY:
            log.debug(f"Copying '{sim_info}'s outfit {outfit_name}[{outfit_index}] to clipboard '{clipboard_index}'")
            parts = CommonOutfitUtils.get_outfit_parts(sim_info, choice)
            if parts:
                self.save_outfit(sim_info, parts, clipboard_index, outfit_category, outfit_index)
                self.show_notification(f"Copied outfit '{outfit_name}[{outfit_index}]' to clipboard {clipboard_index}.")
        else:
            log.error(f"process_pick('{sim_info}', '{action}', '{choice})' -> (unknown action)", throw=False)

    @staticmethod
    def get_parts(co_age: int, clipboard_index: int = 0) -> dict:
        parts = dict()
        outfit_for_age = OutfitStore.outfits.get(co_age, dict())
        if outfit_for_age:
            parts = outfit_for_age.get(clipboard_index, None)
            if parts:
                source = OutfitStore.outfits.get(co_age).get(clipboard_index)
                debug_message = f' (from clipboard {clipboard_index} - {source})'
                pass
            else:
                debug_message = f' (clipboard {clipboard_index} empty)'
        else:
            debug_message = ' (no outfits for this age)'
        log.debug(f"get_parts({co_age}, {clipboard_index}) -> '{parts}'{debug_message}")
        return parts

    @staticmethod
    def merge_parts(src_sim_info, new_parts, valid_parts_ids, src_outfit_category_and_index: Union[Tuple, None] = None) -> dict:
        """
        :param src_sim_info: The sim whose outfit is to be modified
        :param new_parts: A dict with parts to apply {BodyPart: CasPartId, ...}
        :param valid_parts_ids: A list with BodyParts to apply. If they are in 'new_parts' they will be replaced in, otherwise they are removed.
            # A filter for the part ids to apply. All part ids will be removed from the current outfit. Part ids in this list will be copied from {new_parts}.
        :param src_outfit_category_and_index optional to specify an outfit for the source sim
        :return:
        """

        if src_outfit_category_and_index:
            outfit_category_and_index = src_outfit_category_and_index
        else:
            outfit_category_and_index: Tuple = CommonOutfitUtils.get_current_outfit(src_sim_info)
        current_parts: Dict = CommonOutfitUtils.get_outfit_parts(src_sim_info, outfit_category_and_index).copy()
        log.debug(f"merge_parts() current_parts = {current_parts}")
        log.debug(f"merge_parts() valid_parts_ids = {valid_parts_ids}: {type(valid_parts_ids)}")
        log.debug(f"merge_parts() new_parts = {new_parts}")

        for valid_part_id in valid_parts_ids:
            new_part = new_parts.get(valid_part_id, None)
            current_parts.update({valid_part_id: new_part})
            if new_part is None:
                del current_parts[valid_part_id]  # valid_part_id exists with None

        log.debug(f"merge_parts() -> {current_parts}")
        return current_parts

    @staticmethod
    def show_notification(message, urgency=UiDialogNotification.UiDialogNotificationUrgency.DEFAULT):
        """
        :param message: The text to print
        :param urgency: UiDialogNotification.UiDialogNotificationUrgency.URGENT = orange box
        :return:
        """
        mod_identifier = ModInfo.get_identity().name
        basic_notification = CommonBasicNotification(
            InternalSTBL.TS4_STRING,  # '{0.String}'
            InternalSTBL.TS4_STRING,  # '{0.String}'
            title_tokens=(mod_identifier,),  # 'Copy Outfits'
            description_tokens=(message.replace('{', '[').replace('}', ']'),),  # 0.String has no variables. Parsing `{'Dict': 123}` fails!
            urgency=urgency
        )
        basic_notification.show()

    def print_outfit_details(self):
        log.debug(f"Sources: {OutfitStore.sources}")
        log.debug(f"Outfits: {OutfitStore.outfits}")

        for co_age, clipboard_data in OutfitStore.outfits.items():
            if clipboard_data:
                msg = f"{CopyOutfitsAge(co_age).name}:"
                for clipboard_index, parts in clipboard_data.items():
                    source = OutfitStore.sources.get(co_age).get(clipboard_index)
                    msg = f"{msg} (#{clipboard_index}: {source})"
                log.debug(f"UI Notification: '{msg}'")
                self.show_notification(msg)

    def remove_all_outfits(self):
        OutfitStore.outfits = dict()
        OutfitStore.sources = dict()

    def clone_sim(self, sim_info: SimInfo, action: int, action_id: int, outfit_category: int, outfit_index: int, clipboard_index: int):
        co_age = CopyOutfitsAge.get_co_age(sim_info)
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)
        new_parts = self.get_parts(co_age, clipboard_index)
        if not new_parts:
            self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")
            return False
        src_sim_info = CommonSimUtils.get_sim_info(SimStore.sims.get(co_age, None))
        if not src_sim_info:
            self.show_notification(f"No sim_info found in cache.")
            return False
        if PieMenuActionIds.ALL_OUTFITS_FOR_CATEGORY < action_id < PieMenuActionIds.ALL:
            valid_parts_ids = OutfitGroups.parts[action_id]
            merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
            sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
            sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))
        else:
            if action_id == PieMenuActionIds.ALL_OUTFITS_FOR_CATEGORY or action_id == PieMenuActionIds.ALL:
                sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=new_parts, mod_identity=ModInfo.get_identity())
                sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))

            if action_id == PieMenuActionIds.AGE_GENDER or action_id == PieMenuActionIds.ALL:
                SimInfoBaseWrapper.copy_base_attributes(sim_info, src_sim_info)  # Order: dest, src

                # CommonSimGenderOptionUtils.update_body_frame() !CommonSimGenderOptionUtils.get_body_frame()
                if CommonTraitUtils.has_trait(src_sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_MASCULINE).result:
                    CommonTraitUtils.add_trait(sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_MASCULINE)
                else:
                    CommonTraitUtils.remove_trait(sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_MASCULINE)
                if CommonTraitUtils.has_trait(src_sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_FEMININE).result:
                    CommonTraitUtils.add_trait(sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_FEMININE)
                else:
                    CommonTraitUtils.remove_trait(sim_info, CommonTraitId.GENDER_OPTIONS_FRAME_FEMININE)

                # CommonSimGenderOptionUtils.update_clothing_preference() !CommonSimGenderOptionUtils.get_clothing_preference()
                if CommonTraitUtils.has_trait(src_sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_MENS_WEAR).result:
                    CommonTraitUtils.add_trait(sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_MENS_WEAR)
                else:
                    CommonTraitUtils.remove_trait(sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_MENS_WEAR)
                if CommonTraitUtils.has_trait(src_sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_WOMENS_WEAR).result:
                    CommonTraitUtils.add_trait(sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_WOMENS_WEAR)
                else:
                    CommonTraitUtils.remove_trait(sim_info, CommonTraitId.GENDER_OPTIONS_CLOTHING_WOMENS_WEAR)

                # O19CommonSimPregnancyUtils.can_be_impregnated(sim_info, O19CommonSimPregnancyUtils.can_be_impregnated(src_sim_info).result)
                # O19CommonSimPregnancyUtils.can_impregnate(sim_info, O19CommonSimPregnancyUtils.can_impregnate(src_sim_info).result)
                CommonSimGenderOptionUtils.update_can_be_impregnated(sim_info, CommonSimGenderOptionUtils.can_be_impregnated(src_sim_info).result)
                CommonSimGenderOptionUtils.update_can_impregnate(sim_info, CommonSimGenderOptionUtils.can_impregnate(src_sim_info).result)
                CommonSimGenderOptionUtils.update_can_reproduce(sim_info, CommonSimGenderOptionUtils.can_reproduce(src_sim_info).result)

                CommonSimGenderOptionUtils.update_has_breasts(sim_info, CommonSimGenderOptionUtils.has_breasts(src_sim_info).result)

                # !can_use_toilet_standing() set_can_use_toilet_standing()
                toilet_standing_trait: CommonTraitId = CommonSimGenderOptionUtils.determine_toilet_standing_trait(src_sim_info)
                if toilet_standing_trait:
                    CommonTraitUtils.add_trait(sim_info, toilet_standing_trait)
                else:
                    CommonTraitUtils.remove_trait(sim_info, toilet_standing_trait)

                # !can_use_toilet_standing() set_can_use_toilet_standing()
                uses_toilet_sitting: CommonTraitId = CommonSimGenderOptionUtils.determine_toilet_sitting_trait(src_sim_info)
                if uses_toilet_sitting:
                    CommonTraitUtils.add_trait(sim_info, uses_toilet_sitting)
                else:
                    CommonTraitUtils.remove_trait(sim_info, uses_toilet_sitting)

            if action_id == PieMenuActionIds.PHYSICS_GENETICS or action_id == PieMenuActionIds.ALL:
                SimInfoBaseWrapper.copy_physical_attributes(sim_info, src_sim_info)
                SimInfoBaseWrapper.resend_physical_attributes(sim_info)

            if action_id == PieMenuActionIds.GENETICS:
                SimInfoBaseWrapper.copy_genetic_data(sim_info, src_sim_info)

            if action_id == PieMenuActionIds.SLIDERS:
                pass

            if action_id == PieMenuActionIds.TRAITS or action_id == PieMenuActionIds.ALL:
                # CommonTraitUtils.remove_trait(sim_info, *CommonTraitUtils.get_equipped_traits(sim_info))
                # CommonTraitUtils.add_traits(sim_info, CommonTraitUtils.get_equipped_traits(src_sim_info))
                del_traits: list = CommonTraitUtils.get_equipped_traits(sim_info)
                add_traits: list = CommonTraitUtils.get_equipped_traits(src_sim_info)
                for trait in del_traits:
                    if trait in add_traits:
                        continue  # trait in both lists, don't delete this trait
                    CommonTraitUtils.remove_trait(sim_info, trait)

                for trait in add_traits:
                    if trait in del_traits:
                        continue  # trait in both lists, don't add this trait
                    try:
                        CommonTraitUtils.add_trait(sim_info, trait)
                    except Exception as e:
                        log.warn(f"Could not add trait '{trait}'")

            if action_id == PieMenuActionIds.WALKSTYLE or action_id == PieMenuActionIds.ALL:
                src_sim: Sim = CommonSimUtils.get_sim_instance(src_sim_info)
                sim: Sim = CommonSimUtils.get_sim_instance(sim_info)
                # sim.routing_component._walkstyle_requests = src_sim.routing_component._walkstyle_requests  # CAS to Game will fail, likely wrong 'sim'
                walkstyle_requests: list = src_sim.routing_component.get_walkstyle_requests()
                for walkstyle_request in walkstyle_requests:
                    WalkStyleRequest(sim, walkstyle=walkstyle_request.walkstyle, priority=walkstyle_request.priority)

            # Relationship
            # TODO

    def paste_outfit(self, sim_info: SimInfo, action: int, action_id: int, outfit_category: int, outfit_index: int, clipboard_index: int):
        co_age = CopyOutfitsAge.get_co_age(sim_info)
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)
        valid_parts_ids = OutfitGroups.parts[PieMenuActionIds.CLOTH]
        if action_id == PieMenuActionIds.PICKER:
            self.open_outfit_picker(sim_info, action, None, None)
        elif action_id == PieMenuActionIds.XPICKER:
            occult_type: CommonOccultType = CommonSimOccultTypeUtils.determine_current_occult_type(sim_info)
            if CommonSpeciesUtils.is_pet(sim_info):
                log.warn(f"Pets have no special outfits.")
                self.show_notification(f"Pets have has no special outfits.")
                return True
            if CommonOccultType.MERMAID == occult_type or CommonOccultType.ALIEN == occult_type:
                log.warn(f"Occult '{occult_type}' has no special outfits.")
                self.show_notification(f"Occult '{occult_type}' has no special outfits.")
                return True
            self.open_outfit_picker(
                sim_info,
                action,
                (
                    (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.SPECIAL, 0), (OutfitCategory.SPECIAL, 1), (OutfitCategory.CAREER, 0),
                    (OutfitCategory.BATUU, 0), (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                ),
                (OutfitCategory.CURRENT_OUTFIT, )
            )  # SPECIAL[1] == Towel
        elif action_id == PieMenuActionIds.ALL_OUTFITS_FOR_CATEGORY:
            i = 0
            log.debug(f"Pasting all outfits to '{outfit_name}'")
            for outfit_index in range(0, 5):
                new_parts = self.get_parts(co_age, outfit_index)
                if new_parts:
                    merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
                    OutfitUtilities().apply_outfit(sim_info, merged_parts, (outfit_category, outfit_index))
                    i += 1

                    # Copy 1 outfit
                    if outfit_category == OutfitCategory.BATHING or outfit_category == OutfitCategory.SITUATION or outfit_category == OutfitCategory.CAREER:
                        break
                    # Copy 2 outfits (SPECIAL.1 == Towel)
                    if outfit_category == OutfitCategory.SPECIAL and outfit_index == 1:
                        break

            self.show_notification(f"Pasted {i} outfit(s) to '{outfit_name}'.")
        elif 100 <= clipboard_index <= 104:
            clipboard_index -= 100
            log.debug(f"Pasting from clipboard '{clipboard_index}' to current outfit '{outfit_category}[{outfit_index}]'")
            new_parts = self.get_parts(co_age, clipboard_index)
            if new_parts:
                merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
                OutfitUtilities().apply_outfit(sim_info, merged_parts, (outfit_category, outfit_index))
                log.debug(f"Pasted.")
                self.show_notification(f"Pasted from clipboard '{clipboard_index}' to outfit '{outfit_category}[{outfit_index}]'")
            else:
                self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")
        else:
            log.debug(f"Paste to outfit '{outfit_name}[{outfit_index}]' (from clipboard '{clipboard_index}')")
            if ((outfit_category == OutfitCategory.BATHING or outfit_category == OutfitCategory.SITUATION or outfit_category == OutfitCategory.CAREER) and outfit_index > 0) \
                    or (outfit_category == OutfitCategory.SPECIAL and outfit_index > 1):
                self.show_notification(f"Can't paste to '{outfit_category}[{outfit_index}]'.")
                return False
            new_parts = self.get_parts(co_age, clipboard_index)
            if new_parts:
                merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids, (outfit_category, outfit_index))
                OutfitUtilities().apply_outfit(sim_info, merged_parts, (outfit_category, outfit_index))
                self.show_notification(f"Pasted from clipboard '{clipboard_index}' to outfit '{outfit_name}[{outfit_index}]'.")
            else:
                self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")

    def copy_outfit(self, sim_info: SimInfo, action: int, action_id: int, outfit_category: int, outfit_index: int, clipboard_index: int):
        co_age = CopyOutfitsAge.get_co_age(sim_info)
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)
        SimStore.sims.update({co_age: sim_info.sim_id})
        if action_id == PieMenuActionIds.PICKER:
            self.open_outfit_picker(sim_info, action, None, None)
        elif action_id == PieMenuActionIds.XPICKER:
            occult_type: CommonOccultType = CommonSimOccultTypeUtils.determine_current_occult_type(sim_info)
            if CommonSpeciesUtils.is_pet(sim_info):
                log.warn(f"Pets have no special outfits.")
                self.show_notification(f"Pets have has no special outfits.")
                return True
            if CommonOccultType.MERMAID == occult_type or CommonOccultType.ALIEN == occult_type:
                log.warn(f"Occult '{occult_type}' has no special outfits.")
                self.show_notification(f"Occult '{occult_type}' has no special outfits.")
                return True
            self.open_outfit_picker(
                sim_info,
                action,
                (
                    (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.SPECIAL, 0), (OutfitCategory.SPECIAL, 1), (OutfitCategory.CAREER, 0),
                    (OutfitCategory.BATUU, 0), (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                ),
                (OutfitCategory.CURRENT_OUTFIT, )
            )  # SPECIAL[1] == Towel
        elif action_id == PieMenuActionIds.ALL_OUTFITS_FOR_CATEGORY:
            i = -1
            log.debug(f"Copying all outfits for '{outfit_name}'")
            for outfit_index in range(0, 5):
                parts = CommonOutfitUtils.get_outfit_parts(sim_info, (outfit_category, outfit_index))
                if parts:
                    self.save_outfit(sim_info, parts, outfit_index, outfit_category, outfit_index)
                    i += 1
                else:
                    break
            self.show_notification(f"Copied {i} '{outfit_name}' outfit(s) to clipboards 0-{i}.")
        else:
            log.debug(f"Copying outfit {outfit_name}[{outfit_index}] to clipboard '{clipboard_index}'")
            parts = CommonOutfitUtils.get_outfit_parts(sim_info, (outfit_category, outfit_index))
            if parts:
                self.save_outfit(sim_info, parts, clipboard_index, outfit_category, outfit_index)
                self.show_notification(f'Copied outfit {outfit_name}[{outfit_index}] to clipboard {clipboard_index}.')

    def save_outfit(self, sim_info: SimInfo, parts, clipboard_index: int, outfit_category: int, outfit_index: int):
        co_age = CopyOutfitsAge.get_co_age(sim_info)
        outfit_name = OutfitGroups.outfit_categories.get(outfit_category)

        clipboard_data: Dict = OutfitStore.outfits.get(co_age, {})
        clipboard_data.update({clipboard_index: parts})
        OutfitStore.outfits.update({co_age: clipboard_data})

        clipboard_data: Dict = OutfitStore.sources.get(co_age, {})
        clipboard_data.update({clipboard_index: f"{sim_info} {outfit_name}[{outfit_index}]"})
        OutfitStore.sources.update({co_age: clipboard_data})

