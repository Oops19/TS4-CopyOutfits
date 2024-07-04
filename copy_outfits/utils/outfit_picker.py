#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Union, Tuple

from copy_outfits.enums.outfit_category import OutfitCategory
from copy_outfits.enums.pie_menu_action import PieMenuAction
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from copy_outfits.struct.internal_stbl import InternalSTBL
from copy_outfits.modinfo import ModInfo
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_choose_outfit_dialog import CommonChooseOutfitDialog
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'BodyPartPicker')
log.enable()


class BodyPartPicker:
    """ ... """
    r'''
    TODO Adjust so we can add 130 BodyTypes and their part descriptions
    Currently not used!
    '''
    def open_body_part_picker(self, zim: CopyOutfitsSim, action: int, outfit_list: Union[None, Tuple[OutfitCategory, int]] = None, exclude_outfit_categories: Union[None, Tuple[OutfitCategory]] = None):
        sim_info = zim.sim_info

        log.debug(f"show_outfit_picker({action}, {outfit_list}, {exclude_outfit_categories})")

        def _on_chosen(choice: Tuple[OutfitCategory, int], outcome: CommonChoiceOutcome):
            if outcome == CommonChoiceOutcome.CHOICE_MADE:
                """ callback() """
                # self.process_pick(zim, action, choice)

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string(InternalSTBL.TS4_SIM_NAME, tokens=(sim_info,), ),)
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
