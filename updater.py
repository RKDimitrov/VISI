import requests
from bs4 import BeautifulSoup
import time
import croniter

cron = croniter.croniter('*/30 * * * *', time.time())

def windows_update():
    id = 0
    url = 'https://support.microsoft.com/en-us/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562'
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    current_version = soup.find('a', {'data-bi-slot': '3'}).text
    print("Current version:", current_version)

    return windows_update, url

def vs_code_update():
    id = 1
    url = 'https://code.visualstudio.com/updates'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    active_li = soup.findAll('li', {'class':'active'})

    a_active = active_li[1].find('a')
    href_value = a_active.get('href')


    return href_value, url


AppsToUpdates = {
    "Windows 10": "{}".format(windows_update()),
    "VS-Code": "https://code.visualstudio.com{}".format(vs_code_update()),
    "Chrome": "https://chromereleases.googleblog.com/2021/02/stable-channel-update-for-desktop_23.html",
}