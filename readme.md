#Project Name
"transperfect_challenge"

#Installation
1 install python 3.9 or higher https://www.python.org/downloads/
2 after clone the repo from github go to /transperfect in your local dir and run: "pip install -r requirements.txt" to set dependencies.  

#Test 1 Name
"herokuapp"

#Description
The purpose of the project is to interact with "http://the-internet.herokuapp.com" webpage. 
The program contains certain methods that allows the user post and get data through requests module. 
The basic_auth_login method pass to the webpage the credentials required to make a successful login to at 'https://the-internet.herokuapp.com/basic_auth' 
File_upload and file_download methods Upload and download respectively a given image selected by the user. please specify the image path and name before run.
open_shifting_content method make an API call and gets a web element's list for the indicated URL address. Then creates a web element list and automatically open the links witch are include in it.

#Run
1 Set file_name and file_path correctly in config.py before run.
2 go to /transperfect/herokuapp and run te command: "pytest test_herokuapp.py" to execute tests.

#Test 2 Name
"Police uk"

#Description
The purpose of the project is to provide an automated test suite for https://data.police.uk webpage. 
The program contains:
API requests methods to get police data in requests.py
Certain methods that transform data taken from requests and retriever processed senior officer's information in police_uk.py
A module that contain the suite case test_police_uk.py

#Run
1 go to /transperfect/police_uk and run te command: "pytest test_herokuapp.py" to execute tests.


