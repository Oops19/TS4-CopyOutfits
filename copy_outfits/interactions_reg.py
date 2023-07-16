#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.utils.common_type_utils import CommonTypeUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _RegisterOutfitTools_Copy_Outfits_0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0x4B864F684F7FC787,  # 'Print Clipboard' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More_PMA_Print_Clipboard_debug')
            0x5BA6F113C0F2661A,  # 'Clear All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More_PMA_Clear_All_debug')
            0xA88C83FEBA17597D,  # 'Clipboard 0' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_0_debug')
            0x71BE7E2EB047630C,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_1_debug')
            0x470F4F06757F1343,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_2_debug')
            0xAD750FAC05321AA2,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_3_debug')
            0x29E00A6CC15685D1,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__More__Clear_PMA_Clipboard_4_debug')
            0xE7B5AF07D572C84E,  # 'Complete OutfitTools' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Complete_Outfit_debug')
            0x0CC4DCB90A56C860,  # 'Body Paint' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Body_Paint_debug')
            0xF5023A4B64C42453,  # 'Cloth' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Cloth_debug')
            0xB8CD40D728593D35,  # 'Hand Accessories' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Hand_Accessories_debug')
            0x8B4FE1E8304CFF44,  # 'Head Accessories' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Head_Accessories_debug')
            0x1EE88925345AC29E,  # 'Head Paint' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Head_Paint_debug')
            0xF29B02DFAAA77156,  # 'Head Piercings' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Head_Piercings_debug')
            0xBA778FBC5C05189C,  # 'Occult Scars' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Occult_Scars_debug')
            0xD4E18170AF070DA0,  # 'Pet' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Pet_debug')
            0x7B66B0B9E1B23752,  # 'Sim' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Transfer_PMA_Sim_debug')
            0x6B25215E8D850230,  # 'All' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_All_debug')
            0xA456FEEFEAE2F20F,  # 'Age & Gender' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_Age_x26_Gender_debug')
            0xAA8A2721F3AF6972,  # 'Physics & Genetics' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_Physics_x26_Genetics_debug')
            0x939B8B8F908F690F,  # 'Genetics' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_Genetics_debug')
            # 0x2FEFAB196D60C9BF,  # 'Sliders' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_Sliders_debug')
            0x10827C2F06AECC9C,  # 'Traits' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Xx2DTransfer_PMA_Traits_debug')
            0x309EEC0739EF76B7,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_1_debug')
            0x82FE19747EA17CF0,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_2_debug')
            0x1217A48330E02C31,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_3_debug')
            0x95ACA9C274BBC102,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__from_PMA_Clipboard_4_debug')
            0x000B57AA1D5D8346,  # 'OutfitTools 0' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__to_PMA_Outfit_0_debug')
            0x273FF83BA8E25717,  # 'OutfitTools 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__to_PMA_Outfit_1_debug')
            0x231B25ADD594BB50,  # 'OutfitTools 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__to_PMA_Outfit_2_debug')
            0xB1471B78F81DDB11,  # 'OutfitTools 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__to_PMA_Outfit_3_debug')
            0x34DD20B83BFB23E2,  # 'OutfitTools 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__to_PMA_Outfit_4_debug')
            0x42C13C56219110CE,  # 'Clipboard 1' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_1_debug')
            0xC84962394FC118B9,  # 'Clipboard 2' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_2_debug')
            0x6656A1AB9A347ED8,  # 'Clipboard 3' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_3_debug')
            0x6924714F189D108B,  # 'Clipboard 4' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__to_PMA_Clipboard_4_debug')
            0x963363849E50ACAD,  # 'Paste' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits_PMA_Paste_debug')
            0xB4BD9EC859F87DA7,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste_PMA_Picker_debug')
            0xB93D2007E430410D,  # 'X-Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste_PMA_Xx2DPicker_debug')
            0xEC810595D17D6FBF,  # 'Copy' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits_PMA_Copy_debug')
            0x5020FF18FDB9BAC9,  # 'Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy_PMA_Picker_debug')
            0x04346C61AD16A86B,  # 'X-Picker' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy_PMA_Xx2DPicker_debug')
            0xCF47514BC12BF930,  # 'Everyday' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Everyday_debug')
            0x821AF14A79863FD0,  # 'Formal' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Formal_debug')
            0xE381D40CCD6B1AC1,  # 'Athletic' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Athletic_debug')
            0x6A47AE12568BBCF2,  # 'Sleep' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Sleep_debug')
            0xD73CB33C30AA172F,  # 'Party' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Party_debug')
            0x4C50742DB10555A0,  # 'Bathing' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Bathing_debug')
            0x65C307D86C4BEBC1,  # 'Career' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Career_debug')
            0x4780D187691D2F25,  # 'Situation' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Situation_debug')
            0x7F0B7F986F291F18,  # 'Special' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Special_debug')
            0xA26243B934ABA1E8,  # 'Swimwear' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Swimwear_debug')
            0x4285E2BDB177DBD6,  # 'Hotweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Hotweather_debug')
            0x96EE25889AED629D,  # 'Coldweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Category_PMA_Coldweather_debug')
            0x4614B28FC3E66C6E,  # 'Batuu' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Copy__Xx2DCategory_PMA_Batuu_debug')
            0xBE47A3DB04992FDA,  # 'Everyday' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Everyday_debug')
            0x4800548834695F56,  # 'Formal' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Formal_debug')
            0xE4AA0531416EFCBF,  # 'Athletic' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Athletic_debug')
            0xBFBE95D88A17E3A4,  # 'Sleep' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Sleep_debug')
            0x82FE1EE02BF2A491,  # 'Party' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Party_debug')
            0xBA2466DEED56CBCE,  # 'Bathing' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Bathing_debug')
            0x579386424F75D94B,  # 'Career' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Career_debug')
            0xFC1901CC0002F6AB,  # 'Situation' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Situation_debug')
            0x4BAFF91287481312,  # 'Special' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Special_debug')
            0x379E5BA0737A1502,  # 'Swimwear' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Swimwear_debug')
            0x95E30B80F1161FC4,  # 'Hotweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Hotweather_debug')
            0xFE3B50A478096753,  # 'Coldweather' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Category_PMA_Coldweather_debug')
            0x38592B87D566B97C,  # 'Batuu' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Paste__Xx2DCategory_PMA_Batuu_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        if not CommonTypeUtils.is_sim_instance(script_object):
            return False # If the object is not a Sim, return False.
        return True
