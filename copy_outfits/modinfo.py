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
        return '1.9.0'


r'''
IDEAS for the far future
    Add Pie Menu to paste with filter
        Show a picker to select the outfit groups and then the BodyParts to delete one after the other
        Show a picker to define what to filter - replace the cheat command
    Clone buffs and/or relationship bits
    Split FACE and BODY modifiers/sliders

TODO
    Load and Save outfits
    Read config files / support user defined skins
    
v1.9.0
    Experimental support for mannequins
    TS4lib requires an update.
    This mod doesn't create a new outfit (dress the mannequin) when replacing the 'bathing' outfit.
    Most useful interactions: 'Clone > Everything', 'Mannequin > Skins | Add'
    'Clone > Characteristics' may require a 'Reset' to apply these.
    Allow to add non-existing outfits to sims.
    Allow to de-/spawn mannequins on the floor, also off-lot.
    Fixed Age.PET
    Added Age.HORSE
    Added X-OutfitCategory.SPECIAL[FASHION]
    Outfit order is now: BATHING; SITUATION; CAREER.[0-2]; SPECIAL.[DEFAULT,TOWEL,FASHION]; BATUU.[0-4] with picker hint notification.
    Address exception "_on_outfit_change() 'missing 2 required positional arguments: 'sim_info_wrapper' and 'outfit_category_and_index'" within a 3rd party mod.
v1.0.6
    Tested with TS4 v1.107
v1.0.5
    Imports cleaned up
v1.0.4
    Added INFANT
    Added PET and BABY (likely never needed)
v1.0.3
    Updated README for new TS4 version
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
