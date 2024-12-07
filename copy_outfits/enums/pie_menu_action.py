#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class PieMenuAction(CommonEnum):
    NONE = 0
    COPY = 1  # DEFAULT, ALL_OUTFITS_FOR_CATEGORY, PICKER, X-PICKER
    PASTE = 2  # DEFAULT, ALL_OUTFITS_FOR_CATEGORY, PICKER, X-PICKER
    CLONE_CAS_PARTS = 4  # ALL_OUTFITS_FOR_CATEGORY, ..., SIM
    CLONE_SIM_DATA = 8
    CLEAR = 16  # DEFAULT
    PRINT = 32  # DEFAULT
    ADD = 64  # Add outfits

    BODY_TYPE = 128  # TS4 CAS parts as defined in ts4lib.BodyType(CommonEnum) ea.outfits.BodyType(Enum)

    SKIN = 256  # Apply next head/skin to mannequin
    MANNEQUIN = 512  # Add mannequin

    RESERVED = 1024  # free

    FIX_HEAD = 2048
