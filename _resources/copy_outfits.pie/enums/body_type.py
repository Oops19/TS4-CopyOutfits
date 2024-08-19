#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class BodyType(CommonEnum):
    NONE = 0
    HAT = 1
    HAIR = 2
    HEAD = 3
    TEETH = 4
    FULL_BODY = 5
    UPPER_BODY = 6
    LOWER_BODY = 7
    SHOES = 8
    CUMMERBUND = 9
    EARRINGS = 10
    GLASSES = 11
    NECKLACE = 12
    GLOVES = 13
    WRIST_LEFT = 14
    WRIST_RIGHT = 15
    LIP_RING_LEFT = 16
    LIP_RING_RIGHT = 17
    NOSE_RING_LEFT = 18
    NOSE_RING_RIGHT = 19
    BROW_RING_LEFT = 20
    BROW_RING_RIGHT = 21
    INDEX_FINGER_LEFT = 22
    INDEX_FINGER_RIGHT = 23
    RING_FINGER_LEFT = 24
    RING_FINGER_RIGHT = 25
    MIDDLE_FINGER_LEFT = 26
    MIDDLE_FINGER_RIGHT = 27
    FACIAL_HAIR = 28
    LIPS_TICK = 29
    EYE_SHADOW = 30
    EYE_LINER = 31
    BLUSH = 32
    FACEPAINT = 33
    EYEBROWS = 34
    EYECOLOR = 35
    SOCKS = 36
    MASCARA = 37
    SKINDETAIL_CREASE_FOREHEAD = 38
    SKINDETAIL_FRECKLES = 39
    SKINDETAIL_DIMPLE_LEFT = 40
    SKINDETAIL_DIMPLE_RIGHT = 41
    TIGHTS = 42
    SKINDETAIL_MOLE_LIP_LEFT = 43
    SKINDETAIL_MOLE_LIP_RIGHT = 44
    TATTOO_ARM_LOWER_LEFT = 45
    TATTOO_ARM_UPPER_LEFT = 46
    TATTOO_ARM_LOWER_RIGHT = 47
    TATTOO_ARM_UPPER_RIGHT = 48
    TATTOO_LEG_LEFT = 49
    TATTOO_LEG_RIGHT = 50
    TATTOO_TORSO_BACK_LOWER = 51
    TATTOO_TORSO_BACK_UPPER = 52
    TATTOO_TORSO_FRONT_LOWER = 53
    TATTOO_TORSO_FRONT_UPPER = 54
    SKINDETAIL_MOLE_CHEEK_LEFT = 55
    SKINDETAIL_MOLE_CHEEK_RIGHT = 56
    SKINDETAIL_CREASE_MOUTH = 57
    SKIN_OVERLAY = 58
    FUR_BODY = 59
    EARS = 60
    TAIL = 61
    SKINDETAIL_NOSE_COLOR = 62
    EYECOLOR_SECONDARY = 63
    OCCULT_BROW = 64
    OCCULT_EYE_SOCKET = 65
    OCCULT_EYE_LID = 66
    OCCULT_MOUTH = 67
    OCCULT_LEFT_CHEEK = 68
    OCCULT_RIGHT_CHEEK = 69
    OCCULT_NECK_SCAR = 70
    FOREARM_SCAR = 71
    ACNE = 72
    FINGERNAIL = 73
    TOENAIL = 74
    HAIRCOLOR_OVERRIDE = 75
    BITE = 76
    BODYFRECKLES = 77
    BODYHAIR_ARM = 78
    BODYHAIR_LEG = 79
    BODYHAIR_TORSOFRONT = 80
    BODYHAIR_TORSOBACK = 81
    BODYSCAR_ARMLEFT = 82
    BODYSCAR_ARMRIGHT = 83
    BODYSCAR_TORSOFRONT = 84
    BODYSCAR_TORSOBACK = 85
    BODYSCAR_LEGLEFT = 86
    BODYSCAR_LEGRIGHT = 87
    ATTACHMENT_BACK = 88
    SKINDETAIL_ACNE_PUBERTY = 89
    SCARFACE = 90
    BIRTHMARKFACE = 91
    BIRTHMARKTORSOBACK = 92
    BIRTHMARKTORSOFRONT = 93
    BIRTHMARKARMS = 94
    MOLEFACE = 95
    MOLECHESTUPPER = 96
    MOLEBACKUPPER = 97
    BIRTHMARKLEGS = 98
    STRETCHMARKS_FRONT = 99
    STRETCHMARKS_BACK = 100
    SADDLE = 101
    BRIDLE = 102
    REINS = 103
    BLANKET = 104
    SKINDETAIL_HOOF_COLOR = 105
    HAIR_MANE = 106
    HAIR_TAIL = 107
    HAIR_FORELOCK = 108
    HAIR_FEATHERS = 109
    HORN = 110
    TAIL_BASE = 111

    @classmethod
    def _missing_(cls, key_value):
        """
        Return a default or a random enum value.
        @param key_value: Can either be the value `Enum(value)` (usually int; str or float) or the key `Enum.KEY ==> KEY` (usually str).
        """
        if isinstance(key_value, str):
            try:
                from sims.outfits.outfit_enums import BodyType
                return getattr(BodyType, key_value)
            except:
                pass
        return cls.NONE
