import requests
from bs4 import BeautifulSoup

# Send a GET request to the Windows 10 update page
def windows_update():
    url = 'https://support.microsoft.com/en-us/topic/february-21-2023-kb5022906-os-builds-19042-2673-19044-2673-and-19045-2673-preview-bf72fc27-6222-4f6a-991a-f472b3f9d3fd'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    windows_update= soup.find('h1', id='page-header').text

    return windows_update

#def vs_code_update():
    url = 'https://code.visualstudio.com/updates/v1_56'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    vs_code_update = soup.find('h1', id='col-sm-9 col-md-8 body').text

    return vs_code_update


AppsToUpdates = {
    "Windows 10": "{}".format(windows_update()),
    #"VS-Code": "{}".format(vs_code_update()),
    "Chrome": "https://chromereleases.googleblog.com/2021/02/stable-channel-update-for-desktop_23.html",
}


# Find the link for the latest update



# Print the link
print(windows_update)