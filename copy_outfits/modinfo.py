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
        return '0.6.1'

'''
v0.6.1 Don't register the interaction for objects

'''
