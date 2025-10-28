#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from copy_outfits.enums.outfit_category import OutfitCategory
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.modinfo import ModInfo
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from sims.outfits.outfit_utils import get_maximum_outfits_for_category
from sims4communitylib.enums.tags_enum import CommonGameTag
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitAdd')
log.enable()


class OutfitAdd:

    @staticmethod
    def add_outfits(zim: CopyOutfitsSim) -> int:
        """ Return the number of created outfits """
        num_outfits_created = 0

        sim_info = zim.sim_info
        action_id = zim.action_id
        outfit_category = zim.outfit_category

        if action_id in [PieMenuActionId.X_PICKER, PieMenuActionId.X_PICKER]:
            log.debug(f"TODO implement Picker support")
            return num_outfits_created

        maximum_outfits = get_maximum_outfits_for_category(outfit_category)
        log.debug(f"Adding (0-{maximum_outfits}) '{outfit_category}' outfits to '{zim.sim_info}'")

        for outfit_index in range(0, maximum_outfits):
            if CommonOutfitUtils.has_outfit(zim.sim_info, (outfit_category, outfit_index)):
                continue

            # Create an outfit for the sim with not too much cas parts
            r'''
            As soon as CommonGameTag is implemented as a proper enum
            try:
                tag_list = (CommonGameTag[f"OUTFIT_CATEGORY_{outfit_category}"], )
            except:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_BATHING, )
            '''
            if outfit_category == OutfitCategory.EVERYDAY:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_EVERYDAY, )
            elif outfit_category == OutfitCategory.ATHLETIC:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_ATHLETIC, )
            elif outfit_category == OutfitCategory.BATUU:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_BATUU, )
            elif outfit_category == OutfitCategory.CAREER:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_CAREER, )
            elif outfit_category == OutfitCategory.COLDWEATHER:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_COLD_WEATHER, )
            elif outfit_category == OutfitCategory.HOTWEATHER:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_HOT_WEATHER, )
            elif outfit_category == OutfitCategory.FORMAL:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_FORMAL, )
            elif outfit_category == OutfitCategory.PARTY:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_PARTY, )
            elif outfit_category == OutfitCategory.SLEEP:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_SLEEP, )
            elif outfit_category == OutfitCategory.SITUATION:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_SITUATION, )
            elif outfit_category == OutfitCategory.SWIMWEAR:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_SWIMWEAR, )
            elif outfit_category == OutfitCategory.SMALL_BUSINESS:
                tag_list = (CommonGameTag.UNIFORM_SMALL_BUSINESS_EMPLOYEE, )
            else:
                tag_list = (CommonGameTag.OUTFIT_CATEGORY_BATHING, )

            CommonOutfitUtils.generate_outfit(sim_info, (outfit_category, outfit_index), tag_list)
            num_outfits_created += 1

        log.debug(f"Added {num_outfits_created} '{outfit_category}' outfits to '{zim.sim_info}'")
        return num_outfits_created
