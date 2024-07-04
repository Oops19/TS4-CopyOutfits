#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from random import randint
from typing import Dict, List, Set

from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.modinfo import ModInfo
from sims4communitylib.utils.cas.common_cas_utils import CommonCASUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SkinStore')
log.enable()


class SkinStore(metaclass=Singleton):
    def __init__(self, config: Dict):
        self.index = {
            CopyOutfitsAge.TYAE: {
                True: 0,
                False: 0,
            },
            CopyOutfitsAge.CHILD: {
                True: 0,
                False: 0,
            },
        }
        self.config = {
            CopyOutfitsAge.TYAE: {
                True: [],
                False: [],
            },
            CopyOutfitsAge.CHILD: {
                True: [],
                False: [],
            },
        }
        self.size = {
            CopyOutfitsAge.TYAE: {
                True: 0,
                False: 0,
            },
            CopyOutfitsAge.CHILD: {
                True: 0,
                False: 0,
            },
        }
        missing_packages: Set = set()
        for age, gender_data in config.items():
            gender_size = {}
            for gender, cas_parts in gender_data.items():
                existing_cas_parts = []
                for cas_part in cas_parts:
                    check_cas_part, use_cas_part, package_name = cas_part
                    if CommonCASUtils.is_cas_part_loaded(check_cas_part):
                        if CommonCASUtils.is_cas_part_loaded(use_cas_part):
                            existing_cas_parts.append(use_cas_part)
                        else:
                            log.warn(f"copy_outfits.package missing or broken - {use_cas_part:016X} not found!")
                    else:
                        missing_packages.add(package_name)
                        log.warn(f"Dropping: {cas_part}")
                gender_data.update({gender: existing_cas_parts})
                gender_size.update({gender: len(existing_cas_parts)})
            self.config.update({age: gender_data})
            self.size.update({age: gender_size})

        if missing_packages:
            log.info(f"Optional packages which are not installed: '{missing_packages}'. Install some of them to use more skins on mannequins.")
        log.debug(f"self.size = {self.size}")
        log.debug(f"self.config = {self.config}")

    def get_skin(self, age: CopyOutfitsAge, is_female: bool = True, offset: int = 1, random_offset: bool = False):
        size = self.size.get(age).get(is_female)
        if size == 0:
            return None
        index = self.index.get(age).get(is_female)
        log.debug(f"index {self.index.get(age).get(is_female)}")
        if random_offset or offset:
            if random_offset:
                offset = randint(1, size)
            index += offset
            while index < 0:
                index += size
            while index >= size:
                index -= size
            self.index.get(age).update({is_female: index})
            log.debug(f"index {self.index.get(age).get(is_female)}")

        cas_parts: List = self.config.get(age).get(is_female)
        log.debug(f"get_skin -> index {index} . {cas_parts[index]} -  cas_parts {cas_parts} ")
        cas_part = cas_parts[index]
        return cas_part
