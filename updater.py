import requests
from bs4 import BeautifulSoup

# Send a GET request to the Windows 10 update page
def windows_update():
    url = 'https://support.microsoft.com/en-us/topic/february-21-2023-kb5022906-os-builds-19042-2673-19044-2673-and-19045-2673-preview-bf72fc27-6222-4f6a-991a-f472b3f9d3fd'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    windows_update= soup.find('a', {'data-bi-slot': '3'}).text

    return windows_update

def vs_code_update():
    url = 'https://code.visualstudio.com/updates'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    active_li = soup.findAll('li', {'class':'active'})

    a_active = active_li[1].find('a')
    href_value = a_active.get('href')


    return href_value


AppsToUpdates = {
    "Windows 10": "{}".format(windows_update()),
    "VS-Code": "https://code.visualstudio.com{}".format(vs_code_update()),
    "Chrome": "https://chromereleases.googleblog.com/2021/02/stable-channel-update-for-desktop_23.html",
}