#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from copy_outfits.enums.outfit_groups import OutfitGroups
from copy_outfits.enums.pie_menu_action_ids import PieMenuActionIds
from sims.sim_info import SimInfo
from ts4lib.utils.singleton import Singleton


class OutfitModifiers(object, metaclass=Singleton):
    def __init__(self):
        self.installed = False  # True if a mod which uses outfit modifiers is installed. Try to remove these modifiers on paste (otherwise some pasted parts might be replaced by outfit modifiers.
        try:
            from deviantcore.cas_part_system.enums.part_layer import DCPartLayer
            from deviousdesires.nudity_system.utils.nudity_system_utils import DDNuditySystemUtils
            self.installed = True
        except:
            pass

    def remove_all_outfit_appearance_modifiers(self, sim_info: SimInfo):
        if self.installed:
            try:
                from deviantcore.cas_part_system.enums.part_layer import DCPartLayer
                from deviousdesires.nudity_system.utils.nudity_system_utils import DDNuditySystemUtils
                for body_type in OutfitGroups.parts[PieMenuActionIds.ALL_OUTFITS_FOR_CATEGORY]:
                    DDNuditySystemUtils().set_equipment_part_to_layer_by_body_location(sim_info, body_type, DCPartLayer.OUTERWEAR)
            except:
                pass
