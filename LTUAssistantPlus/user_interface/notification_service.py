#!/usr/bin/env python3

import platform
from user_interface.notification_service_base import NotificationServiceBase

platform_string = platform.system()

if platform_string == "Linux":
    import notify2 # pylint: disable=import-error
    import dbus    # pylint: disable=import-error
    notify2.init('LTU Assistant')
elif platform_string == "Windows":
    from win10toast import ToastNotifier # pylint: disable=import-error
    toaster = ToastNotifier()

class NotificationService(NotificationServiceBase):
    """Provides notification services."""

    def show_notification(self, message: str, also_cmd: bool = False):
        """Show spoken words from the assistant as a notification."""
        if platform_string == "Linux":
            try:
                notification = notify2.Notification('LTU Assistant',
                                                    message,
                                                    'notification-message-im')
                notification.show()
            except dbus.exceptions.DBusException:
                if not also_cmd:
                    print(message)
        elif platform_string == "Windows":
            toaster.show_toast("LTU Assistant", message, threaded=True)

if __name__ == "__main__":
    service = NotificationService()
    service.show_notification("This is a test notification.")