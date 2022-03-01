
from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.utils.common_type_utils import CommonTypeUtils
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _RegisterOutfitTools_OutfitTools_0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0x12C9400C09DEE8DA,  # 'Print Clipboard' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More_PMA_Print_Clipboard_debug')
            0xD6E0821CF8F73F8F,  # 'Clear All' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More_PMA_Clear_All_debug')
            0x8B5C7843E921986A,  # 'Clipboard 0' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More__Clear_PMA_Clipboard_0_debug')
            0x2A4A8F4823B1C96B,  # 'Clipboard 1' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More__Clear_PMA_Clipboard_1_debug')
            0x4FA5C6C69436AA34,  # 'Clipboard 2' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More__Clear_PMA_Clipboard_2_debug')
            0x5D6430A229E4C325,  # 'Clipboard 3' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More__Clear_PMA_Clipboard_3_debug')
            0x5A6C5A4A44A71DAE,  # 'Clipboard 4' - fnv('o19_OutfitTools_PMC__Outfit_Tools__More__Clear_PMA_Clipboard_4_debug')
            0x94F03D1F5506FEA7,  # 'All' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_All_debug')
            0x3FCACB609A61CA6F,  # 'Body Paint' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Body_Paint_debug')
            0xAD03A8BD50EC121A,  # 'Cloth' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Cloth_debug')
            0xCCDA716B7809346A,  # 'Hand Accessories' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Hand_Accessories_debug')
            0x29DE7A230452C1F7,  # 'Head Accessories' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Head_Accessories_debug')
            0xAA150F5E7990CB2D,  # 'Head Paint' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Head_Paint_debug')
            0xE5BFE0F66AB91829,  # 'Head Piercings' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Head_Piercings_debug')
            0x0C6B2EC31735EFEB,  # 'Occult Scars' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Occult_Scars_debug')
            0x0218C249138A7795,  # 'Pet' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Pet_debug')
            0x7DEF6F04E48F1037,  # 'Sim' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Transfer_PMA_Sim_debug')
            0xFA329AAEBBB31384,  # 'Clipboard 1' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__from_PMA_Clipboard_1_debug')
            0x28325CB864EC85BB,  # 'Clipboard 2' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__from_PMA_Clipboard_2_debug')
            0xDE6521A9D9EE973A,  # 'Clipboard 3' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__from_PMA_Clipboard_3_debug')
            0xB466162C627DB529,  # 'Clipboard 4' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__from_PMA_Clipboard_4_debug')
            0xBAE65CBDFB928567,  # 'Outfit 0' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__to_PMA_Outfit_0_debug')
            0xBAE5F5BAABC98056,  # 'Outfit 1' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__to_PMA_Outfit_1_debug')
            0x993082134CF70061,  # 'Outfit 2' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__to_PMA_Outfit_2_debug')
            0xE1E15B1027501720,  # 'Outfit 3' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__to_PMA_Outfit_3_debug')
            0xB89DEAB26A4843D3,  # 'Outfit 4' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__to_PMA_Outfit_4_debug')
            0xC39E24C1FECDE97B,  # 'Clipboard 1' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__to_PMA_Clipboard_1_debug')
            0x959E62B855947744,  # 'Clipboard 2' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__to_PMA_Clipboard_2_debug')
            0x21876AA06243A1F5,  # 'Clipboard 3' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__to_PMA_Clipboard_3_debug')
            0x718731DD5B31623E,  # 'Clipboard 4' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__to_PMA_Clipboard_4_debug')
            0x14B87A86412B87C0,  # 'Paste' - fnv('o19_OutfitTools_PMC__Outfit_Tools_PMA_Paste_debug')
            0x616516756A3A20BE,  # 'Picker' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste_PMA_Picker_debug')
            0x6209B5F9B9A776C0,  # 'X-Picker' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste_PMA_Xx2DPicker_debug')
            0x606616021F6A5F3C,  # 'Copy' - fnv('o19_OutfitTools_PMC__Outfit_Tools_PMA_Copy_debug')
            0x897686AB68B36FF2,  # 'Picker' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy_PMA_Picker_debug')
            0xD852E31FC12A5ACC,  # 'X-Picker' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy_PMA_Xx2DPicker_debug')
            0x4746DBE5A4BFC63F,  # 'Everyday' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Everyday_debug')
            0xD65F489E9F34F18F,  # 'Formal' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Formal_debug')
            0x5D8785A1B657728E,  # 'Athletic' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Athletic_debug')
            0xF755082EEF94E28B,  # 'Sleep' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Sleep_debug')
            0x6A0C7DBD679A31B6,  # 'Party' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Party_debug')
            0xCF1C4CFCACC893C9,  # 'Bathing' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Xx2DCategory_PMA_Bathing_debug')
            0xA775A2AF45A627E6,  # 'Career' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Xx2DCategory_PMA_Career_debug')
            0x66463CDB3319906C,  # 'Situation' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Xx2DCategory_PMA_Situation_debug')
            0x01CA9A3B3CBA66AD,  # 'Special' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Xx2DCategory_PMA_Special_debug')
            0xB94EE60C2CAE3407,  # 'Swimwear' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Swimwear_debug')
            0x9E4964CCE2B54E19,  # 'Hotweather' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Hotweather_debug')
            0xB82BC7B9C5363470,  # 'Coldweather' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Category_PMA_Coldweather_debug')
            0xDFC30A9F66417BCF,  # 'Batuu' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Copy__Xx2DCategory_PMA_Batuu_debug')
            0x99050CE9601074D3,  # 'Everyday' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Everyday_debug')
            0x457FF992AD850E73,  # 'Formal' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Formal_debug')
            0x474FDF346A050D12,  # 'Athletic' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Athletic_debug')
            0xAD32B6605BECFC6F,  # 'Sleep' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Sleep_debug')
            0x7B3422A54FA6812A,  # 'Party' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Party_debug')
            0x3936D70ECC406C95,  # 'Bathing' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Xx2DCategory_PMA_Bathing_debug')
            0x0998CDF7A8701942,  # 'Career' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Xx2DCategory_PMA_Career_debug')
            0x212D97B501EDA808,  # 'Situation' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Xx2DCategory_PMA_Situation_debug')
            0x69448726FDED0D31,  # 'Special' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Xx2DCategory_PMA_Special_debug')
            0x7D36934C195E258B,  # 'Swimwear' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Swimwear_debug')
            0xF10386D3918377BD,  # 'Hotweather' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Hotweather_debug')
            0x8BD6992B17EB99F4,  # 'Coldweather' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Category_PMA_Coldweather_debug')
            0xAD3C7334DFB863AB,  # 'Batuu' - fnv('o19_OutfitTools_PMC__Outfit_Tools__Paste__Xx2DCategory_PMA_Batuu_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        if not CommonTypeUtils.is_sim_instance(script_object):
            return False # If the object is not a Sim, return False.
        return True
