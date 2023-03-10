import requests
from bs4 import BeautifulSoup
import re

# Scrape the Ubuntu releases page to obtain the latest stable release version
url = 'https://releases.ubuntu.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
latest_version_string = soup.find('a', string=re.compile(r'Ubuntu\s+\d+\.\d+')).text

version_regex = r'Ubuntu\s+(\d+\.\d+)'
match = re.search(version_regex, latest_version_string)
if match:
    latest_version = match.group(1)
    print(f'Latest version is {latest_version}')
else:
    print('Unable to extract version number')

import platform

# Check if the system is running Ubuntu
if platform.system() == 'Linux' and platform.linux_distribution()[0] == 'Ubuntu':
    version = platform.linux_distribution()[1]
    print(f'Ubuntu version is {version}')
else:
    print('This script is meant to run on Ubuntu.')