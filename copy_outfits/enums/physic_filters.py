#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class PhysicFilters(CommonEnum):
    NONE = 0
    # = 2 ** 0
    PHYSIQUE = 2 ** 1
    FACIAL_ATTRIBUTES = 2 ** 2
    VOICE_PITCH = 2 ** 3
    VOICE_ACTOR = 2 ** 4
    VOICE_EFFECT = 2 ** 5
    SKIN_TONE = 2 ** 6
    SKIN_TONE_VAL_SHIFT = 2 ** 7
    FLAGS = 2 ** 8
    PELT_LAYERS = 2 ** 9
    BASE_TRAIT_IDS = 2 ** 10
    GENETIC_DATA = 2 ** 11

    @classmethod
    def _missing_(cls, key_value):
        """
        Return a default or a random enum value.
        @param key_value: Can either be the value `Enum(value)` (usually int; str or float) or the key `Enum.KEY ==> KEY` (usually str).
        """
        return cls.NONE