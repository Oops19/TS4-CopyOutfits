#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Any

from copy_outfits.main import Main
from copy_outfits.enums.outfit_group_id import OutfitGroupId
from copy_outfits.enums.pie_menu_action import PieMenuAction
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.modinfo import ModInfo
from event_testing.results import TestResult
from interactions.context import InteractionContext
from sims.sim import Sim
from sims4.tuning.tunable import Tunable
from sims4communitylib.classes.interactions.common_terrain_interaction import CommonTerrainInteraction
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitTools')
log.enable()


class OutfitTools(CommonTerrainInteraction):
    INSTANCE_TUNABLES = {
        'action': Tunable(tunable_type=int, default=PieMenuAction.NONE.value),
        'action_id': Tunable(tunable_type=int, default=PieMenuActionId.NONE.value),
        'group_id': Tunable(tunable_type=int, default=OutfitGroupId.EVERYTHING.value),
        'clipboard_index': Tunable(tunable_type=int, default=-1),
        'outfit_category': Tunable(tunable_type=int, default=-1),
        'outfit_index': Tunable(tunable_type=int, default=-1),
    }
    __slots__ = {'action', 'action_id', 'clipboard_index', 'outfit_category', 'outfit_index', }

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> TestResult:
        return TestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        it = self.action, self.action_id, self.group_id, self.clipboard_index,  self.outfit_category, self.outfit_index
        return Main().on_started(interaction_sim, interaction_target, it)
