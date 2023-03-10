import pickle
import updater
import interface
import rooster

AppsToUpdates = updater.AppsToUpdates


    # Load the apps to update
with open("updater.py", "rb") as f:
    apps_to_update = pickle.load(f)

    # Check if there are any updates
if apps_to_update:
        # Create the notification
        
        # Create the rooster
    rooster.create_rooster()
else:
    print("No updates available")

