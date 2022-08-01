import requests
from police_uk.config import forces_URL

def id_api_call(param=forces_URL):
    """
    id_api_call() is a request method that receive as param an URL string and return a python response object.
    is called by id_list() method to get the id of each force.
    """
    return requests.get(param)

def people_api_call(id):
    """
    people_api_call() is a request method that consumes a valid id string and return a python response object.
    is called by people_Json_list() method to get force's people data.
    """
    return requests.get(forces_URL + '/' + id + '/people')