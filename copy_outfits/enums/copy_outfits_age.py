#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class CopyOutfitsAge(CommonEnum):
    UNKNOWN = 2 ** 0
    TYAE = 2 ** 1  # Teen, Young Adult, Adult, Elder
    CHILD = 2 ** 2
    TODDLER = 2 ** 3
    INFANT = 2 ** 4
    BABY = 2 ** 5
    PET = 2 ** 10
    LARGE_DOG = 2 ** 11
    HORSE = 2 ** 12


