from police_uk.config import senior_ranks
from police_uk.police_api import id_api_call, people_api_call
"""
This script contains the necessary methods to get data from all senior officers of each police force.
"""

def id_list():
    """
    PURPOSE:
    id_list() is a method that consumes id_api_call() which provides the id of all police forces. Each id means the
    location of the corresponding force. The method transforms the python response object into a json structure and
    creates a list by getting all ids in the json file.

    RETURN:
    list: id_list of all forces.
    """
    response = id_api_call()
    response_json = response.json()
    id_list = [id['id']for id in response_json]
    return id_list

def people_json_list():
    """
    PURPOSE:
    The people_json_list() method calls id_list() method to get a complete id list and also creates an empty list.
    Secondly gets all people police force data by iterating the id list and requesting people data for each id by
    calling people_api_call() method. It also transform python response object to json structure and insert in the empty
    list.Finally filters empty response and return a list that contain people data in dictionarie format.

    RETURN:
    list: json_list contains all people forces data
    """
    list = id_list()
    json_list = []
    for id in list:
        response = people_api_call(id)
        response_json = response.json()
        if response_json != []:
            json_list.append(response_json)
        else:
            pass
    return json_list

def senior_officers():
    """
        PURPOSE:
        senior_officers() method calls people_json_list() method to get all people police force data and also creates
        an empty list. Secondly iterates twice people json list to get each value for rank key and compare the data with
        senior rank list to find out if the person is senior.

        RETURN:
        json: senior_officer contains (if available) all senior officers Name, Rank , bio and contact.
        """
    people_list = people_json_list()
    senior_officers = []
    for json in people_list:
        for key in json:
            if key['rank'] in senior_ranks:
                senior_officers.append(key)
            else:
                pass
    return senior_officers
print(senior_officers())