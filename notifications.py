#!/usr/bin/env python3

import notify2
import dbus

notify2.init('LTU Assistant')

def show_notification(message, also_cmd=False):
    '''Show spoken words from the assistant as a notification.'''
    try:
        notification = notify2.Notification('LTU Assistant',
                                            message,
                                            'notification-message-im')
        notification.show()
    except dbus.exceptions.DBusException:
        if not also_cmd:
            print(message)