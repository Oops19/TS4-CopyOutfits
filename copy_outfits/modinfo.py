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
        return '1.9.22'


r'''
IDEAS for the far future
    Clone buffs and/or relationship bits

    CO-5 Move 'Small Business' form 'Category' into 'X-Category'.
    CO-6 Implement 'Copy Outfits' 'Add Outfits' > 'Picker', 'X-Picker'
    CO-7 Save and Load outfits
    CO-8 Support user defined skins for mannequins
    CO-9 Split Sliders into FACE, BODY and SCULPT to clone individual modifiers
        Limit to 'HEAD' and 'BODY', there are also FEET, HIPS, BODY, CHEST, NOSE, EARS, MOUTH, ...
    CO-10 Implement 'Copy Outfits' > 'Clone' > 'CAS Parts' > 'Picker'
        Show a picker to select the outfit groups and then the BodyParts to delete one after the other
        Show a picker to define what to filter - replace the cheat command
    CO-11 Clone 'buffs'
    CO-12 Clone 'relationship bits'
    CO-15 Mannequin / missing skins are applied to sims. (https://github.com/Oops19/TS4-CopyOutfits/issues/4)

v1.9.22
    CO-14 Fix 'Add Manequin' if no outfits are in buffer
v.1.9.21
    CO-13 Fix File "copy_outfits\main.py", line 249, in clone_sim_data; 'NoneType' object has no attribute 'skin_tone'
v1.9.20
    CO-1 Update the documentation, replace X-Transfer with Clone
    CO-2 Add recent screenshots to the documentation
v1.9.19
    CO-3 Fix exception for Clone > CAS Parts > Picker
v1.9.18
    CO-4 Fix exception when cloning from mannequins
v1.9.17
    Pie Menu for 'Small Business' - icons missing
v1.9.16
    Allow to create missing 'Small Business Outfits'
    'Small Business Outfits' are found in the normal 'Picker'
    Named menu icons are still missing.
v1.9.15
    Remove debug thread dump during startup
v1.9.14
    Resend also physical attribute skintone_value_shift
    Fixed type of int/OutfitCategory
v1.9.13
    Add PieMenu More > Fix Head
v1.9.12
    Add 'o19.co.fix' to apply the vanilla head to Child, Teen-Elder sims
v1.9.11
    Fix generate_outfit()
v1.9.10
    Resent physical attributes also for modified base attributes
    Update physical attributes less often
v1.9.9
    Yet another release to address the broken skin for sims.
    Remaining CAS Part flags are 'Child or Elder, Female and/or Male'.
    This may still cause skin issues for child end elder sims while mannequins can still use it.
    In case of skin issues set the default head with 's4clib.attach_cas_part head_id 3'. The default head_id for 'female male child' are 6977 8860 and 27816.
    Especially for (child and elder) occult sims these CAS parts are still selected by TS4 even if the referenced image/skin resource is missing.
    Hopefully EA fixes this TS4 bug one day and verifies that the referenced images actually exists before using a CAS Part.
v1.9.8
    Remove all CAS Part flags (including DefaultForBodyTypeFemale/Male) to avoid that TS4 uses them when aging up sims.
v1.9.7
    Fix NPE within get_parts_from_clipboard() when no CAS parts are available.
v1.9.6
    Fixed Exception while pasting outfits via picker
v1.9.5
    Modified all head CAS parts to be no longer allowed for random.
    Cleanup of imports
v1.9.4
    Rename MASCARA to EYELASHES (requires TS4T v0.3.24) 
v1.9.3
    Add outfits instead of replacing .0
v1.9.2
    Cleanup code style
v1.9.1
    Fix menu order within 'Rotate'
v1.9.0
    Experimental support for mannequins
    TS4lib requires an update.
    This mod doesn't create a new outfit (dress the mannequin) when replacing the 'bathing' outfit.
    Most useful interactions: 'Clone > Everything', 'Mannequin > Skins | Add'
    'Clone > Characteristics' may require a 'Reset' to apply these.
    Allow to add non-existing outfits to sims.
    Allow to de-/spawn mannequins on terrain, also off-lot.
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
