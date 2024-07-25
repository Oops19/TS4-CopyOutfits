#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.body_type import BodyType
from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class OutfitGroups(CommonEnum):

    PET_ALL = [
        BodyType.FUR_BODY.value, BodyType.EARS.value, BodyType.TAIL.value,
    ]

    HORSE_ALL = [
        BodyType.SADDLE.value, BodyType.BRIDLE.value, BodyType.REINS.value, BodyType.BLANKET.value,
        BodyType.SKINDETAIL_HOOF_COLOR.value, BodyType.HAIR_MANE.value, BodyType.HAIR_TAIL.value, BodyType.HAIR_FORELOCK.value,
        BodyType.HAIR_FEATHERS.value, BodyType.HORN.value, BodyType.TAIL_BASE.value,
    ]
    SIM_GARMENT = [
        BodyType.HAT.value, BodyType.FULL_BODY.value, BodyType.UPPER_BODY.value, BodyType.LOWER_BODY.value,
        BodyType.SHOES.value, BodyType.CUMMERBUND.value, BodyType.GLOVES.value, BodyType.SOCKS.value, BodyType.TIGHTS.value,
        BodyType.ATTACHMENT_BACK.value,
    ]
    SIM_HEAD_DETAILS = [
        BodyType.HEAD.value, BodyType.TEETH.value,
        BodyType.EYECOLOR.value, BodyType.EYECOLOR_SECONDARY.value,
        BodyType.SKINDETAIL_NOSE_COLOR.value,
    ]
    SIM_HEAD_HAIR = [
        BodyType.HAIR.value, BodyType.HAIRCOLOR_OVERRIDE.value, BodyType.FACIAL_HAIR.value,
    ]
    SIM_HEAD = SIM_HEAD_DETAILS + SIM_HEAD_HAIR
    SIM_HEAD_PAINT = [
        BodyType.LIPS_TICK.value, BodyType.EYE_SHADOW.value, BodyType.EYE_LINER.value, BodyType.BLUSH.value,
        BodyType.FACEPAINT.value, BodyType.EYEBROWS.value, BodyType.EYELASHES.value,
    ]

    SIM_PIERCING = [
        BodyType.LIP_RING_LEFT.value, BodyType.LIP_RING_RIGHT.value, BodyType.NOSE_RING_LEFT.value, BodyType.NOSE_RING_RIGHT.value,
        BodyType.BROW_RING_LEFT.value, BodyType.BROW_RING_RIGHT.value,
    ]
    SIM_HEAD_JEWELRY = [
        BodyType.EARRINGS.value, BodyType.GLASSES.value, BodyType.NECKLACE.value,
    ]
    SIM_HAND_JEWELRY = [
        BodyType.WRIST_LEFT.value, BodyType.WRIST_RIGHT.value, BodyType.INDEX_FINGER_LEFT.value, BodyType.INDEX_FINGER_RIGHT.value,
        BodyType.RING_FINGER_LEFT.value, BodyType.RING_FINGER_RIGHT.value, BodyType.MIDDLE_FINGER_LEFT.value, BodyType.MIDDLE_FINGER_RIGHT
    ]
    SIM_ALL_JEWELRY = SIM_HEAD_JEWELRY + SIM_HAND_JEWELRY + SIM_PIERCING

    SIM_BODY_HAIR = [
        BodyType.BODYHAIR_ARM.value, BodyType.BODYHAIR_TORSOFRONT.value,
        BodyType.BODYHAIR_LEG.value, BodyType.BODYHAIR_TORSOBACK.value,
    ]
    SIM_SKIN_OVERLAY = [
        BodyType.SKIN_OVERLAY.value,
    ]
    SIM_SKIN = SIM_SKIN_OVERLAY + SIM_BODY_HAIR

    SIM_TATTOO = [
        BodyType.TATTOO_ARM_LOWER_LEFT.value, BodyType.TATTOO_ARM_UPPER_LEFT.value,
        BodyType.TATTOO_ARM_LOWER_RIGHT.value, BodyType.TATTOO_ARM_UPPER_RIGHT.value,
        BodyType.TATTOO_LEG_LEFT.value, BodyType.TATTOO_LEG_RIGHT.value,
        BodyType.TATTOO_TORSO_BACK_LOWER.value, BodyType.TATTOO_TORSO_BACK_UPPER.value,
        BodyType.TATTOO_TORSO_FRONT_LOWER.value, BodyType.TATTOO_TORSO_FRONT_UPPER.value,
    ]

    SIM_NAIL_COLOR = [
        BodyType.FINGERNAIL.value, BodyType.TOENAIL.value,
    ]
    SIM_ALL_BODY_PAINT = SIM_TATTOO + SIM_NAIL_COLOR

    SIM_OCCULTS = [
        BodyType.OCCULT_BROW.value, BodyType.OCCULT_EYE_SOCKET.value, BodyType.OCCULT_EYE_LID.value, BodyType.OCCULT_MOUTH.value,
        BodyType.OCCULT_LEFT_CHEEK.value, BodyType.OCCULT_RIGHT_CHEEK.value, BodyType.OCCULT_NECK_SCAR.value,
    ]
    SIM_SCARS = [
        BodyType.FOREARM_SCAR.value,
        BodyType.BODYSCAR_ARMLEFT.value, BodyType.BODYSCAR_TORSOFRONTvalue, BodyType.BODYSCAR_LEGLEFT.value,
        BodyType.BODYSCAR_ARMRIGHT.value, BodyType.BODYSCAR_TORSOBACK.value, BodyType.BODYSCAR_LEGRIGHT.value,
    ]
    SIM_ALL_OCCULT_SCARS = SIM_OCCULTS + SIM_SCARS

    SIM_OTHER = [
        BodyType.ACNE.value, BodyType.SKINDETAIL_ACNE_PUBERTY.value, BodyType.SKINDETAIL_FRECKLES.value, BodyType.BODYFRECKLES.value,
        BodyType.SKINDETAIL_DIMPLE_LEFT.value, BodyType.SKINDETAIL_DIMPLE_RIGHT.value,
        BodyType.BITE.value, BodyType.SCARFACE.value,
    ]

    SIM_MOLE_CREASE = [
        BodyType.SKINDETAIL_MOLE_LIP_LEFT.value, BodyType.SKINDETAIL_MOLE_LIP_RIGHT.value, BodyType.SKINDETAIL_MOLE_CHEEK_LEFT.value, BodyType.SKINDETAIL_MOLE_CHEEK_RIGHT.value,
        BodyType.SKINDETAIL_CREASE_MOUTH.value, BodyType.SKINDETAIL_CREASE_FOREHEAD.value,
        BodyType.MOLEFACE.value, BodyType.MOLECHESTUPPER.value, BodyType.MOLEBACKUPPER.value,
    ]
    SIM_MARKS = [
        BodyType.BIRTHMARKFACE.value,
        BodyType.BIRTHMARKTORSOFRONT.value, BodyType.BIRTHMARKTORSOBACK.value,
        BodyType.STRETCHMARKS_FRONT.value, BodyType.STRETCHMARKS_BACK.value,
        BodyType.BIRTHMARKARMS.value, BodyType.BIRTHMARKLEGS.value,
    ]

    SIM_ALL = SIM_HEAD + SIM_HEAD_HAIR + SIM_BODY_HAIR + SIM_GARMENT + \
        SIM_PIERCING + SIM_HEAD_JEWELRY + SIM_HAND_JEWELRY + SIM_HEAD_PAINT + \
        SIM_TATTOO + SIM_SKIN + SIM_NAIL_COLOR + \
        SIM_OCCULTS + SIM_SCARS + \
        SIM_OTHER + SIM_MOLE_CREASE + SIM_MARKS

    EVERYTHING = None  # we use this instead of a very long list.
    # EVERYTHING = [e.value for e in BodyType]
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
