#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Tuple

from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.utils.common_type_utils import CommonTypeUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class RegisterCopyOutfitsInteractions(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xEC810595D17D6FBF,  # 'Copy' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits_PMA_Copy_debug')
            0x5020FF18FDB9BAC9,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy_PMA_Picker_debug')
            0x04346C61AD16A86B,  # 'X-Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy_PMA_Xx2DPicker_debug')
            0xCF47514BC12BF930,  # 'Everyday' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Everyday_debug')
            0x821AF14A79863FD0,  # 'Formal' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Formal_debug')
            0xE381D40CCD6B1AC1,  # 'Athletic' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Athletic_debug')
            0x6A47AE12568BBCF2,  # 'Sleep' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Sleep_debug')
            0xD73CB33C30AA172F,  # 'Party' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Party_debug')
            0xA26243B934ABA1E8,  # 'Swimwear' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Swimwear_debug')
            0x4285E2BDB177DBD6,  # 'Hotweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Hotweather_debug')
            0x96EE25889AED629D,  # 'Coldweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Coldweather_debug')
            0x4C50742DB10555A0,  # 'Bathing' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Bathing_debug')
            0x65C307D86C4BEBC1,  # 'Career' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Career_debug')
            0x4780D187691D2F25,  # 'Situation' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Situation_debug')
            0x7F0B7F986F291F18,  # 'Special' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Special_debug')
            0x4614B28FC3E66C6E,  # 'Batuu' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Batuu_debug')
            0xC019EBEC5D9E59F9,  # 'All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_All_debug')
            0x42C13C56219110CE,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_1_debug')
            0xC84962394FC118B9,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_2_debug')
            0x6656A1AB9A347ED8,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_3_debug')
            0x6924714F189D108B,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_4_debug')
            0x963363849E50ACAD,  # 'Paste' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits_PMA_Paste_debug')
            0xB4BD9EC859F87DA7,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste_PMA_Picker_debug')
            0xB93D2007E430410D,  # 'X-Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste_PMA_Xx2DPicker_debug')
            0xBE47A3DB04992FDA,  # 'Everyday' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Everyday_debug')
            0x4800548834695F56,  # 'Formal' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Formal_debug')
            0xE4AA0531416EFCBF,  # 'Athletic' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Athletic_debug')
            0xBFBE95D88A17E3A4,  # 'Sleep' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Sleep_debug')
            0x82FE1EE02BF2A491,  # 'Party' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Party_debug')
            0x379E5BA0737A1502,  # 'Swimwear' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Swimwear_debug')
            0x95E30B80F1161FC4,  # 'Hotweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Hotweather_debug')
            0xFE3B50A478096753,  # 'Coldweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Coldweather_debug')
            0xBA2466DEED56CBCE,  # 'Bathing' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Bathing_debug')
            0x579386424F75D94B,  # 'Career' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Career_debug')
            0xFC1901CC0002F6AB,  # 'Situation' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Situation_debug')
            0x4BAFF91287481312,  # 'Special' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Special_debug')
            0x38592B87D566B97C,  # 'Batuu' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Batuu_debug')
            0xAF35179A2DB6103C,  # 'All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_All_debug')
            0x309EEC0739EF76B7,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_1_debug')
            0x82FE19747EA17CF0,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_2_debug')
            0x1217A48330E02C31,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_3_debug')
            0x95ACA9C274BBC102,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_4_debug')
            0xA0438F9BE5A2A614,  # 'Everything' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone_PMA_Everything_debug')
            0x4CCDCD923E9DA9F8,  # 'All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_All_debug')
            0x9E44D5D52AEB749D,  # 'Head' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Head_debug')
            0x1201B32E3A191D97,  # 'Garment' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Garment_debug')
            0x6BCABFB72E68DF61,  # 'Piercings' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Piercings_debug')
            0x076196EA2CE19846,  # 'Head Jewelry' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Head_Jewelry_debug')
            0xAFB2CF759C5307D3,  # 'Hand Jewelry' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Hand_Jewelry_debug')
            0x058901BBB11BD8EC,  # 'Head Paint' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Head_Paint_debug')
            0xC7496B975856B51C,  # 'Skin' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Skin_debug')
            0x63764BC0A7620AD0,  # 'Tattoo' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Tattoo_debug')
            0xA2C4A317CB79598B,  # 'Nail Color' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Nail_Color_debug')
            0xD186C3EC5001EF04,  # 'Occults' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Occults_debug')
            0xC2D27A7416DD5CCF,  # 'Scars' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Scars_debug')
            0xBB776F98C3D8E2AF,  # 'Other' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Other_debug')
            0xB16B223619B7822F,  # 'Mole / Crease' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Mole____Crease_debug')
            0xF7DC4D1F3FA35033,  # 'Marks' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Marks_debug')
            0x98B635E72E0CE552,  # 'Pet' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Pet_debug')
            0x98B1FD955FB783AA,  # 'Horse' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Horse_debug')
            0x3DD45204918CAD41,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__CAS_Parts_PMA_Picker_debug')
            0x4CB31771C54A3CD6,  # 'All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_All_debug')
            0x7D805E13757D4EE1,  # 'Age & Gender' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Age_x26_Gender_debug')
            0x841D5D5D78952AD1,  # 'Genetics' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Genetics_debug')
            0x70CC43F38C0C22F8,  # 'Physics & Genetics' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Physics_x26_Genetics_debug')
            0x800D569C583E7411,  # 'Sliders' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Sliders_debug')
            0xC91B2D4775F5D9E1,  # 'Walkstyle' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Walkstyle_debug')
            0xBF2D7E22B63835C6,  # 'Traits' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Traits_debug')
            0x5B781745009E62F7,  # 'Skills' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Skills_debug')
            0x92C181081028082A,  # 'Skintone' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Clone__Characteristics_PMA_Skintone_debug')
            0x963617A59101AEC4,  # 'Same Skin' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Skins_PMA_Same_Skin_debug')
            0x1528B333133341B7,  # 'Next Skin' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Skins_PMA_Next_Skin_debug')
            0x8DF8F6C0972C3C5F,  # 'Previous Skin' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Skins_PMA_Previous_Skin_debug')
            0x11E56FC28ACBD921,  # 'Random Skin' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Skins_PMA_Random_Skin_debug')

            0xA4C3FF059DBFBC58,  # 'Adult Female' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Adult_Female_debug')
            0xB6F3DD7382AEEF83,  # 'Adult Male' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Adult_Male_debug')
            0xC24D189F4EFFF3A2,  # 'Child Female' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Child_Female_debug')
            0x4C7BC30EF1D3B919,  # 'Child Male' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Child_Male_debug')
            0x685CD5634DA17B31,  # 'Zero' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Rotate_PMA_Zero_debug')
            0xBDF3E3D99B0E2FF0,  # 'Left' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Rotate_PMA_Left_debug')
            0x06C075ADACF829B3,  # 'Right' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Rotate_PMA_Right_debug')
            0xC11F89ED9D7FF93A,  # 'Destroy' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Remove_PMA_Destroy_debug')

            0x4B864F684F7FC787,  # 'Print Clipboard' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More_PMA_Print_Clipboard_debug')
            0x5BA6F113C0F2661A,  # 'Clear All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More_PMA_Clear_All_debug')
            0xA88C83FEBA17597D,  # 'Clipboard 0' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_0_debug')
            0x71BE7E2EB047630C,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_1_debug')
            0x470F4F06757F1343,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_2_debug')
            0xAD750FAC05321AA2,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_3_debug')
            0x29E00A6CC15685D1,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_4_debug')
            0x7FA94A6F76A52A88,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits_PMA_Picker_debug')
            0xCC635FE722234B0E,  # 'X-Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits_PMA_Xx2DPicker_debug')
            0x63DA2C923BDD4D19,  # 'Everyday' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Everyday_debug')
            0x429729349BDA2EE5,  # 'Formal' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Formal_debug')
            0x793C9BA5044FF08C,  # 'Athletic' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Athletic_debug')
            0x8612D3F191ACA4AD,  # 'Sleep' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Sleep_debug')
            0xFC4E473669D9D5A0,  # 'Party' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Party_debug')
            0xB54C16F984C43719,  # 'Swimwear' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Swimwear_debug')
            0x1CC166EFB9A71E2F,  # 'Hotweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Hotweather_debug')
            0x20ABC6FE1E9E68A6,  # 'Coldweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Category_PMA_Coldweather_debug')
            0x99A887A11A57BB0F,  # 'Bathing' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Xx2DCategory_PMA_Bathing_debug')
            0xA0DFE4F7E793BB28,  # 'Career' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Xx2DCategory_PMA_Career_debug')
            0x193C7DC81219FD5A,  # 'Situation' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Xx2DCategory_PMA_Situation_debug')
            0xD5329B0934E989D7,  # 'Special' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Xx2DCategory_PMA_Special_debug')
            0x1A54B1AF82F79ACD,  # 'Batuu' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Add_Outfits__Xx2DCategory_PMA_Batuu_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        if CommonTypeUtils.is_sim_instance(script_object):
            return True
        if f"{script_object}".startswith('object_Mannequin'):
            return True
        return False
