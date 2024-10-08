#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict, Union

from copy_outfits.modinfo import ModInfo
from copy_outfits.enums.outfit_category import OutfitCategory
from copy_outfits.persist.outfit_store import OutfitStore
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from sims.outfits.outfit_enums import BodyType
from sims4communitylib.enums.tags_enum import CommonGameTag
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from ts4lib.utils.singleton import Singleton

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'CopyOutfitUtilities')
log.enable()


class CopyOutfitUtilities(metaclass=Singleton):

    @staticmethod
    def get_body_parts(zim: CopyOutfitsSim,  outfit_category: int, outfit_index: int) -> Dict[Union[BodyType, int], int]:
        if outfit_category is None:
            outfit_category = zim.outfit_category
        if outfit_index is None:
            outfit_index = zim.outfit_index
        if not CommonOutfitUtils.has_outfit(zim.sim_info, (outfit_category, outfit_index)):
            # Create an outfit for the sim with not too much cas parts
            tag_list = (CommonGameTag.OUTFIT_CATEGORY_BATHING, )
            CommonOutfitUtils.generate_outfit(zim.sim_info, (OutfitCategory.BATHING, 0), tag_list)
        return CommonOutfitUtils.get_outfit_parts(zim.sim_info, (outfit_category, outfit_index))

    @staticmethod
    def merge_parts(current_parts: Dict[Union[BodyType, int], int], new_parts: Dict[Union[BodyType, int], int], valid_parts_ids, merge_parts: bool = False) -> Dict:
        """
        @param current_parts: A dict with parts to use as a base {BodyPart: CasPartId, ...}
        @param new_parts: A dict with parts to apply {BodyPart: CasPartId, ...}
        @param valid_parts_ids: A list with BodyParts to apply. If they are in 'new_parts' they will be replaced in, otherwise they are removed.
        # A filter for the part ids to apply. All part ids will be removed from the current outfit. Part ids in this list will be copied from {new_parts}.
        @param merge_parts: CAS parts will not be dropped, even if they are missing in new_parts
        :return:
        """
        log.debug(f"current_parts = {current_parts}")
        log.debug(f"new_parts = {new_parts}")
        log.debug(f"valid_parts_ids = {valid_parts_ids}: {type(valid_parts_ids)}")

        merged_parts = current_parts.copy()
        for valid_part_id in valid_parts_ids:
            new_part = new_parts.get(valid_part_id, None)
            if merge_parts is True and new_part is None:
                continue  # Keep the old part
            merged_parts.update({valid_part_id: new_part})
            if new_part is None:
                del merged_parts[valid_part_id]  # merged_parts exists with None and can safely be deleted without raising an exception

        log.debug(f"merge_parts('{current_parts}', '{new_parts}', '{valid_parts_ids}', {merge_parts}) -> {merged_parts}")
        return merged_parts

    @staticmethod
    def get_parts_from_clipboard(sim_age: int, clipboard_index: int = 0) -> Dict:
        parts = {}
        outfit_for_age = OutfitStore.outfits.get(sim_age, {})
        if outfit_for_age:
            parts = outfit_for_age.get(clipboard_index, None)
            if parts:
                source = OutfitStore.outfits.get(sim_age).get(clipboard_index)
                debug_message = f"(with data from '{source}')"
            else:
                debug_message = f"(clipboard is empty)"
        else:
            debug_message = "(no outfits available for this age)"
        log.debug(f"get_parts_from_clipboard({sim_age}, {clipboard_index}) -> '{parts}' {debug_message}")
        if parts:
            return parts.copy()
        return {}
