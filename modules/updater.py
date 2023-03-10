import requests
from bs4 import BeautifulSoup
import time
import croniter

cron = croniter.croniter('*/30 * * * *', time.time())

def windows_update():
    url = 'https://support.microsoft.com/en-us/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562'
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    current_version = soup.find('a', {'data-bi-slot': '3'}).text
    

    return windows_update, url

def ubuntu_update():
    url = 'https://ubuntu.com/download/desktop/thank-you?version='
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    current_version = str(soup.find('a', {'data-bi-slot': '3'}))

    return current_version, url


def vs_code_update():
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
    "Ubuntu": "{}".format(ubuntu_update()),
}

url_values = {
    "0": windows_update()[1],
    "3": vs_code_update()[1],
}