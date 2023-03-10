import platform

# Get the Windows version
windows_version = platform.win32_ver()

# Print the version information
print(windows_version)

# Check if the version is up to date
if "10.0" in windows_version[0]:
    print("Your version of Windows 10 is up to date.")
else:
    print("Your version of Windows is not supported.")
