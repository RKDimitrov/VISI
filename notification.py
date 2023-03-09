from plyer import notification
import updater
from updater import AppsToUpdates

AppsToUpdates=AppsToUpdates['Windows 10']

notification.notify(
    title='Notification Title',
    message='Notification Message',
    title='Windows Update',
    message=AppsToUpdates,
    app_name='My App',
    timeout=5000  # 5 seconds
)