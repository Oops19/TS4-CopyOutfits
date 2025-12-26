#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class VariousFilters(CustomEnum):
    NONE = 0
    # = 2 ** 0
    GENDER = 2 ** 1
    TRAITS = 2 ** 2
    WALKSTYLE = 2 ** 3
    GENETICS = 2 ** 4
    ALL_PHYSICS = 2 ** 5
    SPECIES = 2 ** 6
    FACE_SLIDERS = 2 ** 7
    BODY_SLIDERS = 2 ** 8
    SCULPTS = 2 ** 9
    RELATIONSHIPS = 2 ** 10

    @classmethod
    def _missing_(cls, key_value):
        """
        Return a default or a random enum value.
        @param key_value: Can either be the value `Enum(value)` (usually int; str or float) or the key `Enum.KEY ==> KEY` (usually str).
        """
        return cls.NONE