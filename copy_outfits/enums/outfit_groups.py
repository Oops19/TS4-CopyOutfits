#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
from ts4lib.custom_enums.custom_body_type import CustomBodyType
from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class OutfitGroups(CustomEnum):

    PET_ALL = [
        CustomBodyType.FUR_BODY.value, CustomBodyType.EARS.value, CustomBodyType.TAIL.value,
    ]

    HORSE_ALL = [
        CustomBodyType.SADDLE.value, CustomBodyType.BRIDLE.value, CustomBodyType.REINS.value, CustomBodyType.BLANKET.value,
        CustomBodyType.SKINDETAIL_HOOF_COLOR.value, CustomBodyType.HAIR_MANE.value, CustomBodyType.HAIR_TAIL.value, CustomBodyType.HAIR_FORELOCK.value,
        CustomBodyType.HAIR_FEATHERS.value, CustomBodyType.HORN.value, CustomBodyType.TAIL_BASE.value,
    ]
    SIM_GARMENT = [
        CustomBodyType.HAT.value, CustomBodyType.FULL_BODY.value, CustomBodyType.UPPER_BODY.value, CustomBodyType.LOWER_BODY.value,
        CustomBodyType.SHOES.value, CustomBodyType.CUMMERBUND.value, CustomBodyType.GLOVES.value, CustomBodyType.SOCKS.value, CustomBodyType.TIGHTS.value,
        CustomBodyType.ATTACHMENT_BACK.value,
    ]
    SIM_HEAD_DETAILS = [
        CustomBodyType.HEAD.value, CustomBodyType.TEETH.value,
        CustomBodyType.EYECOLOR.value, CustomBodyType.EYECOLOR_SECONDARY.value,
        CustomBodyType.SKINDETAIL_NOSE_COLOR.value,
    ]
    SIM_HEAD_HAIR = [
        CustomBodyType.HAIR.value, CustomBodyType.HAIRCOLOR_OVERRIDE.value, CustomBodyType.FACIAL_HAIR.value,
    ]
    SIM_HEAD = SIM_HEAD_DETAILS + SIM_HEAD_HAIR
    SIM_HEAD_PAINT = [
        CustomBodyType.LIPS_TICK.value, CustomBodyType.EYE_SHADOW.value, CustomBodyType.EYE_LINER.value, CustomBodyType.BLUSH.value,
        CustomBodyType.FACEPAINT.value, CustomBodyType.EYEBROWS.value, CustomBodyType.EYELASHES.value,
    ]

    SIM_PIERCING = [
        CustomBodyType.LIP_RING_LEFT.value, CustomBodyType.LIP_RING_RIGHT.value, CustomBodyType.NOSE_RING_LEFT.value, CustomBodyType.NOSE_RING_RIGHT.value,
        CustomBodyType.BROW_RING_LEFT.value, CustomBodyType.BROW_RING_RIGHT.value,
    ]
    SIM_HEAD_JEWELRY = [
        CustomBodyType.EARRINGS.value, CustomBodyType.GLASSES.value, CustomBodyType.NECKLACE.value,
    ]
    SIM_HAND_JEWELRY = [
        CustomBodyType.WRIST_LEFT.value, CustomBodyType.WRIST_RIGHT.value, CustomBodyType.INDEX_FINGER_LEFT.value, CustomBodyType.INDEX_FINGER_RIGHT.value,
        CustomBodyType.RING_FINGER_LEFT.value, CustomBodyType.RING_FINGER_RIGHT.value, CustomBodyType.MIDDLE_FINGER_LEFT.value, CustomBodyType.MIDDLE_FINGER_RIGHT
    ]
    SIM_ALL_JEWELRY = SIM_HEAD_JEWELRY + SIM_HAND_JEWELRY + SIM_PIERCING

    SIM_BODY_HAIR = [
        CustomBodyType.BODYHAIR_ARM.value, CustomBodyType.BODYHAIR_TORSOFRONT.value,
        CustomBodyType.BODYHAIR_LEG.value, CustomBodyType.BODYHAIR_TORSOBACK.value,
    ]
    SIM_SKIN_OVERLAY = [
        CustomBodyType.SKIN_OVERLAY.value,
    ]
    SIM_SKIN = SIM_SKIN_OVERLAY + SIM_BODY_HAIR

    SIM_TATTOO = [
        CustomBodyType.TATTOO_ARM_LOWER_LEFT.value, CustomBodyType.TATTOO_ARM_UPPER_LEFT.value,
        CustomBodyType.TATTOO_ARM_LOWER_RIGHT.value, CustomBodyType.TATTOO_ARM_UPPER_RIGHT.value,
        CustomBodyType.TATTOO_LEG_LEFT.value, CustomBodyType.TATTOO_LEG_RIGHT.value,
        CustomBodyType.TATTOO_TORSO_BACK_LOWER.value, CustomBodyType.TATTOO_TORSO_BACK_UPPER.value,
        CustomBodyType.TATTOO_TORSO_FRONT_LOWER.value, CustomBodyType.TATTOO_TORSO_FRONT_UPPER.value,
    ]

    SIM_NAIL_COLOR = [
        CustomBodyType.FINGERNAIL.value, CustomBodyType.TOENAIL.value,
    ]
    SIM_ALL_BODY_PAINT = SIM_TATTOO + SIM_NAIL_COLOR

    SIM_OCCULTS = [
        CustomBodyType.OCCULT_BROW.value, CustomBodyType.OCCULT_EYE_SOCKET.value, CustomBodyType.OCCULT_EYE_LID.value, CustomBodyType.OCCULT_MOUTH.value,
        CustomBodyType.OCCULT_LEFT_CHEEK.value, CustomBodyType.OCCULT_RIGHT_CHEEK.value, CustomBodyType.OCCULT_NECK_SCAR.value,
    ]
    SIM_SCARS = [
        CustomBodyType.FOREARM_SCAR.value,
        CustomBodyType.BODYSCAR_ARMLEFT.value, CustomBodyType.BODYSCAR_TORSOFRONTvalue, CustomBodyType.BODYSCAR_LEGLEFT.value,
        CustomBodyType.BODYSCAR_ARMRIGHT.value, CustomBodyType.BODYSCAR_TORSOBACK.value, CustomBodyType.BODYSCAR_LEGRIGHT.value,
    ]
    SIM_ALL_OCCULT_SCARS = SIM_OCCULTS + SIM_SCARS

    SIM_OTHER = [
        CustomBodyType.ACNE.value, CustomBodyType.SKINDETAIL_ACNE_PUBERTY.value, CustomBodyType.SKINDETAIL_FRECKLES.value, CustomBodyType.BODYFRECKLES.value,
        CustomBodyType.SKINDETAIL_DIMPLE_LEFT.value, CustomBodyType.SKINDETAIL_DIMPLE_RIGHT.value,
        CustomBodyType.BITE.value, CustomBodyType.SCARFACE.value,
    ]

    SIM_MOLE_CREASE = [
        CustomBodyType.SKINDETAIL_MOLE_LIP_LEFT.value, CustomBodyType.SKINDETAIL_MOLE_LIP_RIGHT.value, CustomBodyType.SKINDETAIL_MOLE_CHEEK_LEFT.value, CustomBodyType.SKINDETAIL_MOLE_CHEEK_RIGHT.value,
        CustomBodyType.SKINDETAIL_CREASE_MOUTH.value, CustomBodyType.SKINDETAIL_CREASE_FOREHEAD.value,
        CustomBodyType.MOLEFACE.value, CustomBodyType.MOLECHESTUPPER.value, CustomBodyType.MOLEBACKUPPER.value,
    ]
    SIM_MARKS = [
        CustomBodyType.BIRTHMARKFACE.value,
        CustomBodyType.BIRTHMARKTORSOFRONT.value, CustomBodyType.BIRTHMARKTORSOBACK.value,
        CustomBodyType.STRETCHMARKS_FRONT.value, CustomBodyType.STRETCHMARKS_BACK.value,
        CustomBodyType.BIRTHMARKARMS.value, CustomBodyType.BIRTHMARKLEGS.value,
    ]

    SIM_ALL = SIM_HEAD + SIM_HEAD_HAIR + SIM_BODY_HAIR + SIM_GARMENT + \
        SIM_PIERCING + SIM_HEAD_JEWELRY + SIM_HAND_JEWELRY + SIM_HEAD_PAINT + \
        SIM_TATTOO + SIM_SKIN + SIM_NAIL_COLOR + \
        SIM_OCCULTS + SIM_SCARS + \
        SIM_OTHER + SIM_MOLE_CREASE + SIM_MARKS

    EVERYTHING = None  # we use this instead of a very long list.
    # EVERYTHING = [e.value for e in CustomBodyType]
    # EVERYTHING = SIM_ALL + PET_ALL + HORSE_ALL

    # Order as in PieMenuActionIds
    # None | Sim | Body Paint | Cloth | Hand Accessories | Head Accessories | Head Paint | Head Piercings | Occult Scars | Pet |
    r'''
    parts = [
        EVERYTHING,
        SIM_ALL,
        SIM_GARMENT, SIM_JEWELRY, SIM_HAND_ACCESSORIES, SIM_HEAD_PAINT, SIM_BODY_PAINT, SIM_PIERCING, SIM_OCCULTS_SCARS, PET, HORSE
    ]
    '''

    outfit_categories = dict({
        0: 'Everyday',
        1: 'Formal',
        2: 'Athletic',
        3: 'Sleep',
        4: 'Party',
        5: 'Bathing',
        6: 'Career',
        7: 'Situation',
        8: 'Special',
        9: 'Swimwear',
        10: 'Hot Weather',
        11: 'Cold Weather',
        12: 'Batuu',
    })
