#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.body_part import BodyPart
from ts4lib.utils.singleton import Singleton


class OutfitGroups(object, metaclass=Singleton):

    body_paint = [
        BodyPart.TATTOO_ARM_LOWER_LEFT.value, BodyPart.TATTOO_ARM_UPPER_LEFT.value,
        BodyPart.TATTOO_ARM_LOWER_RIGHT.value, BodyPart.TATTOO_ARM_UPPER_RIGHT.value,
        BodyPart.TATTOO_LEG_LEFT.value, BodyPart.TATTOO_LEG_RIGHT.value,
        BodyPart.TATTOO_TORSO_BACK_LOWER.value, BodyPart.TATTOO_TORSO_BACK_UPPER.value,
        BodyPart.TATTOO_TORSO_FRONT_LOWER.value, BodyPart.TATTOO_TORSO_FRONT_UPPER.value,
        BodyPart.SKIN_OVERLAY.value,
        BodyPart.FINGERNAIL.value, BodyPart.TOENAIL.value,
    ]

    cloth = [
        BodyPart.HAT.value, BodyPart.FULL_BODY.value, BodyPart.UPPER_BODY.value, BodyPart.LOWER_BODY.value,
        BodyPart.SHOES.value, BodyPart.CUMMERBUND.value, BodyPart.GLOVES.value, BodyPart.SOCKS.value, BodyPart.TIGHTS.value,
        BodyPart.ATTACHMENT_BACK.value,
    ]

    hand_accessories = [
        BodyPart.WRIST_LEFT.value, BodyPart.WRIST_RIGHT.value, BodyPart.INDEX_FINGER_LEFT.value, BodyPart.INDEX_FINGER_RIGHT.value,
        BodyPart.RING_FINGER_LEFT.value, BodyPart.RING_FINGER_RIGHT.value, BodyPart.MIDDLE_FINGER_LEFT.value, BodyPart.MIDDLE_FINGER_RIGHT
    ]

    head_accessories = [
        BodyPart.EARRINGS.value, BodyPart.GLASSES.value, BodyPart.NECKLACE.value,
    ]

    head_paint = [
        BodyPart.LIPS_TICK.value, BodyPart.EYE_SHADOW.value, BodyPart.EYE_LINER.value, BodyPart.BLUSH.value,
        BodyPart.FACEPAINT.value, BodyPart.EYEBROWS.value, BodyPart.MASCARA.value,
    ]

    head_piercings = [
        BodyPart.LIP_RING_LEFT.value, BodyPart.LIP_RING_RIGHT.value, BodyPart.NOSE_RING_LEFT.value, BodyPart.NOSE_RING_RIGHT.value,
        BodyPart.BROW_RING_LEFT.value, BodyPart.BROW_RING_RIGHT.value,
    ]

    occult_scars = [
        BodyPart.OCCULT_BROW.value, BodyPart.OCCULT_EYE_SOCKET.value, BodyPart.OCCULT_EYE_LID.value, BodyPart.OCCULT_MOUTH.value,
        BodyPart.OCCULT_LEFT_CHEEK.value, BodyPart.OCCULT_RIGHT_CHEEK.value, BodyPart.OCCULT_NECK_SCAR.value, BodyPart.FOREARM_SCAR.value,
    ]

    pet = [
        BodyPart.FUR_BODY.value, BodyPart.EARS.value, BodyPart.TAIL.value,
    ]

    sim = [
        BodyPart.HEAD.value, BodyPart.TEETH.value,
        BodyPart.HAIR.value, BodyPart.HAIRCOLOR_OVERRIDE.value, BodyPart.FACIAL_HAIR.value, BodyPart.EYECOLOR.value,
        BodyPart.SKINDETAIL_CREASE_FOREHEAD.value, BodyPart.SKINDETAIL_FRECKLES.value, BodyPart.SKINDETAIL_DIMPLE_LEFT.value,
        BodyPart.SKINDETAIL_DIMPLE_RIGHT.value, BodyPart.SKINDETAIL_MOLE_LIP_LEFT.value, BodyPart.SKINDETAIL_MOLE_LIP_RIGHT.value,
        BodyPart.SKINDETAIL_MOLE_CHEEK_LEFT.value, BodyPart.SKINDETAIL_MOLE_CHEEK_RIGHT.value, BodyPart.SKINDETAIL_CREASE_MOUTH.value,
        BodyPart.MOLEFACE.value, BodyPart.MOLECHESTUPPER.value, BodyPart.MOLEBACKUPPER.value,
        BodyPart.BIRTHMARKFACE.value, BodyPart.BIRTHMARKTORSOBACK.value, BodyPart.BIRTHMARKTORSOFRONT.value, BodyPart.BIRTHMARKARMS.value, BodyPart.BIRTHMARKLEGS.value,
        BodyPart.STRETCHMARKS_FRONT.value, BodyPart.STRETCHMARKS_BACK.value,
        BodyPart.SKINDETAIL_NOSE_COLOR.value, BodyPart.EYECOLOR_SECONDARY.value,
        BodyPart.BODYFRECKLES.value, BodyPart.SKINDETAIL_ACNE_PUBERTY.value, BodyPart.ACNE.value,
        BodyPart.BODYHAIR_LEG.value, BodyPart.BODYHAIR_TORSOFRONT.value, BodyPart.BODYHAIR_TORSOBACK.value,  BodyPart.BODYHAIR_ARM.value, BodyPart.BODYSCAR_ARMLEFT.value, BodyPart.BODYSCAR_ARMRIGHT.value,
        BodyPart.SCARFACE.value, BodyPart.BITE.value, BodyPart.BODYSCAR_TORSOFRONT.value, BodyPart.BODYSCAR_TORSOBACK.value, BodyPart.BODYSCAR_LEGLEFT.value, BodyPart.BODYSCAR_LEGRIGHT.value,
    ]

    # Order as in PieMenuActionIds
    # None | All | Body Paint | Cloth | Hand Accessories | Head Accessories | Head Paint | Head Piercings | Occult Scars | Pet | Sim
    parts = [
        None,
        body_paint + cloth + hand_accessories + head_accessories + head_paint + head_piercings + occult_scars + pet + sim,
        body_paint, cloth, hand_accessories, head_accessories, head_paint, head_piercings, occult_scars, pet, sim
    ]

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
