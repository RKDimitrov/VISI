import os
# Get the operating system

def search_file_on_windows(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Example usage
game_exe_path = search_file_on_windows("hui.exe")
if game_exe_path is not None:
    print("Game is installed at:", game_exe_path)
else:
    print("Game is not installed.")

# Print different messages based on the OS
