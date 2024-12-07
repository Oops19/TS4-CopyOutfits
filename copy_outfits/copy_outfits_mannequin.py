#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import random
from typing import Any, Tuple, Union

# noinspection PyUnresolvedReferences
from sims4.math import Vector3, Quaternion, Transform, Location
import routing
import services
import sims4

from copy_outfits.enums.outfit_category import OutfitCategory
from copy_outfits.modinfo import ModInfo
from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.enums.pie_menu_action_id import PieMenuActionId
from copy_outfits.outfit_skin import OutfitSkin
from copy_outfits.struct.copy_outfits_sim import CopyOutfitsSim
from copy_outfits.utils.copy_outfit_utilities import CopyOutfitUtilities
from sims.outfits.outfit_utils import get_maximum_outfits_for_category
from sims.sim import Sim
from sims.sim_info import SimInfo
from sims4communitylib.utils.objects.common_object_ownership_utils import CommonObjectOwnershipUtils
from sims4communitylib.utils.objects.common_object_spawn_utils import CommonObjectSpawnUtils
from sims4communitylib.utils.objects.common_object_utils import CommonObjectUtils
from sims4communitylib.utils.sims.common_household_utils import CommonHouseholdUtils

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.classes.coordinates.std_euler_angle import StdEulerAngle
from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
from ts4lib.utils.outfit_utilities import OutfitUtilities
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'AddMannequin')
log.enable()


class CopyOutfitsMannequin(metaclass=Singleton):
    def __init__(self):
        self.guids = {
            CopyOutfitsAge.TYAE: {
                True: [71052, 75022, 75023, 75024, 75025, 75026, 75027, 75028, 75029, 75030, ],  # Female
                False: [71054, 75031, 75032, 75033, 75034, 75035, 75036, 75037, 75038, 75039, ],  # Male
            },
            CopyOutfitsAge.CHILD: {
                True: [71056, 75040, 75041, 75042, 75043, 75044, 75045, 75046, 75047, 75048, ],  # Female
                False: [71059, 75049, 75050, 75051, 75052, 75053, 75054, 75055, 75056, 75057, ],  # Male
            },
        }

    def change_mannequin(self, zim: CopyOutfitsSim, interaction_sim: Sim, interaction_target: Any):
        log.debug(f"change_mannequin {zim.mannequin_component} {interaction_sim} {interaction_target}")
        log.debug(f"change_mannequin {zim.action_id}")

        if zim.action_id in [PieMenuActionId.MANNEQUIN_YF, PieMenuActionId.MANNEQUIN_YM, PieMenuActionId.MANNEQUIN_CF, PieMenuActionId.MANNEQUIN_CM, ]:
            self.add_mannequin(zim, interaction_sim, interaction_target)
        elif zim.action_id in [PieMenuActionId.MANNEQUIN_ROTATE_ZERO, PieMenuActionId.MANNEQUIN_ROTATE_LEFT, PieMenuActionId.MANNEQUIN_ROTATE_RIGHT, ]:
            self.rotate_mannequin(zim, interaction_target)

        elif zim.action_id in [PieMenuActionId.MANNEQUIN_REMOVE, ]:
            self.destroy_mannequin(zim, interaction_target)

    def rotate_mannequin(self, zim: CopyOutfitsSim, interaction_target: Any):
        log.debug(f"rotate_mannequin {zim.mannequin_component} {interaction_target}")
        log.debug(f"rotate_mannequin {zim.action_id}")
        item = interaction_target
        action_id = zim.action_id

        position, orientation, level, routing_surface, parent_object_id = self._game_object_location(item)
        if position is None:
            return

        if action_id == PieMenuActionId.MANNEQUIN_ROTATE_ZERO:
            yaw = 'to 0'
            q = StdQuaternion()
        else:
            if action_id == PieMenuActionId.MANNEQUIN_ROTATE_LEFT:
                yaw = 1
            else:
                yaw = -1

            # Rotate:
            q = StdQuaternion(orientation.w, orientation.x, orientation.y, orientation.z)
            roll = 0
            pitch = 0
            yaw = yaw * random.randint(10, 50)

            relative_euler_angle = StdEulerAngle(roll, pitch, yaw, convert_deg_to_rad=True)
            relative_q: StdQuaternion = relative_euler_angle.quaternion()
            q = q * relative_q

        orientation = q.as_ts4_quaternion()
        location = sims4.math.Location(sims4.math.Transform(position, orientation), routing_surface)
        try:
            item.location = location
            item.resend_location()
            log.debug(f"Rotated '{item}' {yaw}°")
        except Exception as e:
            log.warn(f"Exception '{e}' occurred while rotating.")

    def _game_object_location(self, _object) -> Tuple[Vector3, Quaternion, int, int, int]:
        position: Union[Vector3, None] = None
        orientation: Union[Quaternion, None] = None
        level = 0
        routing_surface = 0
        parent_object_id = 0
        try:
            position = _object._location.transform.translation
            orientation = _object._location.transform.orientation
            level: int = getattr(_object._location, 'level', 0)
            # level = _object._location.routing_surface.secondary_id
            routing_surface = getattr(_object, 'routing_surface', routing.SurfaceType.SURFACETYPE_WORLD)
            if _object.parent:
                parent_object_id = _object.parent.id
            else:
                parent_object_id = None
            return position, orientation, level, routing_surface, parent_object_id
        except Exception as e:
            log.warn(f"Oops ({e}). Couldn't get generic position of '{_object}'")

            try:
                if isinstance(_object, Sim):
                    (position, orientation, level, _surface_id) = _object.get_location_for_save()
                    _zone_id = services.current_zone_id()
                    routing_surface = routing.SurfaceIdentifier(_zone_id, level, routing.SurfaceType.SURFACETYPE_WORLD)
                else:
                    position = _object.position
                    orientation = _object.orientation
                    # _level = getattr(item, 'level', 0)
                    routing_surface = getattr(_object, 'routing_surface', routing.SurfaceType.SURFACETYPE_WORLD)
                return position, orientation, level, routing_surface, parent_object_id
            except Exception as e:
                log.warn(f"Oops ({e}). Couldn't get position of '{_object}'")
            return position, orientation, level, routing_surface, parent_object_id

    def destroy_mannequin(self, zim: CopyOutfitsSim, interaction_target: Any):
        log.debug(f"destroy_mannequin {zim.mannequin_component} {interaction_target}")
        if zim.mannequin_component:
            msg: str = f"Destroyed {interaction_target}"
            CommonObjectSpawnUtils.destroy_object(zim.interaction_target)
            log.debug(msg)

    def add_mannequin(self, zim: CopyOutfitsSim, interaction_sim: Sim, interaction_target: Any):
        action_id = zim.action_id
        clipboard_index = 0

        if action_id == PieMenuActionId.MANNEQUIN_YF:
            sim_age = CopyOutfitsAge.TYAE
            is_female = True
        elif action_id == PieMenuActionId.MANNEQUIN_YM:
            sim_age = CopyOutfitsAge.TYAE
            is_female = False
        elif action_id == PieMenuActionId.MANNEQUIN_CF:
            sim_age = CopyOutfitsAge.CHILD
            is_female = True
        elif action_id == PieMenuActionId.MANNEQUIN_CM:
            sim_age = CopyOutfitsAge.CHILD
            is_female = False
        else:
            return True

        parts = CopyOutfitUtilities().get_parts_from_clipboard(sim_age, clipboard_index).copy()
        if not parts:
            log.debug(f"Found no parts for age {sim_age} and clipboard {clipboard_index}")
            return

        instance_ids = self.guids.get(sim_age).get(is_female)
        instance_id = random.choice(instance_ids)
        log.debug(f"Using mannequin '{instance_id}'")
        game_object = CommonObjectSpawnUtils.spawn_object_on_lot(instance_id, interaction_target.location)
        if game_object is not None:
            _sim_info: SimInfo = CommonSimUtils.get_sim_info(interaction_sim)
            CommonObjectOwnershipUtils.set_owning_household_id(game_object, CommonHouseholdUtils.get_household_id(_sim_info))

            game_object_id = CommonObjectUtils.get_object_id(game_object)
            log.info(f"Spawned {instance_id} as {game_object} with ID {game_object_id}")

            mannequin_component = zim.mannequin_component = game_object.mannequin_component
            sim_info = zim.sim_info = getattr(zim.mannequin_component, '_sim_info_data', None)

            # TODO (OutfitCategory.EVERYDAY.value, OutfitCategory.PARTY.value)== 5 = safe; (OutfitCategory.EVERYDAY.value, OutfitCategory.BATUU.value)  # 13 risky
            outfit_category = zim.outfit_category = random.randint(OutfitCategory.EVERYDAY.value, OutfitCategory.BATUU.value)
            maximum_outfits = get_maximum_outfits_for_category(zim.outfit_category)
            outfit_index = zim.outfit_index = random.randint(0, maximum_outfits - 1)

            log.debug(f"Using outfit '{outfit_category}.{outfit_index}'")
            mannequin_component.set_current_outfit = (outfit_category, outfit_index)
            mannequin_component._on_outfit_change(sim_info, (outfit_category, outfit_index))
            OutfitUtilities().apply_outfit(zim.sim_info, parts, (outfit_category, outfit_index))

            # Apply a skin
            zim.sim_age = sim_age
            zim.is_female = is_female
            zim.action_id = PieMenuActionId.RANDOM_SKIN
            OutfitSkin().apply_skin(zim)

        else:
            log.warn(f"Spawning of {instance_id} failed.")
