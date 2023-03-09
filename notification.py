from plyer import notification
from threading import Thread
import time
import interface

def on_notification_click():
    interface.overAllFunction()
    print("Notification clicked!")

def notification_listener():
    while True:
        # check if a notification has been clicked
        if notification.is_sticky():
            on_notification_click()
        time.sleep(1)

AppsToUpdates = {'Windows 10': 'Update available!'}
notification.notify(
    title='Windows Update',
    message=AppsToUpdates['Windows 10'],
    app_name='My App',
    timeout=5000,  # 5 seconds
    app_icon=None,  # set to None to use the default icon
    toast=False,  # set to False to use non-toast notification on Windows 10
    ticker='',  # set to an empty string to hide ticker on Android
)

listener_thread = Thread(target=notification_listener)
listener_thread.start()
