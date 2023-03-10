import os
import requests
from bs4 import BeautifulSoup
import json
import re

def check_vscode_version():
    # Get the current version of Visual Studio Code installed on your system
    product_json_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Programs', 'Microsoft VS Code', 'resources', 'app', 'product.json')
    with open(product_json_path, 'r') as f:
        data = json.load(f)
        installed_version = data['version']

    # Scrape the Visual Studio Code releases page to obtain the latest stable release version
    url = 'https://code.visualstudio.com/updates/v1_76'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_version_string = soup.find('strong', string=re.compile(r'Update \d+(\.\d+)*')).text

    version_regex = r"Update (\d+\.\d+\.\d+)"
    match = re.search(version_regex, latest_version_string)
    if match:
        latest_version = match.group(1)
        print(f'Latest version is {latest_version}')
    else:
        print('Unable to extract version number')

    # Compare the two versions and determine if the installed version is up to date
    if installed_version == latest_version:
        return ('Visual Studio Code is up to date.', True)
    else:
        return (f'Visual Studio Code is not up to date. Installed version is {installed_version}. Latest version is {latest_version}.', False)