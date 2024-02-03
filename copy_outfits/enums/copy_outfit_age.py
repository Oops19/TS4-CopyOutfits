#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils
from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class CopyOutfitsAge(CommonEnum):
    UNKNOWN = 2 ** 0  # Cat, Dog
    TYAE = 2 ** 1  # Teen, Young Adult, Adult, Elder
    CHILD = 2 ** 2
    TODDLER = 2 ** 3
    INFANT = 2 ** 4
    BABY = 2 ** 5
    PET = 2 ** 6

    @staticmethod
    def get_co_age(sim_info) -> int:
        """ Return a simplified 'Age' to store outfits for 'each' age (joining Teen..Elder into one age). """
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
        elif CommonSpeciesUtils.is_pet(sim_info):
            age = CopyOutfitsAge.PET
        return age
