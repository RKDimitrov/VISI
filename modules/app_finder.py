import platform

# Get the operating system
os = platform.system()

# Print different messages based on the OS
if os == 'Windows':
    print('You are running Windows')
elif os == 'Linux':
    print('You are running Linux')
elif os == 'Darwin':
    print('You are running macOS')
else:
    print('Unknown operating system')
