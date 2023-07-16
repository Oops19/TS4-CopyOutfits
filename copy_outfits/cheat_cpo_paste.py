#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import re

from copy_outfits.enums.outfit_groups import OutfitGroups
from copy_outfits.enums.physic_filters import PhysicFilters
from copy_outfits.enums.various_filters import VariousFilters
from copy_outfits.persist.filter import Filter
from copy_outfits.persist.paste_mode import PasteMode
from copy_outfits.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.common_enums.body_part import BodyPart


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()


@CommonConsoleCommand(
    ModInfo.get_identity(), 'o19.cpo.paste', '...',
    command_arguments=(
        CommonConsoleCommandArgument('mode', 'String', "'replace' or 'append' outfits.", is_optional=True, ),
    ),
)
def o19_cmd_cpo_paste(output: CommonConsoleCommandOutput, mode: str = ''):
    """
    o19.cpo.paste print  # Print current setting
    o19.cpo.paste replace  # Replace existing outfits. If an empty slot is selected the outfit will be appended.
    o19.cpo.paste append  # Append a new outfit or replace the 5th outfit
    """
    try:
        log.debug(f"paste '{mode}'")
        if mode == 'print':
            output(f"Current mods: {PasteMode().paste_append}")
        elif mode == 'replace':
            PasteMode().paste_append = False
        elif mode == 'append':
            PasteMode().paste_append = True
        else:
            output(f"""Usage:
o19.cpo.paste  # Print this message
o19.cpo.paste print  # Print current setting
o19.cpo.paste replace  # Replace existing outfits
o19.cpo.paste append  # Append a new outfit or replace the 5th outfit""")
    except Exception as e:
        log.error(f"Oops: {e}", throw=True)

