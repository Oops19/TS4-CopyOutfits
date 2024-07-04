#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from copy_outfits.modinfo import ModInfo
from copy_outfits.struct.internal_stbl import InternalSTBL
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from ts4lib.utils.singleton import Singleton
from ui.ui_dialog_notification import UiDialogNotification


class OutfitNotifications(object, metaclass=Singleton):
    @staticmethod
    def show_notification(message, urgency=UiDialogNotification.UiDialogNotificationUrgency.DEFAULT):
        """
        :param message: The text to print
        :param urgency: UiDialogNotification.UiDialogNotificationUrgency.URGENT = orange box
        :return:
        """
        mod_identifier = ModInfo.get_identity().name
        basic_notification = CommonBasicNotification(
            InternalSTBL.TS4_STRING,  # '{0.String}'
            InternalSTBL.TS4_STRING,  # '{0.String}'
            title_tokens=(mod_identifier,),  # 'Copy Outfits'
            description_tokens=(message.replace('{', '[').replace('}', ']'),),  # 0.String has no variables. Parsing `{'Dict': 123}` fails!
            urgency=urgency
        )
        basic_notification.show()
