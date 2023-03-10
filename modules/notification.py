from winotify import Notification

import os, sys
from updater import AppsToUpdates

APPSTOUPDATE=AppsToUpdates['Windows 10']

def on_notification_clicked(notification):
    print("Notification clicked!")

notification = Notification(
    app_id="VISI",
    title="New Update Available",
    msg=APPSTOUPDATE
)

notification.add_actions(label="Open App", launch=f"{os.getcwd()}\interface.py")

notification.show()
