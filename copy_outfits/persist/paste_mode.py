#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class PasteMode(object, metaclass=Singleton):
    def __init__(self):
        self._paste_append = False

    @property
    def paste_append(self) -> bool:
        return self._paste_append

    @paste_append.setter
    def paste_append(self, append: bool):
        self._paste_append = append
