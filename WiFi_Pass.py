import subprocess

# Get all Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

# Loop through profiles to get passwords
for profile in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    password = [line.split(":", 1)[1].strip() for line in result if "Key Content" in line]
    
    try:
        print("{:<30} | {:<}".format(profile, password[0]))
    except IndexError:
        print("{:<30} | {:<}".format(profile, "No password found or access denied"))
        
# This script retrieves and displays saved Wi-Fi profiles and their passwords on a Windows machine.
# Note: This script requires administrative privileges to run successfully.