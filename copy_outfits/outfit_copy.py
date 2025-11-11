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
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from ts4lib.utils.singleton import Singleton

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitCopy')
log.enable()


class OutfitCopy(metaclass=Singleton):

    def copy_all(self, zim: CopyOutfitsSim) -> int:
        log.debug(f"Copying all '{zim.outfit_name}' outfits of '{zim.sim_info}'")
        outfit_category = zim.outfit_category
        outfit_index = -1
        for outfit_index in range(0, 5):
            if self.copy(zim, clipboard_index=outfit_index, outfit_category=outfit_category, outfit_index=outfit_index) is False:
                return outfit_index
        return outfit_index

    def copy(self, zim: CopyOutfitsSim, clipboard_index: int = 0, outfit_category: int = None, outfit_index: int = None) -> bool:
        sim_info = zim.sim_info
        sim_name = zim.sim_name
        outfit_name = zim.outfit_name
        if outfit_category is None:
            outfit_category = zim.outfit_category
            try:
                outfit_name = OutfitCategory(outfit_category).name
            except:
                outfit_name = 'Unknown'
        if outfit_index is None:
            outfit_index = zim.outfit_index
        if clipboard_index is None:
            clipboard_index = zim.clipboard_index

        log.debug(f"Copying {sim_name}'s outfit '{outfit_name}.{outfit_index}' to clipboard {clipboard_index}")
        if not CommonOutfitUtils.has_outfit(sim_info, (outfit_category, outfit_index)):
            log.warn(f"'{sim_info}' has no outfit '{outfit_name}.{outfit_index}'.")
            return False

        log.debug(f"Copying '{sim_info}'s outfit '{outfit_name}.{outfit_index}' to clipboard '{clipboard_index}'")
        parts = CommonOutfitUtils.get_outfit_parts(sim_info, (outfit_category, outfit_index))
        if parts:
            self.save_outfit(zim, outfit_index, clipboard_index, parts)
            return True
        else:
            return False

    @staticmethod
    def save_outfit(zim: CopyOutfitsSim, outfit_index: int, clipboard_index: int, parts: Dict[Union[BodyType, int], int]):
        sim_name = zim.sim_name
        sim_age = zim.sim_age
        outfit_name = zim.outfit_name
        clipboard_data_outfits: Dict = OutfitStore.outfits.get(sim_age, {})
        clipboard_data_outfits.update({clipboard_index: parts})

        clipboard_data_sources: Dict = OutfitStore.sources.get(sim_age, {})
        clipboard_data_sources.update({clipboard_index: f"{sim_name} {outfit_name}.{outfit_index}"})

        OutfitStore.outfits.reset_motives({sim_age: clipboard_data_outfits})
        OutfitStore.sources.reset_motives({sim_age: clipboard_data_sources})
        log.debug(f"Saved outfit for age '{sim_age}' to clipboard '{clipboard_index}' with '{parts}'.")
