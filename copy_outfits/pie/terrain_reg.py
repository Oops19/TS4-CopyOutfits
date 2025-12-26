#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Tuple

from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_TERRAIN_LOAD)
class RegisterCopyOutfitsTerrainInteractions(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xA4C3FF059DBFBC58,  # 'Adult Female' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Adult_Female_debug')
            0xB6F3DD7382AEEF83,  # 'Adult Male' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Adult_Male_debug')
            0xC24D189F4EFFF3A2,  # 'Child Female' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Child_Female_debug')
            0x4C7BC30EF1D3B919,  # 'Child Male' - fnv('o19_Copy_Outfits_PMC__Copy_Outfits__Mannequin__Add_PMA_Child_Male_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True
