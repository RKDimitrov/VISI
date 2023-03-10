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

