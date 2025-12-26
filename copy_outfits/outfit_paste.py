#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from copy_outfits.modinfo import ModInfo

from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from copy_outfits.utils.copy_outfit_utilities import CopyOutfitUtilities
from copy_outfits.utils.outfit_modifiers import OutfitModifiers

from sims.outfits.outfit_utils import get_maximum_outfits_for_category
from ts4lib.custom_enums.custom_outfit_category import CustomOutfitCategory

from ts4lib.utils.outfit_utilities import OutfitUtilities
from ts4lib.utils.singleton import Singleton

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitPaste')
log.enable()


class OutfitPaste(metaclass=Singleton):
    def paste_all(self, zim: CopyOutfitsSim, valid_parts_ids) -> int:
        log.debug(f"Pasting all '{zim.outfit_name}' outfits to '{zim.sim_info}'")
        outfit_category = zim.outfit_category
        outfit_index = -1
        maximum_outfits = get_maximum_outfits_for_category(outfit_category)
        for outfit_index in range(0, maximum_outfits):
            if self.paste(zim, valid_parts_ids, clipboard_index=outfit_index, outfit_category=outfit_category, outfit_index=outfit_index) is False:
                return outfit_index
        return outfit_index

    # def copy(self, zim: CopyOutfitsSim, clipboard_index: int = 0, outfit_category: int = None, outfit_index: int = None) -> bool:
    def paste(self, zim: CopyOutfitsSim, valid_parts_ids, clipboard_index: int = 0, outfit_category: int = None, outfit_index: int = None, merge_parts: bool = False) -> bool:
        """
        @param zim: Copy parts from 'clipboard_index' to zim.sim_info outfit_category.outfit_index
        @param valid_parts_ids: The body type IDs to be replaced, e.g. HAT, SOCKS, SHOES, ...
        @param outfit_category:
        @param outfit_index:
        @param clipboard_index: Copy data from here.
        @param merge_parts: Set to True to merge the parts. If the sim has a HAT but there is nothing in clipboard it will keep the head
        @return:
        """
        sim_info = zim.sim_info
        sim_age = zim.sim_age
        outfit_name = zim.outfit_name
        if outfit_category is None:
            outfit_category = zim.outfit_category
            try:
                outfit_name = CustomOutfitCategory(outfit_category).name
            except:
                outfit_name = 'Unknown'
        if outfit_index is None:
            outfit_index = zim.outfit_index
        if clipboard_index is None:
            clipboard_index = zim.clipboard_index

        log.debug(f"Pasting outfit '{outfit_name}.{outfit_index}' to '{sim_info}' from clipboard '{clipboard_index}'")
        maximum_outfits = self._get_maximum_outfits_for_category(outfit_category)  # 1, 3 or 5
        if outfit_index >= maximum_outfits:
            log.info(f"Outfit '{outfit_name}' supports only {maximum_outfits} different outfit(s). Won't create '{outfit_name}.{outfit_index}'.")
            return False

        new_parts = CopyOutfitUtilities().get_parts_from_clipboard(sim_age, clipboard_index)
        # In case clipboard is empty skip it. The next clipboard might contain an outfit
        if new_parts:
            current_parts = CopyOutfitUtilities().get_body_parts(zim, outfit_category, outfit_index)
            merged_parts = CopyOutfitUtilities().merge_parts(current_parts, new_parts, valid_parts_ids, merge_parts=merge_parts)
            log.debug(f"Updating outfit '{outfit_name}.{outfit_index}'")
            OutfitUtilities().apply_outfit(sim_info, merged_parts, (outfit_category, outfit_index))
            OutfitModifiers().remove_all_outfit_appearance_modifiers(sim_info)
        return True

    # outfit_utils.py#def get_maximum_outfits_for_category(outfit_category):
    @staticmethod
    def _get_maximum_outfits_for_category(outfit_category):
        if outfit_category in [CustomOutfitCategory.BATHING, CustomOutfitCategory.SITUATION, ]:
            return 1
        elif outfit_category in [CustomOutfitCategory.SPECIAL, CustomOutfitCategory.CAREER, ]:
            return 3
        return 5
        # return get_maximum_outfits_for_category(outfit_category)
