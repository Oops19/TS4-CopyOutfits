#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Any, Tuple
from typing import Union

from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.enums.copy_outfits_mannequin import CopyOutfitsMannequin
from copy_outfits.enums.outfit_category import OutfitCategory
from copy_outfits.enums.outfit_group_id import OutfitGroupId
from copy_outfits.enums.pie_menu_action import PieMenuAction
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.modinfo import ModInfo
from objects.components.mannequin_component import MannequinComponent
from sims.sim_info import SimInfo
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_gender_utils import CommonGenderUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'CopyOutfitsSim')
log.enable()


class CopyOutfitsSim:
    def __init__(self, interaction_target: Union[SimInfo, MannequinComponent, Any], instance_tunables: Tuple[int, int, int, int, int, int]):

        log.debug(f"{interaction_target} {instance_tunables}")
        self.interaction_target = interaction_target
        self.sim_info: Union[SimInfo, SimInfoBaseWrapper, None] = None
        self.sim_id: int = CopyOutfitsMannequin.SIM_ID_NONE.value
        self.sim_age: CopyOutfitsAge = CopyOutfitsAge.UNKNOWN
        self.is_female: bool = None
        self.mannequin_component: Union[MannequinComponent, None] = None
        self.sim_name = 'Unknown#Unknown'
        self.outfit_name = 'Unknown'

        _action, _action_id, _group_id, self.clipboard_index, self.outfit_category, self.outfit_index = instance_tunables
        self.action = PieMenuAction(_action)
        self.action_id = PieMenuActionId(_action_id)
        self.group_id = OutfitGroupId(_group_id)

        try:
            self.sim_info: SimInfo = CommonSimUtils.get_sim_info(interaction_target)
            self.sim_name = f"{self.sim_info}"
            self.sim_id: int = self.sim_info.sim_id  # throws an exception if sim_info is None --> Mannequin
            self.sim_age: CopyOutfitsAge = self.get_age(self.sim_info)
            if CommonGenderUtils.is_female(self.sim_info) is True:
                self.is_female = True
            elif CommonGenderUtils.is_male(self.sim_info) is True:
                self.is_female = False
            self.mannequin_component = None
        except:
            if f"{interaction_target}".startswith('object_Mannequin'):
                self.mannequin_component = interaction_target.mannequin_component
                self.sim_info = getattr(self.mannequin_component, '_sim_info_data', None)
                self.sim_name = 'Mannequin'

                if f"{interaction_target}".startswith('object_Mannequin_Adult'):
                    self.sim_id = CopyOutfitsMannequin.SIM_ID_MANNEQUIN_ADULT
                    self.sim_age = CopyOutfitsAge.TYAE
                    if f"{interaction_target}".startswith('object_Mannequin_AdultFemale'):
                        self.is_female = True
                    elif f"{interaction_target}".startswith('object_Mannequin_AdultMale'):
                        self.is_female = False
                    else:
                        log.warn(f"Can get gender for {interaction_target}")

                elif f"{interaction_target}".startswith('object_Mannequin_Child'):
                    self.sim_id = CopyOutfitsMannequin.SIM_ID_MANNEQUIN_CHILD
                    self.sim_age = CopyOutfitsAge.CHILD
                    if f"{interaction_target}".startswith('object_Mannequin_ChildFemale'):
                        self.is_female = True
                    elif f"{interaction_target}".startswith('object_Mannequin_ChildMale'):
                        self.is_female = False
                    else:
                        log.warn(f"Can get gender for {interaction_target}")

                else:
                    log.warn(f"Error getting sim_id for interaction_target: '{type(interaction_target)}' = '{interaction_target}'; sim_info: '{type(self.sim_info)}' = '{self.sim_info}'")
            elif f"{interaction_target}".startswith('TerrainPoint'):
                self.sim_info = None
                self.sim_id = CopyOutfitsMannequin.SIM_ID_NONE.value
                self.sim_age = CopyOutfitsAge.UNKNOWN
                self.is_female: bool = None
                self.sim_name = 'Terrain#Terrain'
                self.outfit_name = 'Terrain'
                log.debug(f"TerrainPoint, setting only '{self.action}' and '{self.action_id}'")
            else:
                log.warn(f"Error getting sim_id for interaction_target: '{type(interaction_target)}' = '{interaction_target}'")

        if self.sim_info:
            if self.outfit_category == -1:
                self.outfit_category = CommonOutfitUtils.get_current_outfit_category(self.sim_info)
            if self.outfit_index == -1:
                self.outfit_index = CommonOutfitUtils.get_current_outfit_index(self.sim_info)
            try:
                self.outfit_name = OutfitCategory(self.outfit_category).name
            except:
                pass

        log.debug(f"Setting sim_info={self.sim_info}; sim_id={self.sim_id}; sim_age={self.sim_age.name}; sim_outfit={self.outfit_name}.{self.outfit_index}")

    @staticmethod
    def get_age(sim_info: SimInfo) -> CopyOutfitsAge:
        """ Return a simplified 'Age' to store outfits for 'each' age (joining Teen to Elder into one age) or species. """
        age = CopyOutfitsAge.UNKNOWN
        if CommonSpeciesUtils.is_human(sim_info):
            if CommonAgeUtils.is_teen_adult_or_elder(sim_info):
                age = CopyOutfitsAge.TYAE
            elif CommonAgeUtils.is_child(sim_info):
                age = CopyOutfitsAge.CHILD
            elif CommonAgeUtils.is_toddler(sim_info):
                age = CopyOutfitsAge.TODDLER
            elif CommonAgeUtils.is_infant(sim_info):
                age = CopyOutfitsAge.INFANT
            elif CommonAgeUtils.is_baby(sim_info):
                age = CopyOutfitsAge.BABY
            elif CommonSpeciesUtils.is_large_dog(sim_info):
                age = CopyOutfitsAge.LARGE_DOG
            elif CommonSpeciesUtils.is_horse(sim_info):
                age = CopyOutfitsAge.HORSE
            elif CommonSpeciesUtils.is_pet(sim_info):  # Small Dog, Cat, Fox share the same slot du to their size
                age = CopyOutfitsAge.PET
        return age
