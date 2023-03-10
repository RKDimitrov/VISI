import requests
from bs4 import BeautifulSoup
import re
import platform

def get_installed_ubuntu_version():
    # Check if the system is running Ubuntu
    if platform.system() == 'Linux' and platform.linux_distribution()[0] == 'Ubuntu':
        version = platform.linux_distribution()[1]
        return version
    else:
        return None

def get_latest_ubuntu_version():
    # Scrape the Ubuntu releases page to obtain the latest stable release version
    url = 'https://releases.ubuntu.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_version_string = soup.find('a', string=re.compile(r'Ubuntu\s+\d+\.\d+')).text

    version_regex = r'Ubuntu\s+(\d+\.\d+)'
    match = re.search(version_regex, latest_version_string)
    if match:
        latest_version = match.group(1)

        if (get_installed_ubuntu_version() == latest_version):
            return (f'Ubuntu is up to date. Installed version is {latest_version}.', True)
        else:
            return (f'Ubuntu is not up to date. Installed version is {get_installed_ubuntu_version()}. Latest version is {latest_version}.', False)
    else:
        return None

