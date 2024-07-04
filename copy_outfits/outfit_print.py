#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from copy_outfits.enums.copy_outfits_age import CopyOutfitsAge
from copy_outfits.modinfo import ModInfo
from copy_outfits.persist.outfit_store import OutfitStore
from copy_outfits.persist.sim_store import SimStore
from copy_outfits.utils.outit_notifications import OutfitNotifications
from ts4lib.utils.singleton import Singleton
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitPrint')
log.enable()


class OutfitPrint(metaclass=Singleton):
    @staticmethod
    def print_outfit_details():
        log.debug(f"Sims: {SimStore.sims}")
        log.debug(f"Sources: {OutfitStore.sources}")
        log.debug(f"Outfits: {OutfitStore.outfits}")

        for _sim_age, clipboard_data in OutfitStore.outfits.items():
            if clipboard_data:
                msg = f"{CopyOutfitsAge(_sim_age).name}:"
                for clipboard_index, parts in clipboard_data.items():
                    source = OutfitStore.sources.get(_sim_age).get(clipboard_index)
                    msg = f"{msg} (#{clipboard_index}: {source})"
                log.debug(f"UI Notification: '{msg}'")
                OutfitNotifications().show_notification(msg)
                