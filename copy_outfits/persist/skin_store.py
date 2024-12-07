#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from random import randint
from typing import Dict, List, Set

from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SkinStore')
log.enable()


class SkinStore(metaclass=Singleton):
    def __init__(self, config: Dict):
        log.debug(f'init')
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
        if config:
            self.config = config
        else:
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

        for sim_age in [CopyOutfitsAge.CHILD, CopyOutfitsAge.TYAE, ]:
            _age_sizes = {}
            for is_female in [True, False, ]:
                _age_sizes.update({is_female: len(config.get(sim_age).get(is_female))})
            self.size.update({sim_age: _age_sizes})
        log.debug(f"size = {self.size}")
        log.debug(f"config = {self.config}")

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
