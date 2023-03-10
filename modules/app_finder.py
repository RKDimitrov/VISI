import os
# Get the operating system
import platform
import time

print(platform.system())

def search_file_on_windows(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return None
    

def search_file_on_ubuntu(filename):
    for root, dirs, files in os.walk("/"):
        for file in files:
            if filename in file:
                return os.path.join(root, file)
    return None
    

def search_file_on_mac(filename):
    for root, dirs, files in os.walk("/"):
        for file in files:
            if filename in file:
                return os.path.join(root, file)
    return None


def Os_type():

    if platform.system() == "Windows": 
        return 1
    elif platform.system() == "Linux":
        return 2
    elif platform.system() == "Darwin":
        return 3



# Print different messages based on the OS
import platform

# Get the Windows version
windows_version = platform.win32_ver()

# Print the version information
print(windows_version)

import win32com.client

# Connect to the Windows Update service
wu = win32com.client.Dispatch("Microsoft.Update.Session")

# Search for available updates
search_result = wu.CreateUpdateSearcher().Search("IsInstalled=0")

# Check if any updates are available
if search_result.Updates.Count == 0:
    print("Your version of Windows is up to date.")
else:
    print("Updates are available for your version of Windows.")
