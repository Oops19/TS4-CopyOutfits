#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import random
import sys
import threading
import traceback
from typing import Dict, Set

import services
from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.enums.default_head import DefaultHead
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.modinfo import ModInfo
from copy_outfits.persist.skin_store import SkinStore
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from objects import HiddenReasonFlag, ALL_HIDDEN_REASONS
from sims.sim_info import SimInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.services.sim.cas.common_sim_outfit_io import CommonSimOutfitIO
from sims4communitylib.utils.cas.common_cas_utils import CommonCASUtils
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_gender_utils import CommonGenderUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.common_enums.body_type import BodyType
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitSkin')
log.enable()


class OutfitSkin(metaclass=Singleton):
    do_init = True

    def __init__(self):
        log.debug(f"{OutfitSkin.do_init}")
        if OutfitSkin.do_init is True:
            OutfitSkin.do_init = False
            self.init()

    """ Add skins to sims """
    def init(self):
        log.debug(f"init")

        self.available_skins: Dict = {
            CopyOutfitsAge.TYAE: {
                True: [],  # Female / is_female==True
                False: [],  # Male
            },
            CopyOutfitsAge.CHILD: {
                True: [],  # Female
                False: [],  # Male
            },
        }
        self.supported_skins: Dict = {
            CopyOutfitsAge.TYAE: {
                True: [  # is_female, used in o19_yfHead.package
                    # The high-bit must be set for all custom CAS Parts. Otherwise, they will not be found.
                    # custom head cas part, custom skin images, description
                    (0xFD57E11C9F0D2AFD, 0xA83ABE943B90DD44, 'ddarkpinkrosa0_Miami_Skin_V1'),
                    (0xE2F29393763FBEFD, 0xE9DF3FAEC660DE19, 'ddarkpinkrosa0_Miami_Skin_V1'),
                    (0xF2157D9C0F5DBB0C, 0xE1750D34ED49C938, 'ddarkpinkrosa0_Miami_Skin_V1'),
                    (0x8C0E7897293238B3, 0xEE0B69DE5BBD855F, 'ddarkpinkrosa0_Miami_Skin_V1'),
                    (0x93563E918FEBB5BC, 0x83E62685A97D8F89, 'JS_007Skin'),
                    (0xA9876E2C98488A1F, 0xC17C5B56ACB01052, 'JS_007Skin'),
                    (0xE3F4C09AE4116472, 0xEEC5C7D8C1141D6F, 'JS_007Skin'),
                    (0x8B269F3A852B0059, 0xC42933F4CFD6B686, 'JS_008Skin'),
                    (0x8F30F85CC19644C1, 0xDABE010DB300612C, 'JS_008Skin'),
                    (0x8D88C11365FFA9EC, 0xA91D148D8D6709B5, 'JS_008Skin'),
                    (0xCD27D0CC83CC79CE, 0xA2C37B6FF654696D, '[THISISTHEM] Pamela Anderson Skin'),
                    (0x8111880154582F44, 0xBF054E412D1C3FF1, '[THISISTHEM] Selena G. Skin'),
                    (0xD8191C563F223169, 0x945804D533C7195C, '[THISISTHEM] Salma Hayek Skin'),
                    (0x987751B214F2E943, 0xAC597DD75A2F5AEE, '[THISISTHEM] Rihanna Skin'),
                    (0xE5CFDDCBB78C6BA3, 0xA29F929AA4995422, '[THISISTHEM] Clémentine Skin'),
                    (0xF1ADB9C2D8AE9F78, 0xBCEC44FB88C29A83, '[THISISTHEM] Suzie Skin'),
                    (0xF2C0E624085BB1AB, 0xA7C5CC25F8956A9A, '[THISISTHEM] Divya Skin'),
                    (0xBCB53E389E68DA4B, 0xE56E337611D4C315, '[THISISTHEM] Jenna Skin'),
                    (0xBCBDC13D5BCF3C5F, 0x862EC5514B8E4EE8, '[THISISTHEM] Nayla Skin'),
                    (0x9DACD5DFA64FBCF5, 0xE702BF8602F51CAA, '[THISISTHEM] Asha Skin'),
                    (0x9868EBFC6E8E5D4D, 0xB4B4EABA8ADEB62A, '[THISISTHEM] Hye-Jeong Skin'),
                    (0xEAECC7875C23908D, 0x83AE964764D81BA6, '[THISISTHEM] Yoon Young Skin'),
                    (0xB43F17ECA2ADE6A8, 0xA3B77DEBA532B6ED, '[THISISTHEM] Anok Skin'),
                    (0xF5E803E374BAAA88, 0xC6E085AE73312D6D, '[THISISTHEM] Ashley Skin'),
                    (0xA59BBF6B64B413FF, 0xAD660A57BEC2E456, '[THISISTHEM] Abény Skin'),
                    (DefaultHead.YF_HEAD_DEFAULT.value, DefaultHead.YF_HEAD_DEFAULT.value, 'TS4 Default'),
                ],
                False: [  # is_male, used in o19_ymHead.package
                    (0xE66AA85AD5A6C480, 0xA63963459FAC2D01, '[THISISTHEM] A$AP Rocky Skin'),
                    (0xACA3B7ABB3685226, 0x9116D5AB84042CDD, '[THISISTHEM] Djibril Skin'),
                    (0xF6A0375C754567A7, 0x93A1C806A844BC7C, '[THISISTHEM] Jacob Elordi Skin'),
                    (DefaultHead.YM_HEAD_DEFAULT.value, DefaultHead.YM_HEAD_DEFAULT.value, 'TS4 Default'),
                ],
            },
            CopyOutfitsAge.CHILD: {
                True: [  # is_female
                    (0xE28829A8F12B9633, 0x88FAFEB05A6FC545, '[THISISTHEM] Child Skin N18'),
                    (0xDDB8501105C39A87, 0xA50AEC5AF2019EC1, '[THISISTHEM] Child Skin N19'),
                    (0xFE246E651CEC2C4A, 0x9F4AB0CEBDA786D7, '[THISISTHEM] Child Skin N22'),
                    (0xA0A24376A4CB35F8, 0x9C34ED7FA6AD7603, '[THISISTHEM] Child Skin N23'),
                    (DefaultHead.CU_HEAD_DEFAULT.value, DefaultHead.CU_HEAD_DEFAULT.value, 'TS4 Default'),
                ],
                False: [  # is_male
                    (0xC0251674E90910D7, 0xB368D42AAC081FF0, '[THISISTHEM] Child Skin N17'),
                    (0xDDB8501105C39A87, 0xA50AEC5AF2019EC1, '[THISISTHEM] Child Skin N19'),
                    (0xA0A24376A4CB35F8, 0x9C34ED7FA6AD7603, '[THISISTHEM] Child Skin N23'),
                    (0x800298CD9078A60D, 0xA78520CC00C7191C, '[THISISTHEM] Child Skin N24'),
                    (DefaultHead.CU_HEAD_DEFAULT.value, DefaultHead.CU_HEAD_DEFAULT.value, 'TS4 Default'),
                ],
            },
        }

        missing_packages: Set = set()
        for sim_age in [CopyOutfitsAge.CHILD, CopyOutfitsAge.TYAE, ]:
            _ages = {}
            for is_female in [True, False, ]:
                _available_skins = []
                for data in self.supported_skins.get(sim_age).get(is_female):
                    check_cas_part, use_cas_part, package_name = data
                    if CommonCASUtils.is_cas_part_loaded(check_cas_part):
                        if CommonCASUtils.is_cas_part_loaded(use_cas_part):
                            _available_skins.append(use_cas_part)
                        else:
                            # this should never happen
                            log.warn(f"copy_outfits.package missing or broken - {use_cas_part:016X} not found!")
                    else:
                        missing_packages.add(package_name)
                        log.warn(f"Dropping: {is_female} {sim_age}: {data}")
                _ages.update({is_female: _available_skins})
            self.available_skins.update({sim_age: _ages})

        if missing_packages:
            log.info(f"Optional packages which are not installed: '{missing_packages}'. Install some of them to use more skins on mannequins.")

        log.debug(f".... {self.available_skins}")
        # Initialize store with the available skins
        self.skin_store = SkinStore(self.available_skins)
        log.debug(f"init-end")

    # A78520CC00C7191C
    def apply_skin(self, zim: CopyOutfitsSim):
        sim_info = zim.sim_info
        outfit_category = zim.outfit_category
        outfit_index = zim.outfit_index
        mannequin_component = zim.mannequin_component
        action_id = zim.action_id

        offset = 0
        random_offset = False
        if action_id == PieMenuActionId.NEXT_SKIN:
            offset = 1
        elif action_id == PieMenuActionId.PREVIOUS_SKIN:
            offset = -1
        elif action_id == PieMenuActionId.RANDOM_SKIN:
            random_offset = True
        log.debug(f"offset {offset} {random_offset}")
        head_skin = self.skin_store.get_skin(zim.sim_age, zim.is_female, offset, random_offset)

        parts = CommonOutfitUtils.get_outfit_parts(zim.sim_info, (zim.outfit_category, zim.outfit_index)).copy()
        log.debug(f"{outfit_category} - {outfit_index} - {parts} ")
        current_head = parts.get(3)
        parts.update({3: head_skin})
        log.debug(f"{outfit_category} - {outfit_index} - {parts} ")
        sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=(outfit_category, outfit_index), initial_outfit_parts=parts, mod_identity=ModInfo.get_identity())
        sim_outfit_io.apply(apply_to_outfit_category_and_index=(outfit_category, outfit_index))

        if mannequin_component:
            mannequin_component.set_current_outfit = (outfit_category, outfit_index)
            mannequin_component._on_outfit_change(sim_info, (outfit_category, outfit_index))
        else:
            sim_info._current_outfit = (outfit_category, outfit_index)
        log.debug(f"Replacing head {current_head} with new {head_skin}.")

    def fix_head(self, sim_info: SimInfo):
        sim_info = CommonSimUtils.get_sim_info(sim_info)
        if not sim_info:
            return
        if CommonAgeUtils.is_child(sim_info):
            sim_age = CopyOutfitsAge.CHILD
        elif CommonAgeUtils.is_teen_adult_or_elder(sim_info):
            sim_age = CopyOutfitsAge.TYAE
        else:
            log.info(f"Age not supported.")
            return
        is_female = CommonGenderUtils.is_female(sim_info)
        old_head_id = CommonCASUtils.get_cas_part_id_at_body_type(sim_info, BodyType.HEAD.value)
        # True == CommonCASUtils.is_cas_part_loaded(old_head_id) as the part is 'in use'. A test makes no sense.
        head_ids = OutfitSkin().available_skins.get(sim_age).get(is_female)
        head_id = random.choice(head_ids)

        log.info(f"Fixing '{sim_info}'s head to {head_id} (from {old_head_id}).")
        CommonCASUtils.attach_cas_part_to_sim(sim_info, head_id, BodyType.HEAD.value)

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.co.fix', 'Fix the head of the active sim.')
    def cheat_o19_test_print_genetics(output: CommonConsoleCommandOutput):
        sim_info = CommonSimUtils.get_active_sim_info()
        OutfitSkin().fix_head(sim_info)


# Init OutfitSkin / SkinStore as soon as possible
OutfitSkin()
