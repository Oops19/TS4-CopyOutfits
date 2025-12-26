#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class DisplayPriority(CustomEnum):
    HIGHEST = 10
    VERY_HIGH = 9
    HIGH = 8
    ABOVE_AVERAGE = 7
    AVERAGE = 6
    BELOW_AVERAGE = 5
    LOW = 4
    VERY_LOW = 3
    MINIMAL = 2
    CLOSE_TO_NONE = 1
    NONE = 0
