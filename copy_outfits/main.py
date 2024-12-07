#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Any, Tuple, Union

from copy_outfits.copy_outfits_mannequin import CopyOutfitsMannequin
from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.enums.outfit_group_id import OutfitGroupId
from copy_outfits.enums.outfit_groups import OutfitGroups
from copy_outfits.enums.pie_menu_action import PieMenuAction
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.modinfo import ModInfo
from copy_outfits.outfit_add import OutfitAdd
from copy_outfits.outfit_copy import OutfitCopy
from copy_outfits.outfit_paste import OutfitPaste
from copy_outfits.outfit_print import OutfitPrint
from copy_outfits.outfit_skin import OutfitSkin
from copy_outfits.persist.outfit_store import OutfitStore
from copy_outfits.persist.sim_store import SimStore
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from copy_outfits.struct.internal_stbl import InternalSTBL
from copy_outfits.utils.copy_outfit_utilities import CopyOutfitUtilities
from copy_outfits.utils.outfit_modifiers import OutfitModifiers
from copy_outfits.utils.outit_notifications import OutfitNotifications
from objects.components.mannequin_component import MannequinComponent
from routing.walkstyle.walkstyle_request import WalkStyleRequest
from sims.outfits.outfit_enums import OutfitCategory, SpecialOutfitIndex
from sims.sim import Sim
from sims.sim_info import SimInfo
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_choose_outfit_dialog import CommonChooseOutfitDialog
from sims4communitylib.enums.common_occult_type import CommonOccultType
from sims4communitylib.enums.traits_enum import CommonTraitId
from sims4communitylib.services.sim.cas.common_sim_outfit_io import CommonSimOutfitIO
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.sims.common_sim_gender_option_utils import CommonSimGenderOptionUtils
from sims4communitylib.utils.sims.common_sim_occult_type_utils import CommonSimOccultTypeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils
from sims4communitylib.utils.sims.common_trait_utils import CommonTraitUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'Main')
log.enable()


class Main:
    def __init__(self):
        self.interaction_target = None

        # Instance tunables
        self.action: PieMenuAction = PieMenuAction.NONE
        self.clipboard_index = 0
        self.outfit_category = -1
        self.outfit_name = OutfitCategory(self.outfit_category)
        self.outfit_index = -1

        self._sim: Union[CopyOutfitsSim, None] = None
        self.sim_info: Union[SimInfo, None] = None
        self.mannequin_component: Union[MannequinComponent, None] = None  # Set only for mannequins
        self.sim_age = CopyOutfitsAge.UNKNOWN
        self.is_female = None
        self.sim_id = -1

        self.SIM_ID_MANNEQUIN = -1
        self.SIM_ID_MANNEQUIN_ADULT = -2
        self.SIM_ID_MANNEQUIN_CHILD = -3

    def on_started(self, interaction_sim: Sim, interaction_target: Any, instance_tunables: Tuple[int, int, int, int, int, int], ) -> bool:
        log.debug(f"on_started({interaction_sim}, {interaction_target}, it={instance_tunables})")
        try:
            self.interaction_target = interaction_target
            try:
                self._sim: CopyOutfitsSim = CopyOutfitsSim(interaction_target, instance_tunables)
            except Exception as e:
                log.debug(f"Error '{e}' getting sim data.")
                return True

            _action: PieMenuAction = self._sim.action
            _, _, _, self.clipboard_index, self.outfit_category, self.outfit_index = instance_tunables

            if _action in [PieMenuAction.CLONE_CAS_PARTS, PieMenuAction.CLONE_SIM_DATA, ]:
                action_name = self._sim.group_id.name
            else:
                action_name = self._sim.action_id.name
            log.debug(f"starting({interaction_sim}, {self.interaction_target}) a={_action.name}.{action_name} o={self._sim.outfit_name}.{self._sim.outfit_index} c={self._sim.clipboard_index}")

            if _action == PieMenuAction.COPY:
                self.copy_outfit(self._sim)
            elif _action == PieMenuAction.PASTE:
                self.paste_outfit(self._sim)
                OutfitModifiers().remove_all_outfit_appearance_modifiers(self.sim_info)
            elif _action == PieMenuAction.CLONE_SIM_DATA:
                self.clone_sim_data(self._sim)
                OutfitModifiers().remove_all_outfit_appearance_modifiers(self.sim_info)
            elif _action == PieMenuAction.CLONE_CAS_PARTS:
                self.clone_cas_parts(self._sim)
                OutfitModifiers().remove_all_outfit_appearance_modifiers(self.sim_info)
            elif _action == PieMenuAction.CLEAR:
                self.remove_all_outfits()
            elif _action == PieMenuAction.PRINT:
                OutfitPrint().print_outfit_details()
            elif _action == PieMenuAction.SKIN:
                OutfitSkin().apply_skin(self._sim)
            elif _action == PieMenuAction.MANNEQUIN:
                CopyOutfitsMannequin().change_mannequin(self._sim, interaction_sim, interaction_target)
            elif _action == PieMenuAction.ADD:
                OutfitAdd().add_outfits(self._sim)
            elif _action == PieMenuAction.BODY_TYPE:
                log.debug(f"TODO - BODY_TYPE Picker")
            elif _action == PieMenuAction.FIX_HEAD:
                OutfitSkin().fix_head(self.interaction_target)
            else:
                log.warn(f"Unknown action '{_action}'. This should never happen.")
        except Exception as e:
            log.error(f"Error '{e}'")
        return True

    def open_outfit_picker(self, zim: CopyOutfitsSim, action: int, outfit_list: Union[None, Tuple[OutfitCategory, int]] = None, exclude_outfit_categories: Union[None, Tuple[OutfitCategory]] = None):
        log.debug(f"show_outfit_picker({action}, {outfit_list}, {exclude_outfit_categories})")

        def _on_chosen(choice: Tuple[OutfitCategory, int], outcome: CommonChoiceOutcome):
            if outcome == CommonChoiceOutcome.CHOICE_MADE:
                self.process_pick(zim, action, choice)

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.TS4_SIM_NAME, tokens=(zim.sim_info,), ),)
            if action == PieMenuAction.COPY:
                # InternalSTBL.O19_SOURCE = 'Source'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_SOURCE, text_color=CommonLocalizedStringColor.GREEN),)
            else:
                # InternalSTBL.O19_TARGET = 'Target'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_TARGET, text_color=CommonLocalizedStringColor.RED),)
            dialog = CommonChooseOutfitDialog(
                ModInfo.get_identity(),
                InternalSTBL.TS4_STRING,  # '{0.String}'
                InternalSTBL.O19_SELECT___OUTFIT,  # 'Select {0.String} OutfitTools'
                title_tokens=title_tokens,  # '{SimName}'
                description_tokens=description_tokens  # 'Source' or 'Target'
            )

            if outfit_list and exclude_outfit_categories:
                try:
                    dialog.show(zim.sim_info, outfit_list=outfit_list, exclude_outfit_categories=exclude_outfit_categories, on_chosen=_on_chosen)
                except Exception as e:
                    log.warn(f"It seems that no special outfit is available. ({e})")
            else:
                dialog.show(zim.sim_info, on_chosen=_on_chosen)
        except Exception as e:
            log.warn(f"It seems that no outfits are available. ({e})")
        log.debug(f"Dialog closed.")

    def process_pick(self, zim: CopyOutfitsSim, action: int, choice: Tuple[OutfitCategory, int]):
        clipboard_index = 0
        outfit_category, outfit_index = choice
        # outfit_name = OutfitGroups.outfit_categories.get(outfit_category)
        # valid_parts_ids = OutfitGroups.parts[PieMenuActionId.CLOTH]

        if action == PieMenuAction.COPY:
            if OutfitCopy().copy(zim, clipboard_index, outfit_category, outfit_index):
                OutfitNotifications().show_notification(f'Copied outfit.')
            else:
                log.warn(f"Outfit 'Copy' failed.")

        elif action == PieMenuAction.PASTE:
            valid_parts_ids = OutfitGroups.SIM_GARMENT.value  # Paste all outfit parts, nothing else.
            if OutfitPaste().paste(zim, valid_parts_ids, clipboard_index, outfit_category, outfit_index):
                pass
            else:
                log.warn(f"Outfit 'Paste' failed.")

        else:
            log.error(f"process_pick(sim_info='{zim.sim_info}', action={action}, choice='{choice})' -> (unknown action)", throw=False)

    def remove_all_outfits(self):
        """ Remove all source sims and outfits from store """
        OutfitStore.outfits = dict()
        OutfitStore.sources = dict()

    def clone_cas_parts(self, zim: CopyOutfitsSim):
        sim_age = zim.sim_age
        sim_info: SimInfo = zim.sim_info
        group_id: OutfitGroupId = zim.group_id
        outfit_category = zim.outfit_category
        outfit_index = zim.outfit_index
        clipboard_index = 0

        new_parts = CopyOutfitUtilities().get_parts_from_clipboard(sim_age, clipboard_index)
        if not new_parts:
            OutfitNotifications().show_notification(f"No outfit found in clipboard [{clipboard_index}].")
            return False

        if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.SIM_ALL, ]:
            if group_id == OutfitGroupId.EVERYTHING:
                self.clone_sim_data(zim)  # Clone also the sim data, genetics, traits, ...
            merged_parts = new_parts  # Replace everything
        else:
            current_parts = CopyOutfitUtilities().get_body_parts(zim, outfit_category, outfit_index)
            valid_parts_ids = OutfitGroups[group_id.name].value
            merged_parts = CopyOutfitUtilities().merge_parts(current_parts, new_parts, valid_parts_ids)

        # Apply the outfit
        sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
        sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))

        self.apply_cas_parts(zim)
        log.debug(f"CAS Parts clone completed.")

    def apply_cas_parts(self, zim: CopyOutfitsSim):
        sim_info: SimInfo = zim.sim_info
        outfit_category = zim.outfit_category
        outfit_index = zim.outfit_index
        mannequin_component = zim.mannequin_component

        if mannequin_component:
            mannequin_component.set_current_outfit = (outfit_category, outfit_index)
            mannequin_component._on_outfit_change(sim_info, (outfit_category, outfit_index))
        else:
            sim_info._current_outfit = (outfit_category, outfit_index)
        log.debug(f"CAS Parts clone completed.")

    def clone_sim_data(self, zim: CopyOutfitsSim):
        sim_age = zim.sim_age
        sim_info = zim.sim_info
        group_id: OutfitGroupId = zim.group_id
        mannequin_component = zim.mannequin_component

        _sim_id = SimStore.sims.get(sim_age, None)
        if _sim_id < self.SIM_ID_MANNEQUIN:
            src_sim_info = None
        else:
            src_sim_info = CommonSimUtils.get_sim_info(_sim_id)
            if src_sim_info is None:
                OutfitNotifications().show_notification(f"No sim_info found in cache.")
                return False

        if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_SKIN_TONE, ]:
            sim_info.skin_tone = src_sim_info.skin_tone
            sim_info.skin_tone_val_shift = src_sim_info.skin_tone_val_shift
            sim_info.resend_skin_tone()
            log.debug(f"X_SKIN_TONE")

        if src_sim_info is None:
            log.debug(f"Source mannequin can't distribute age/gender/extended_species, slider and/or physics/genetics data.")
            """ A mannequin can't be used as the age/gender/extended_species source """
            """ A mannequin can't currently be used as a slider source """
            """ A mannequin can't currently be used as a genetics and physics source """
        else:
            resend_attributes = False
            # age-gender
            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_AGE_GENDER, ]:
                log.debug(f"Cloning base attributes (age, gender, species).")
                SimInfoBaseWrapper.copy_base_attributes(sim_info, src_sim_info)  # Order: dest, src
                resend_attributes = True

            # sliders
            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_SLIDERS, ]:
                log.debug(f"Cloning sliders.")
                sim_info.facial_attributes = src_sim_info.facial_attributes
                resend_attributes = True

            # genetics
            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_GENETICS, ]:
                log.debug(f"Cloning genetics.")
                SimInfoBaseWrapper.copy_genetic_data(sim_info, src_sim_info)
                resend_attributes = True

            # genetics and physics
            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_PHYSICS_GENETICS, ]:
                log.debug(f"Cloning physics and genetics.")
                SimInfoBaseWrapper.copy_physical_attributes(sim_info, src_sim_info)
                resend_attributes = True

            if resend_attributes:
                SimInfoBaseWrapper.resend_physical_attributes(sim_info)

        if src_sim_info is None or mannequin_component:
            log.debug(f"Mannequin can't neither distribute nor retrieve (gender related) traits, walk style and/or skill data.")
            """ A mannequin can't be used as the gender traits source or destination """
            """ A mannequin can't be used as the trait source or destination """
            """ A mannequin can't be used as the walk style source or destination """
            """ A mannequin can't be used as the skill source or destination """
        else:
            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_AGE_GENDER, ]:
                log.debug(f"Cloning age and gender related traits.")
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

            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_TRAITS, ]:
                log.debug(f"Cloning traits.")
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
                        log.warn(f"Could not add trait '{trait}' ({e}).")

            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_WALKSTYLE, ]:
                log.debug(f"Cloning walk style.")
                src_sim: Sim = CommonSimUtils.get_sim_instance(src_sim_info)
                sim: Sim = CommonSimUtils.get_sim_instance(sim_info)
                # sim.routing_component._walkstyle_requests = src_sim.routing_component._walkstyle_requests  # CAS to Game will fail, likely wrong 'sim'
                walkstyle_requests: list = src_sim.routing_component.get_walkstyle_requests()
                for walkstyle_request in walkstyle_requests:
                    WalkStyleRequest(sim, walkstyle=walkstyle_request.walkstyle, priority=walkstyle_request.priority)

            if group_id in [OutfitGroupId.EVERYTHING, OutfitGroupId.X_ALL, OutfitGroupId.X_SKILLS, ]:
                log.debug(f"Cloning skills.")
                """ not implemented """
                log.debug(f"Cloning skills is not yet implemented. Nothing will be clones.")

        log.debug(f"Sim Data clone completed.")

    def paste_outfit(self, zim: CopyOutfitsSim):
        sim_info = zim.sim_info
        action = zim.action
        action_id = zim.action_id
        outfit_category = zim.outfit_category
        outfit_index = zim.outfit_index
        clipboard_index = zim.clipboard_index

        valid_parts_ids = OutfitGroups.SIM_GARMENT.value  # Paste all outfit parts, nothing else.

        if action_id == PieMenuActionId.PICKER:
            self.open_outfit_picker(zim, action, None, None)
        elif action_id == PieMenuActionId.X_PICKER:
            occult_type: CommonOccultType = CommonSimOccultTypeUtils.determine_current_occult_type(sim_info)
            if zim.sim_age in [CopyOutfitsAge.PET, CopyOutfitsAge.HORSE, ]:
                log.warn(f"Pets, cats, dogs, foxes and/or horses shouldn't have special outfits (not supported by 'Copy Outfits').")
                OutfitNotifications().show_notification(f"Animals have no special outfits.")
                return True
            if occult_type in [CommonOccultType.MERMAID, CommonOccultType.ALIEN, ]:
                log.warn(f"Occult '{occult_type}' might have no special outfits. Expect an 'unexpected'000ffffffff exception.")
            OutfitNotifications().show_notification(f"Categories: All | Bathing.0 | Situation.0 | Career.0-2 | Special.0/Towel/Fashion | Batuu.0-4 .")
            self.open_outfit_picker(
                zim,
                action,
                (
                    (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.CAREER, 0), (OutfitCategory.CAREER, 1), (OutfitCategory.CAREER, 2),
                    (OutfitCategory.SPECIAL, SpecialOutfitIndex.DEFAULT), (OutfitCategory.SPECIAL, SpecialOutfitIndex.TOWEL), (OutfitCategory.SPECIAL, SpecialOutfitIndex.FASHION),
                    (OutfitCategory.BATUU, 0), (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                ),
                (OutfitCategory.CURRENT_OUTFIT, )
            )
        elif action_id == PieMenuActionId.ALL_OUTFITS_FOR_CATEGORY:
            i = OutfitPaste().paste_all(zim, valid_parts_ids)
            OutfitNotifications().show_notification(f"Pasted {i} outfit(s).")  # might be too high if clipboard has holes in it, eg .0 not set.

        else:
            log.debug(f"Pasting from clipboard '{clipboard_index}' to current outfit '{outfit_category}.{outfit_index}'")
            if OutfitPaste().paste(zim, valid_parts_ids, clipboard_index=clipboard_index) is True:
                self.apply_cas_parts(zim)
                OutfitNotifications().show_notification(f"Pasted outfit.")
            else:
                OutfitNotifications().show_notification(f"No outfit found in clipboard [{clipboard_index}].")

    def copy_outfit(self, zim: CopyOutfitsSim):
        sim_info = zim.sim_info
        sim_age = zim.sim_age
        sim_id = zim.sim_id
        action = zim.action
        action_id: PieMenuActionId = zim.action_id
        # outfit_category = zim.outfit_category
        outfit_index = zim.outfit_index
        clipboard_index = zim.clipboard_index
        outfit_name = zim.outfit_name

        SimStore.sims.update({sim_age: sim_id})
        if action_id == PieMenuActionId.PICKER:
            self.open_outfit_picker(zim, action, None, None)
        elif action_id == PieMenuActionId.X_PICKER:
            occult_type: CommonOccultType = CommonSimOccultTypeUtils.determine_current_occult_type(sim_info)
            if CommonSpeciesUtils.is_pet(sim_info):
                log.warn(f"Pets, cats, dogs, foxes and/or horses shouldn't have special outfits (not supported by 'Copy Outfits').")
                OutfitNotifications().show_notification(f"Animals have no special outfits.")
                return True
            if CommonOccultType.MERMAID == occult_type or CommonOccultType.ALIEN == occult_type:
                log.warn(f"Occult '{occult_type}' might have no special outfits. Expect than an unexpected exception gets thrown.")
            OutfitNotifications().show_notification(f"Categories: All | Bathing.0 | Situation.0 | Career.0-2 | Special.0/Towel/Fashion | Batuu.0-4 .")
            self.open_outfit_picker(
                zim,
                action,
                (
                    (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.CAREER, 0), (OutfitCategory.CAREER, 1), (OutfitCategory.CAREER, 2),
                    (OutfitCategory.SPECIAL, SpecialOutfitIndex.DEFAULT), (OutfitCategory.SPECIAL, SpecialOutfitIndex.TOWEL), (OutfitCategory.SPECIAL, SpecialOutfitIndex.FASHION),
                    (OutfitCategory.BATUU, 0), (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                ),
                (OutfitCategory.CURRENT_OUTFIT, )
            )
        elif action_id == PieMenuActionId.ALL_OUTFITS_FOR_CATEGORY:
            log.debug(f"Copying all '{outfit_name}' outfits")
            num_outfits = OutfitCopy().copy_all(zim)
            OutfitNotifications().show_notification(f"Copied {num_outfits} '{outfit_name}' outfit(s) to clipboards 0-{num_outfits}.")
        else:
            log.debug(f"Copying outfit '{outfit_name}.{outfit_index}' to clipboard {clipboard_index}")
            if OutfitCopy().copy(zim, clipboard_index) is True:
                OutfitNotifications().show_notification(f"Copied outfit '{outfit_name}.{outfit_index}' to clipboard {clipboard_index}")
