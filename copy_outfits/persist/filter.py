#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import List, Union

from copy_outfits.enums.outfit_groups import OutfitGroups
from copy_outfits.enums.physic_filters import PhysicFilters
from copy_outfits.enums.various_filters import VariousFilters
from copy_outfits.modinfo import ModInfo
from ts4lib.common_enums.body_part import BodyPart
from ts4lib.utils.singleton import Singleton
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class Filter(object, metaclass=Singleton):
    def __init__(self):
        self._enabled = False
        self._filter_body_parts = set()
        self._filter_various = set()
        self._filter_physics = set()

    def enable_filter(self, enable: bool = True):
        self._enabled = enable

    def filter_body_parts(self, body_parts: Union[bool, List[str]] = False):
        """
        @param body_parts: False to filter nothing; True to filter all body parts; List[str] to specify individual body parts
        """
        if body_parts is True:
            self._filter_body_parts = {e.value for e in BodyPart}
        elif body_parts is False:
            self._filter_body_parts = {}
        elif body_parts:
            for body_part in body_parts:
                bp = getattr(BodyPart, body_part)
                if bp:
                    self._filter_body_parts.add(bp.value)
        log.debug(f"Excluded BodyPart IDs: {self._filter_body_parts}")

    def clear_filter_body_parts(self, body_parts: List[str]):
        """
        @param body_parts: List[str] with BodyParts to remove from filter
        """
        if body_parts:
            for body_part in body_parts:
                bp = getattr(BodyPart, body_part)
                if bp and bp in self._filter_body_parts:
                    self._filter_body_parts.remove(bp)
        log.debug(f"Excluded BodyPart IDs: {self._filter_body_parts}")

    def filter_outfit_groups(self, outfit_groups: List[str]):
        for outfit_group in outfit_groups:
            body_parts: List = getattr(OutfitGroups, outfit_group)
            self.filter_body_parts(body_parts)

    def clear_filter_outfit_groups(self, outfit_groups: List[str]):
        for outfit_group in outfit_groups:
            body_parts: List = getattr(OutfitGroups, outfit_group)
            self.clear_filter_body_parts(body_parts)

    def filter_various(self, attributes: Union[bool, List[str]] = False):
        """
        @param attributes: False to filter nothing; True to filter all attributes; List[str] to specify individual attributes
        """
        if attributes is True:
            self._filter_body_parts = {e.value for e in BodyPart}
        elif attributes is False:
            self._filter_body_parts = {}
        elif attributes:
            for attribute in attributes:
                at = getattr(VariousFilters, attribute)
                if at:
                    self._filter_various.add(at.value)
        log.debug(f"Excluded Attributes IDs: {self._filter_various}")

    def clear_filter_various(self, attributes: List[str]):
        if attributes:
            for attribute in attributes:
                at = getattr(VariousFilters, attribute)
                if at and at in self._filter_various:
                    self._filter_various.remove(at)
        log.debug(f"Excluded Attributes IDs: {self._filter_various}")

    def filter_physiques(self, physiques: Union[bool, List[str]] = False):
        """
        @param physiques: False to filter nothing; True to filter all physiques; List[str] to specify individual physiques
        """
        if physiques is True:
            self._filter_body_parts = {e.value for e in BodyPart}
        elif physiques is False:
            self._filter_body_parts = {}
        elif physiques:
            for physique in physiques:
                ph = getattr(PhysicFilters, physique)
                if ph:
                    self._filter_physics.add(ph.value)
        log.debug(f"Excluded Physics IDs: {self._filter_physics}")

    def clear_filter_physiques(self, physiques: List[str]):
        if physiques:
            for physique in physiques:
                ph = getattr(PhysicFilters, physique)
                if ph and ph in self._filter_physics:
                    self._filter_physics.remove(ph)
        log.debug(f"Excluded Attributes IDs: {self._filter_various}")