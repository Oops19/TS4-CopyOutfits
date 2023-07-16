#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims.outfits.outfit_enums import BodyType
from ts4lib.utils.singleton import Singleton


class XXXOutfitGroups(object, metaclass=Singleton):

    body_paint = [
        BodyType.TATTOO_ARM_LOWER_LEFT, BodyType.TATTOO_ARM_UPPER_LEFT,
        BodyType.TATTOO_ARM_LOWER_RIGHT, BodyType.TATTOO_ARM_UPPER_RIGHT, BodyType.TATTOO_LEG_LEFT, BodyType.TATTOO_LEG_RIGHT,
        BodyType.TATTOO_TORSO_BACK_LOWER, BodyType.TATTOO_TORSO_BACK_UPPER, BodyType.TATTOO_TORSO_FRONT_LOWER, BodyType.TATTOO_TORSO_FRONT_UPPER,
        BodyType.SKIN_OVERLAY,
        BodyType.ACNE, BodyType.FINGERNAIL, BodyType.TOENAIL,
    ]

    cloth = [
        BodyType.HAT, BodyType.FULL_BODY, BodyType.UPPER_BODY, BodyType.LOWER_BODY,
        BodyType.SHOES, BodyType.CUMMERBUND, BodyType.GLOVES, BodyType.SOCKS, BodyType.TIGHTS,
    ]

    hand_accessories = [
        BodyType.WRIST_LEFT, BodyType.WRIST_RIGHT, BodyType.INDEX_FINGER_LEFT, BodyType.INDEX_FINGER_RIGHT,
        BodyType.RING_FINGER_LEFT, BodyType.RING_FINGER_RIGHT, BodyType.MIDDLE_FINGER_LEFT, BodyType.MIDDLE_FINGER_RIGHT
    ]

    head_accessories = [
        BodyType.EARRINGS, BodyType.GLASSES, BodyType.NECKLACE
    ]

    head_paint = [
        BodyType.LIPS_TICK, BodyType.EYE_SHADOW, BodyType.EYE_LINER, BodyType.BLUSH,
        BodyType.FACEPAINT, BodyType.EYEBROWS, BodyType.MASCARA
    ]

    head_piercings = [
        BodyType.LIP_RING_LEFT, BodyType.LIP_RING_RIGHT, BodyType.NOSE_RING_LEFT, BodyType.NOSE_RING_RIGHT,
        BodyType.BROW_RING_LEFT, BodyType.BROW_RING_RIGHT
    ]

    occult_scars = [
        BodyType.OCCULT_BROW, BodyType.OCCULT_EYE_SOCKET, BodyType.OCCULT_EYE_LID, BodyType.OCCULT_MOUTH,
        BodyType.OCCULT_LEFT_CHEEK, BodyType.OCCULT_RIGHT_CHEEK, BodyType.OCCULT_NECK_SCAR, BodyType.FOREARM_SCAR,
    ]

    pet = [
        BodyType.FUR_BODY, BodyType.EARS, BodyType.TAIL,
    ]
    sim = [
        BodyType.HEAD, BodyType.TEETH,
        BodyType.HAIR, BodyType.FACIAL_HAIR, BodyType.EYECOLOR,
        BodyType.SKINDETAIL_CREASE_FOREHEAD, BodyType.SKINDETAIL_FRECKLES, BodyType.SKINDETAIL_DIMPLE_LEFT,
        BodyType.SKINDETAIL_DIMPLE_RIGHT, BodyType.SKINDETAIL_MOLE_LIP_LEFT, BodyType.SKINDETAIL_MOLE_LIP_RIGHT,
        BodyType.SKINDETAIL_MOLE_CHEEK_LEFT, BodyType.SKINDETAIL_MOLE_CHEEK_RIGHT, BodyType.SKINDETAIL_CREASE_MOUTH,
        BodyType.SKINDETAIL_NOSE_COLOR, BodyType.EYECOLOR_SECONDARY,
    ]

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

