import os
import requests
from bs4 import BeautifulSoup
import json
import re

def check_epic_games_version():
    # Get the current version of Epic Games Launcher installed on your system
    app_json_path = os.path.join(os.getenv('LOCALAPPDATA'), 'EpicGamesLauncher', 'Saved', 'Logs', 'app.log')
    with open(app_json_path, 'r') as f:
        data = f.readlines()
        for line in reversed(data):
            if "App Version:" in line:
                installed_version = line.split("App Version:")[1].strip()
                break
            
    check_epic_games_version()

    # Scrape the Epic Games Launcher releases page to obtain the latest stable release version
    url = 'https://www.epicgames.com/store/en-US/download'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_version_string = soup.find('span', {'class': 'css-1vjzyv4'}).text.strip()

    version_regex = r"(\d+\.\d+\.\d+)"
    match = re.search(version_regex, latest_version_string)
    if match:
        latest_version = match.group(1)
        print(f'Latest version is {latest_version}')
    else:
        print('Unable to extract version number')



    # Compare the two versions and determine if the installed version is up to date
    if installed_version == latest_version:
        return ('Epic Games Launcher is up to date.')
    else:
        return (f'Epic Games Launcher is not up to date. Installed version is {installed_version}. Latest version is {latest_version}.')
