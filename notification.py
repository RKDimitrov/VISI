from winotify import Notification
import interface
import os, sys

def on_notification_clicked(notification):
    print("Notification clicked!")

notification = Notification(
    app_id="my_app_id",
    title="Notification Title",
    msg="Notification Message"
)

notification.add_actions(label="ghj", launch=f"{os.getcwd()}\interface.py")

notification.show()
