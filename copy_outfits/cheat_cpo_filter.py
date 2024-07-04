#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import re

from copy_outfits.enums.outfit_groups import OutfitGroups
from copy_outfits.enums.physic_filters import PhysicFilters
from copy_outfits.enums.various_filters import VariousFilters
from copy_outfits.persist.filter import Filter
from copy_outfits.modinfo import ModInfo

from ts4lib.common_enums.body_type import BodyType

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


@CommonConsoleCommand(
    ModInfo.get_identity(), 'o19.cpo.filter', '...',
    command_arguments=(
        CommonConsoleCommandArgument('filter_type', 'String', "To 'include' or 'exclude' parts.", is_optional=False, ),
        CommonConsoleCommandArgument('filter_values', 'String', 'Should start and end with " to be one long string.', is_optional=True, default_value='')
    ),
)
def o19_cmd_cpo_filter(output: CommonConsoleCommandOutput, filter_type: str, filter_values: str = ''):
    """
    Define the filters:
    o19.cpo.filter print  # Print all filters
    o19.cpo.filter reset  # Reset all filters
    o19.cpo.filter disable  # Disable the filters temporarily. Each modification enables them again.
    o19.cpo.filter enable  # Enable temporarily disabled filters.
    o19.cpo.filter exclude "bt=... og=... ph=... v=..."  # Define exclude filters
    o19.cpo.filter include "bt=... og=... ph=... v=..."  # Define include filters

    The bp BodyPart and/or og OutfitGroups filter both define BodyParts (HAT, HEAD, ...). 'exclude' will remove all BodyParts and the specified will be used.
    For 'include' all BodyParts are added to the filter and only the specified will be removed from it.

    The ph Physics filter allows to filter physique attributes.
    The v Various filter allows to filter various attributes.
    For 'v' and 'ph' the same 'include' / 'exclude' logic applies.

    Groups (bt/og, ph, v) can be used multiple times. "bp=HEAD, HAT, og=..." is the same as "bp=HAT, og=..., bp=HEAD"

    'exclude' and 'include' can both be used like this:
    o19.cpo.filter exclude "bp=... og=..."
    o19.cpo.filter include "ph=..."
    o19.cpo.filter exclude "v=..."
    Any further include/exclude command will completely replace the filters for the specified group (bt/og, ph, v).
    """
    try:
        log.debug(f"filter '{filter_type}': '{filter_values}'")
        if filter_type == 'exclude':
            default_filter_all = False
        elif filter_type == 'include':
            default_filter_all = True
        else:
            if filter_type == 'disable':
                Filter().enable_filter(enable=False)
                return
            elif filter_type == 'enable':
                Filter().enable_filter()
                return
            elif filter_type == 'help':
                output("""Usage:
o19.cpo.filter print  # Print all filters
o19.cpo.filter reset  # Reset all filters
o19.cpo.filter disable  # Disable the filters temporarily. Each modification enables them again.
o19.cpo.filter enable  # Enable temporarily disabled filters.
o19.cpo.filter exclude "bp=... og=... v=... ph=..."  # Define exclude filters
o19.cpo.filter include "bp=... og=... v=... ph=..."  # Define include filters
o19.cpo.filter exclude "bp=... og=..."  # Define BP and OG exclude filters
o19.cpo.filter include ph=..."  # Define PH include filters
See log file for bp, og, ph and v parameters.
""")
                log.info("""Usage:
o19.cpo.filter print  # Print all filters
o19.cpo.filter reset  # Reset all filters
o19.cpo.filter disable  # Disable the filters temporarily. Each modification enables them again.
o19.cpo.filter enable  # Enable temporarily disabled filters.
o19.cpo.filter exclude "bp=... og=... v=... ph=..."  # Define exclude filters
o19.cpo.filter include "bp=... og=... v=... ph=..."  # Define include filters""")
                _a = {e.key for e in BodyType}
                log.info(f"BodyParts BP: {_a}")
                for _s in 'body_paint cloth hand_accessories head_accessories head_paint head_piercings occult_scars pet unknown sim'.split(' '):
                    log.info(f"OutfitGroup OG: {_s}={getattr(OutfitGroups, _s)}")
                _a = {e.key for e in VariousFilters}
                log.info(f"Various V: {_a}")
                _a = {e.key for e in PhysicFilters}
                log.info(f"Physics PH: {_a}")
            elif filter_type == 'print':
                output(f"Filter enabled: {Filter()._enabled}")
                output(f"Filter BP: {Filter()._filter_body_parts}")
                output(f"Filter V: {Filter()._filter_various}")
                output(f"Filter PH: {Filter()._filter_physics}")
                return
            elif filter_type == 'reset':
                Filter().enable_filter(enable=False)
                Filter().filter_body_parts(False)
                Filter().filter_various(False)
                Filter().filter_physiques(False)
                output(f"Cleared all filters.")
                return

            output(f"Unknown filter_type {filter_type}")
            return
        Filter().enable_filter()
        filter_values = re.sub(r"[\t ,;]+", ',', filter_values)  # normalize to "a=b,c,d,e=f,g,h"
        if "bp=" in filter_values or "og=" in filter_values:
            Filter().filter_body_parts(default_filter_all)
        if "v=" in filter_values:
            Filter().filter_various(default_filter_all)
        if "ph=" in filter_values:
            Filter().filter_physiques(default_filter_all)
        while True:
            m = re.match(r'^(.*?)([a-z]+=[^=]+)$', filter_values)  # match the last 'n=..'
            if m is None:
                break
            filter_values = m[1]
            k, v = m[2].split('=')
            if k == 'bp':
                if default_filter_all:
                    Filter().clear_filter_body_parts(v)
                else:
                    Filter().filter_body_parts(v)
            elif k == 'og':
                if default_filter_all:
                    Filter().clear_filter_outfit_groups(v)
                else:
                    Filter().filter_outfit_groups(v)
            elif k == 'v':
                if default_filter_all:
                    Filter().clear_filter_various(v)
                else:
                    Filter().filter_various(v)
            elif k == 'ph':
                if default_filter_all:
                    Filter().clear_filter_physiques(v)
                else:
                    Filter().filter_physiques(v)
            else:
                output(f"Skipping unknown '{k}={v}'")

    except Exception as e:
        log.error(f"Oops: {e}", throw=True)

