#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'CopyOutfits'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'copy_outfits'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.0.2'


'''
TODO Far Future
    Add Pie Menu to paste with filter
        Show a picker to select the outfit groups and then the BodyParts to delete one after the other
        Show a picker to define what to filter - replace the cheat command
TODO New Features
    Clone relationships
    Implement support for filters
     Split FACE and BODY modifiers/sliders
    Implement support to append a new (or replace 5th) outfit
v1.0.2
    Update links in documentations (MTS)
v1.0.1
    Fix missing dependency
v1.0.0
    Updated the Pie Menu priority
v0.7.0
    Add support for Infants (instead of Unknown)
    Use Ts4Lib
    Add support for BodyTypes including STRETCHMARKS_BACK = 100 via TS4Lib
    Add cheat commands to define a filter. 'o19.cpo.filter help'
    Add cheat commands to append/replace 5th outfit
    Fix 'Copy Category' to copy all 1-5 outfits.
v0.6.6
    Fixed 'Traits' which can't be added (gender, ...) and caused exceptions
v0.6.5
    Added walk styles
v0.6.4
    Move new stuff to X-Transfer, add 'Traits'
v0.6.3
    With 'Age & Gender' also transfer whether the sim can give/receive pregnancy.
v0.6.2
    New paste options for age, gender, physics and genetics
v0.6.1
    Don't register the interaction for objects
'''
