import pickle
import updater
import interface
import notification

AppsToUpdates = updater.AppsToUpdates

def main():
    print(f"""
    Theres a new update for:
        *Windows 10 - {AppsToUpdates["Windows 10"]}
        *VS-Code - {AppsToUpdates["VS-Code"]}
        *Chrome - {AppsToUpdates["Chrome"]}
        
    """)

main()