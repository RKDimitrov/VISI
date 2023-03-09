import pickle
import updater

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