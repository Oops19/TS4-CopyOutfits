from sims.sim_info_types import Age
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils


class O19COAge:
    TYAE = 0  # Teen, Young Adult, Adult, Elder
    CHILD = 1
    TODDLER = 2
    UNKNOWN = 3  # Cat, Dog, ...

    @staticmethod
    def get_age(sim_info) -> int:
        age = O19COAge.UNKNOWN
        if CommonSpeciesUtils.is_human(sim_info):
            if CommonAgeUtils.is_teen_adult_or_elder(sim_info):
                age = O19COAge.TYAE
            elif CommonAgeUtils.is_child(sim_info):
                age = O19COAge.CHILD
            elif CommonAgeUtils.is_toddler(sim_info):
                age = O19COAge.TODDLER
        return age

    '''
    ADULT = 0
    CHILD = 1
    TODDLER = 2
    UNKNOWN = 3

'''