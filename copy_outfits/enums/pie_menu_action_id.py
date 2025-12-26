#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class PieMenuActionId(CustomEnum):
    """
    # None | All | Body Paint | Cloth | Hand Accessories | Head Accessories | Head Paint | Head Piercings | Occult Scars | Pet | Sim
    OutfitGroups.parts: List uses this order
    """
    NONE = 0
    SELECTED = 1
    ALL_OUTFITS_FOR_CATEGORY = 2

    PICKER = 100
    X_PICKER = 101

    SAME_SKIN = 200
    NEXT_SKIN = 201
    PREVIOUS_SKIN = 202
    RANDOM_SKIN = 203

    MANNEQUIN_YF = 205
    MANNEQUIN_YM = 206
    MANNEQUIN_CF = 207
    MANNEQUIN_CM = 208

    MANNEQUIN_ROTATE_ZERO = 210
    MANNEQUIN_ROTATE_LEFT = 211
    MANNEQUIN_ROTATE_RIGHT = 212

    MANNEQUIN_REMOVE = 219
