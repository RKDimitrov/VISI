import pickle
import updater
import interface

AppsToUpdates = updater.AppsToUpdates

def popup():
    print(f"""
    Theres a new update for:
        *Windows 10 - {AppsToUpdates["Windows 10"]}
        
    """)
    pass

def main():
    
    popup()


main()