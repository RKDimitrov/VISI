from winotify import Notification
import interface
import os, sys
from updater import AppsToUpdates

APPSTOUPDATE=AppsToUpdates['Windows 10']

def on_notification_clicked(notification):
    print("Notification clicked!")

notification = Notification(
    app_id="VISI",
    title="NEW UPDATE AVAILABLE",
    msg=APPSTOUPDATE
)

notification.add_actions(label="GO APP", launch=f"{os.getcwd()}\interface.py")

notification.show()
