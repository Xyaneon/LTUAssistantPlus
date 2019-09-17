#!/usr/bin/env python3

import platform

platform_string = platform.system()

if platform_string == "Linux":
    import notify2
    import dbus
    notify2.init('LTU Assistant')
elif platform_string == "Windows":
    from win10toast import ToastNotifier
    toaster = ToastNotifier()

def show_notification(message, also_cmd=False):
    '''Show spoken words from the assistant as a notification.'''
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
    show_notification("LTU Assistant", "This is a test notification.")