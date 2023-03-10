import os

def search_file_on_windows(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return None


key = "hui"
#Finding out if hui.exe exists using th above function 
if None != search_file_on_windows(str(key)+".exe"):
    print("hui.exe exists")
