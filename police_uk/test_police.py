from assertpy import assert_that
import random
from police_uk.config import forces_URL
from police_uk.police import id_list, people_json_list, senior_officers
from police_uk.police_api import id_api_call, people_api_call

def test_id_api_call(param=forces_URL):
    """Test if id_api_call() is requesting correctly. Receives url in string format as parameter."""
    response = id_api_call(param)
    assert_that(response.status_code).is_equal_to(200)

def test_id_list():
    """Test if id_list() first element is 'avon-and-somerset'."""
    list = id_list()
    assert_that(list[0]).is_equal_to('avon-and-somerset')

def test_people_api_call():
    """Gets the id list and tests if people_api_call() is requesting correctly using an id from that list given at random."""
    list = id_list()
    random_item = random.choice(list)
    response = people_api_call(random_item)
    assert_that(response.status_code).is_equal_to(200)

def test_people_json_list():
    """Test if people_json_list() returns a list element type"""
    json_list = people_json_list()
    assert_that(json_list)._type(list)

def test_senior_officers():
    """Test if senior_list() returns a json element type"""
    senior_officers_json = senior_officers()
    assert_that(senior_officers_json)._type(dict)
