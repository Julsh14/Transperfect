from assertpy import assert_that
from herokuapp.config import credentials
from herokuapp.herokuapp_api import basic_Auth_login, file_upload

def test_basic_Auth_login():
    """Test if id_api_call() is requesting correctly. Receives url in string format as parameter."""
    response = basic_Auth_login(credentials)
    assert_that(response.status_code).is_equal_to(200)

def test_file_upload():
    """Test if file_upload() is requesting correctly."""
    response = file_upload()
    assert_that(response.status_code).is_equal_to(200)
