import pickle
from modules import updater
from modules import notification
from modules import interface
from modules import rooster

AppsToUpdates = updater.AppsToUpdates

def main():
    print(f"""
    Theres a new update for:
        *Windows 10 - {AppsToUpdates["Windows 10"]}
        *VS-Code - {AppsToUpdates["VS-Code"]}
        *Chrome - {AppsToUpdates["Chrome"]}
        
    """)

main()