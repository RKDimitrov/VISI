from plyer import notification

from updater import AppsToUpdates

AppsToUpdates=AppsToUpdates['Windows 10']

notification.notify(
    title='Windows Update',
    message=AppsToUpdates,
    app_name='My App',
    timeout=5000  # 5 seconds
)