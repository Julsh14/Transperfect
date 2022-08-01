import webbrowser
import requests
from bs4 import BeautifulSoup
from herokuapp.config import basic_auth, credentials, upload, file_path, picture, file_name, shifting_content, home

def basic_Auth_login(credentials):
    """ Step 1 the program gets credentials and Log in using Basic Auth."""
    URL = basic_auth
    r1 = requests.get(URL, auth=credentials)
    return r1
basic_Auth_login(credentials)

def file_upload():
    """ Step 2 the program open a picture file with open method and post it in File Upload URL. """
    URL = upload
    myfile = {'file': open(file_path, 'rb')}
    r2 = requests.post(URL, files=myfile)
    return r2

file_upload()

def file_download():
    """Step 3 the program Download the uploaded file in previous step requesting Secure File Download URL.
    finally open the file and save it in content format (bytes)."""
    URL = picture
    r3 = requests.get(URL)
    with open(file_name, 'wb') as f:
        download_file = f.write(r3.content)
    return download_file
file_download()

def open_shifting_content():
    """
    Step 4 The program request Shifting Content URL and retrives three links from response. Then iterates the response
    and insert in an empty list. Finally iterates one more time and open the URLS with webbrowser open method.
    """
    URL = shifting_content
    r4 = requests.get(URL)
    soup = BeautifulSoup(r4.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    for element in urls[1:4]:
        webbrowser.open(home + element)
open_shifting_content()