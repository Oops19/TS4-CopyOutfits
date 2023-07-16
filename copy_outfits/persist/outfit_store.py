#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class OutfitStore(object, metaclass=Singleton):

    outfits = {}  # {AGE_ID: { clipboard_index: parts, ...}, ...}
    sources = {}  # {AGE_ID: { clipboard_index: sim, ...}, ...}
