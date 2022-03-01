from typing import Any, Tuple, Union

from outfit_tools.struct.action import O19OTAction
from outfit_tools.struct.actions_id import O19OTActionId
from outfit_tools.struct.age import O19OTAge
from outfit_tools.struct.internal_stbl import InternalSTBL
from outfit_tools.modinfo import ModInfo
from outfit_tools.struct.outfit_store import O19OTOutfitStore

from event_testing.results import TestResult
from interactions.context import InteractionContext
from sims.outfits.outfit_enums import OutfitCategory
from sims.sim import Sim
from sims.sim_info import SimInfo
from sims4.tuning.tunable import Tunable
from ui.ui_dialog_notification import UiDialogNotification

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

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, 'interactions')
log.enable()


class O19OTDD:
    installed = False


# noinspection PyBroadException
try:
    from deviousdesires.nudity_system.utils.nudity_system_utils import DDNuditySystemUtils
    from deviousdesires.nudity_system.enums.part_handle_type import DDPartHandleType
    from deviousdesires.nudity_system.enums.part_layer import DDPartLayer

    O19OTDD.installed = True
except:
    pass


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
        age = O19OTAge.get_age(sim_info)

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
        outfit_name = O19OTOutfitStore.outfit_categories.get(outfit_category)

        log.debug(f"on_started({interaction_sim}, {interaction_target}) a={action}.{action_id} o={outfit_name}[{outfit_index}] upd={update_outfit}")

        # action: 1 Copy || 2 Paste || 4 O19OTActionId || 8 Clear || 16 Print
        # action_id: 0..100
        # outfit_index: 0..5 | -1 Default
        # outfit_category: 0..12 | -1 Default
        # clipboard_index: 0..4
        if action == O19OTAction.PRINT:
            log.debug(f"Outfits: {O19OTOutfitStore.outfits}")
            age_data = self.get_parts(age)
            message = ''
            if age_data:
                message = f"Sources for age {age}:\n"
                for i in range(0, 5):
                    try:
                        message = f"{message}{i}: {age_data.get(i).get('source')}\n"
                    except:
                        pass
            else:
                message = "No outfits found in clipboard."
            self.show_notification(message)

        elif action == O19OTAction.CLEAR:
            # Clear
            if action_id == O19OTActionId.ALL:
                del O19OTOutfitStore.outfits
                O19OTOutfitStore.outfits = dict()
                self.show_notification(f"Removed all outfits from clipboard")
            else:
                age_data = self.get_parts(age)
                if age_data:
                    age_data.update({clipboard_index: None})
                    del age_data[clipboard_index]
                    O19OTOutfitStore.outfits.update({age: age_data})
                    self.show_notification(f"Removed outfit {clipboard_index} from clipboard.")

        elif action == O19OTAction.CLONE:
            log.debug("Clone")
            new_parts = self.get_parts(age, clipboard_index)
            if not new_parts:
                self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")
                return False
            if action_id == O19OTActionId.ALL:
                sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=new_parts, mod_identity=ModInfo.get_identity())
                sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))
            else:
                valid_parts_ids = O19OTOutfitStore.parts[action_id]
                merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
                sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
                sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))

        elif action == O19OTAction.PASTE:
            log.debug('Paste')
            really_update_outfit = True
            valid_parts_ids = O19OTOutfitStore.parts[O19OTActionId.CLOTH]
            if action_id == O19OTActionId.PICKER:
                self.open_outfit_picker(sim_info, action, None, None)
            elif action_id == O19OTActionId.XPICKER:
                self.open_outfit_picker(
                    sim_info, action, (
                        (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.SPECIAL, 0), (OutfitCategory.SPECIAL, 1),
                        (OutfitCategory.CAREER, 0), (OutfitCategory.CAREER, 1), (OutfitCategory.CAREER, 2), (OutfitCategory.BATUU, 0),
                        (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                    ), (OutfitCategory.CURRENT_OUTFIT,)
                )
            elif action_id == O19OTActionId.ALL:
                i = 0
                log.debug(f"Pasting all outfits to '{outfit_name}'")
                for outfit_index in range(0, 5):
                    new_parts = self.get_parts(age, outfit_index)
                    if new_parts:
                        merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
                        sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
                        sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))
                        i += 1

                        # Copy 1 outfit
                        if outfit_category == OutfitCategory.BATHING or outfit_category == OutfitCategory.SITUATION:
                            break
                        # Copy 2 outfits (SPECIAL.1 == Towel)
                        if outfit_category == OutfitCategory.SPECIAL and outfit_index == 1:
                            break
                        # Copy 3 outfits
                        if outfit_category == OutfitCategory.CAREER and outfit_index == 2:
                            break

                self.show_notification(f"Pasted {i} outfit(s) to '{outfit_name}'.")
            elif 100 <= clipboard_index <= 104:
                clipboard_index -= 100
                log.debug(f"Paste from clipboard '{clipboard_index}' to current outfit '{outfit_category}[{outfit_index}]'")
                new_parts = self.get_parts(age, clipboard_index)
                if new_parts:
                    merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids)
                    sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
                    sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))
                    # self.show_notification() - user will see it
                else:
                    self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")
            else:
                log.debug(f"Paste to outfit '{outfit_name}[{outfit_index}]' (from clipboard '{clipboard_index}')")
                if (outfit_category == OutfitCategory.BATHING or outfit_category == OutfitCategory.SITUATION) and outfit_index > 0 \
                        or outfit_category == OutfitCategory.SPECIAL and outfit_index > 1 \
                        or outfit_category == OutfitCategory.CAREER and outfit_index > 2:
                    self.show_notification(f"Can't paste tp '{outfit_category}[{outfit_index}]'.")
                    return False

                new_parts = self.get_parts(age, clipboard_index)
                if new_parts:
                    merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids, (outfit_category, outfit_index))
                    sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
                    sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))
                    self.show_notification(f"Pasted outfit to '{outfit_name}[{outfit_index}]'.")
                else:
                    self.show_notification(f"No outfit found in clipboard [{clipboard_index}].")

        elif action == O19OTAction.COPY:
            # Copy
            if action_id == O19OTActionId.PICKER:
                self.open_outfit_picker(sim_info, action, None, None)
            elif action_id == O19OTActionId.XPICKER:
                self.open_outfit_picker(
                    sim_info, action, (
                        (OutfitCategory.BATHING, 0), (OutfitCategory.SITUATION, 0), (OutfitCategory.SPECIAL, 0), (OutfitCategory.SPECIAL, 1),
                        (OutfitCategory.CAREER, 0), (OutfitCategory.CAREER, 1), (OutfitCategory.CAREER, 2), (OutfitCategory.BATUU, 0),
                        (OutfitCategory.BATUU, 1), (OutfitCategory.BATUU, 2), (OutfitCategory.BATUU, 3), (OutfitCategory.BATUU, 4),
                    ), (OutfitCategory.CURRENT_OUTFIT,)
                )
            elif action_id == O19OTActionId.ALL:
                i = 0
                log.debug(f"Copying all outfits for '{outfit_name}'")
                age_data = self.get_parts(age)
                for outfit_index in range(0, 5):
                    parts = CommonOutfitUtils.get_outfit_parts(sim_info, (outfit_category, outfit_index))
                    if parts:
                        age_data.update({outfit_index: {'source': f'{sim_info} {outfit_category}[{outfit_index}]', 'parts': parts}})
                        i += 1
                O19OTOutfitStore.outfits.update({age: age_data})
                self.show_notification(f"Copied {i} '{outfit_name}' outfit(s) to clipboard.")
            else:
                log.debug(f"Copying outfit {outfit_name}[{outfit_index}] to clipboard '{clipboard_index}'")
                parts = CommonOutfitUtils.get_outfit_parts(sim_info, (outfit_category, outfit_index))
                if parts:
                    age_data = self.get_parts(age)
                    age_data.update({clipboard_index: {'source': f'{sim_info} {int(outfit_category)}[{outfit_index}]', 'parts': parts}})
                    O19OTOutfitStore.outfits.update({age: age_data})
                    self.show_notification(f'Copied outfit {outfit_name}[{outfit_index}] to clipboard {clipboard_index}.')

        if really_update_outfit and update_outfit:
            log.debug(f"Updating outfit '{outfit_name}[{outfit_index}]'")
            sim_info.set_outfit_dirty(outfit_category)
            sim_info.set_current_outfit((outfit_category, outfit_index))
        if O19OTDD.installed:
            for body_type in O19OTOutfitStore.parts[O19OTActionId.ALL]:
                DDNuditySystemUtils().set_equipment_part_to_layer_by_body_location(sim_info, body_type, DDPartLayer.OUTERWEAR)
        return True

    def open_outfit_picker(self, sim_info: SimInfo, action: int, outfit_list: Union[None, Tuple[OutfitCategory, int]] = None, exclude_outfit_categories: Union[None, Tuple[OutfitCategory]] = None):
        log.debug(f"show_outfit_picker({action}, {outfit_list}, {exclude_outfit_categories})")

        def _on_chosen(choice: Tuple[OutfitCategory, int], outcome: CommonChoiceOutcome):
            if outcome == CommonChoiceOutcome.CHOICE_MADE:
                self.process_pick(sim_info, action, choice)

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.TS4_SIM_NAME, tokens=(sim_info,), ),)
            if action == O19OTAction.COPY:
                # InternalSTBL.O19_SOURCE = 'Source'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_SOURCE, text_color=CommonLocalizedStringColor.GREEN),)
            else:
                # InternalSTBL.O19_TARGET = 'Target'
                description_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.O19_TARGET, text_color=CommonLocalizedStringColor.RED),)
            from sims4communitylib.utils.common_icon_utils import CommonIconUtils
            dialog = CommonChooseOutfitDialog(
                ModInfo.get_identity(),
                InternalSTBL.TS4_STRING,  # '{0.String}'
                InternalSTBL.O19_SELECT___OUTFIT,  # 'Select {0.String} Outfit'
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
        age = O19OTAge.get_age(sim_info)
        clipboard_index = 0
        outfit_category, outfit_index = choice
        outfit_name = O19OTOutfitStore.outfit_categories.get(outfit_category)
        valid_parts_ids = O19OTOutfitStore.parts[O19OTActionId.CLOTH]

        if action == O19OTAction.PASTE:
            log.debug(f"Paste to outfit '{outfit_name}[{outfit_index}]' for '{sim_info}' (from clipboard '{clipboard_index}')")
            new_parts = self.get_parts(age, clipboard_index)
            if new_parts:
                merged_parts = self.merge_parts(sim_info, new_parts, valid_parts_ids, (outfit_category, outfit_index))
                sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=merged_parts, mod_identity=ModInfo.get_identity())
                sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))

                log.debug(f"Updating outfit '{outfit_name}[{outfit_index}]'")
                sim_info.set_outfit_dirty(outfit_category)
                sim_info.set_current_outfit((outfit_category, outfit_index))
                if O19OTDD.installed:
                    # remove all appearance modifiers
                    for body_type in O19OTOutfitStore.parts[O19OTActionId.ALL]:
                        DDNuditySystemUtils().set_equipment_part_to_layer_by_body_location(sim_info, body_type, DDPartLayer.OUTERWEAR)

        elif action == O19OTAction.COPY:
            log.debug(f"Copying '{sim_info}'s outfit {outfit_name}[{outfit_index}] to clipboard '{clipboard_index}'")
            parts = CommonOutfitUtils.get_outfit_parts(sim_info, choice)
            if parts:
                age_data = self.get_parts(age)
                age_data.update({clipboard_index: {'source': f'{sim_info} {outfit_category}[{outfit_index}]', 'parts': parts}})
                O19OTOutfitStore.outfits.update({age: age_data})
                self.show_notification(f"Copied outfit '{outfit_name}[{outfit_index}]' to clipboard {clipboard_index}.")

        else:
            log.error(f"process_pick('{sim_info}', '{action}', '{choice})' -> (unknown action)", throw=False)

    @staticmethod
    def get_parts(age: int, clipboard_index: int = -1) -> dict:
        parts = dict()
        debug_message = ''
        age_data = O19OTOutfitStore.outfits.get(age, dict())
        if age_data:
            if clipboard_index == -1:
                parts = age_data
                debug_message = ' (clipboard)'
            else:
                clipboard_data = age_data.get(clipboard_index, dict())
                if clipboard_data:
                    parts = clipboard_data.get('parts')
                else:
                    debug_message = ' (clipboard empty)'
        else:
            debug_message = ' (age empty)'
        log.debug(f"get_parts({age}, {clipboard_index}) -> '{parts}'{debug_message}")
        return parts

    @staticmethod
    def merge_parts(sim_info, new_parts, valid_parts_ids, outfit_category_and_index: Union[Tuple, None] = None) -> dict:
        """
        :param sim_info: The sim  whose outfit is to be modified
        :param new_parts: A list with parts to apply
        :param valid_parts_ids: A filter for the part ids to apply. All part ids will be removed from the current outfit. Part ids in this list will be copied from {new_parts}.
        :param outfit_category_and_index optional to specify an outfit
        :return:
        """

        if not outfit_category_and_index:
            outfit_category_and_index: Tuple = (CommonOutfitUtils.get_current_outfit_category(sim_info), CommonOutfitUtils.get_current_outfit_index(sim_info))
        current_parts: dict = CommonOutfitUtils.get_outfit_parts(sim_info, outfit_category_and_index).copy()
        log.debug(f"merge_parts() current_parts = {current_parts}")
        log.debug(f"merge_parts() valid_part_id = {valid_parts_ids}")
        log.debug(f"merge_parts() new_parts = {new_parts}")

        for valid_part_id in valid_parts_ids:
            new_part = new_parts.get(valid_part_id, None)
            if new_part:
                current_parts.update({valid_part_id: new_part})
            elif current_parts.get(valid_part_id, None):
                del current_parts[valid_part_id]

        log.debug(f"merge_parts() merged_parts = {new_parts}")
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
            title_tokens=(mod_identifier,),  # 'Outfit Tools'
            description_tokens=(message,),
            urgency=urgency
        )
        basic_notification.show()

# r outfit_tools.interactions
