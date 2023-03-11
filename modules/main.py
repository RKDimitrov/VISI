import os
import tkinter as tk
import customtkinter as CTk
import subprocess
import threading
import win32com.client
from PIL import Image, ImageTk, ImageEnhance
import time
import croniter

# Modules
import VSCodeUpToDater
import windowsUpToDate
import ubuntuUpToDater
import rooster

# Global variables
update_time = 60 #30 minutes

def updateCheck():
    while True:
        if (VSCodeUpToDater.check_vscode_version()[1] == False) and (windowsUpToDate.check_windows_update()[1] == False) and (ubuntuUpToDater.check_ubuntu_updates()[1] == False):
            print("No updates needed")
        else:
            print("Needs update")
            subprocess.run(["python", "rooster.py"])
            time.sleep(update_time)
        
def main():
    updateCheck()
        

if __name__ == "__main__":
    main()

