#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CopyOutfitsAge(CustomEnum):
    UNKNOWN: 'CopyOutfitsAge' = 2 ** 0
    TYAE: 'CopyOutfitsAge' = 2 ** 1  # Teen, Young Adult, Adult, Elder
    CHILD: 'CopyOutfitsAge' = 2 ** 2
    TODDLER: 'CopyOutfitsAge' = 2 ** 3
    INFANT: 'CopyOutfitsAge' = 2 ** 4
    BABY: 'CopyOutfitsAge' = 2 ** 5
    PET: 'CopyOutfitsAge' = 2 ** 10
    LARGE_DOG: 'CopyOutfitsAge' = 2 ** 11
    HORSE: 'CopyOutfitsAge' = 2 ** 12


