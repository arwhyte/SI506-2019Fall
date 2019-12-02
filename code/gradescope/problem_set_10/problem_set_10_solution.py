# SI 506 2019F - Problem Set 109

# In this problem set you will work with the Star Wars API. We recommend you read through some of the documentation (https://swapi.co/documentation) and reference it as you work through the following problems. You will also want to reference the requests documentation (https://requests.readthedocs.io/en/master/user/quickstart/#quickstart).

# Responses from the Star Wars API may be slow, don't worry if your terminal "hangs" while making and parsing calls to the API.

# Read the following block quote ENTIRELY before beginning this assignment.

'''
For this assignment, you will build four utility functions (functions that do one small thing) and a main function
(a function that will execute the main purpose of this script). Outside of testing, you should not need to write
any code that is not contained within one of these functions. Below is a description of each of the functions
that you should write. At the bottom of this block quote you will find the grading rubric for the autograder
of this homework.

----- Functions to Create -----

get_data:
    parameters:
        - baseurl (str)
        - resource (str with default value of "")
        - params (dict with default value of an empty dict {})
    description:
        This function should make a call to an API using the <requests> module. <baseurl> should be the
        base url for the API endpoint, <resource> should be which resource is being called, and <params>
        should be a dictionary of any optional parameters.
    returns:
        This function should return a dictionary that is the result of the API call.
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'


search_swapi:
    parameters:
        - resource (str)
        - query (str)
    description:
        This function should use the "search" functionality of SWAPI to search for the <query> string
        given a <resource>. In other words, you might want to search for a query of "luke" in the
        resource "people/". This function should make a call to <get_data> to accomplish this goal.
    returns:
        This function should return a dictionary that is the result of the query.
    test:
        There are a couple tests provided for you at the bottom of this file. They should return 'True'


get_information_on_characters
    parameters:
        - list_of_characters (list of dictionaries)
    description:
        Given a result set of characters from a SWAPI query, return a nested list
        of the character name, birth year, and species name. In other words, <list_of_characters>
        should be a list structured like the value to the key 'results' from the dictionary that
        is returned from <search_swapi>.
    returns:
        This function should return a nested dictionary in the following form:
        {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' : <name of the species of the character>
                    'homeworld_name' : <name of the homeworld of the character>
                }
            <other character name> :
                {
                    ... etc ...
                }
            ... etc ...
        }
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'


write_json:
    parameters:
        - filename (str)
        - data (json-able object, e.g. nested dictionary or list)
    description:
        Write <data> to the .json file specified by <filename>
    returns:
        This function doesn't return anything.
    test:
        There is no test for this function provided, although you are free and encouraged to test this
        function however you see fit.


main:
    parameters:
        (there are no parameters for <main>)
    description:
        Use <search_swapi>, <get_information_on_characters>, and <write_json> to produce the following
        .json files:

        "darth_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "darth" in their name.

        "skywalker_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "skywalker" in their name.

        "tatooine_residents_info.json": <-- CHALLENGE
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have are residents of "tatooine".
            - HINT: You may want to use your <search_swapi> function with "planets" as the <resource> and
            "tatooine" as the <query> here...and then you'll need to find the URLs of all the characters that
            reside on Tatooine and save their information to a list for <get_information_on_characters> to use.


----- Grading Rubric -----

20 pts: <get_data> works correctly
20 pts: <search_swapi> works correctly and makes a call to <get_data>
20 pts: <get_information_on_characters> works correctly
20 pts: <write_json> works correctly
10 pts: Every function has a docstring
20 pts: "darth_info.json" is correct
20 pts: "skywalker_info.json" is correct
20 pts: "tatooine_residents_info" is correct
---
150 points total
'''

import requests
import json

def get_data(baseurl,resource='',params={}):
    '''
    Make a request to a REST API endpoint, and convert the reponse into a
    python object.

    Required parameters (in this order):
        baseurl: (str) The base URL of the API from which access is desired.

    Optional parameters:
        resource: (str) The resource of the API to be accessed. Default: ''
        params: (dict) Any additional parameters for this API call. Default: {}

    Returns:
        A dictionary of the result of the API call.
    '''

    # Get the response from the REST API endpoint and return it as .json format.
    response = requests.get(baseurl+resource,params=params)
    response_out = response.json()

    # Another method:
    # Convert the string response from the API endpoint to a python object and return it.
    reponse_out = json.loads(response.text)

    return response_out


def search_swapi(resource,query):
    '''
    Make a more specific request of SWAPI to return the results of a query of
    one of the resources available.

    Required parameters (in this order):
        resource: (str) The resource of the API to be searched.
        query: (str) The string to search for in the API resource.

    Returns:
        A dictionary of the result of this query.
    '''
    # Build the proper query dictionary; in this case, a query using the "search" parameter.
    params = {"search":query}

    response = get_data("https://swapi.co/api/",resource+'/',params=params)

    return response


def get_information_on_characters(list_of_characters):
    '''
    Given a result set of characters from a SWAPI query, return a nested list
    of the character name, birth year, and species name.

    Required parameters (in this order):
        list_of_characters: (list) A result list (from value associated with 'result' in the dict from <search_swapi>)

    Returns:
        A nested dictionary that is built according to the following structure:
        {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' : <name of the species of the character>
                    'homeworld_name' : <name of the homeworld of the character
                }
        }
    '''

    out_dict = {}

    for char in list_of_characters:

        name = char['name']
        by = char['birth_year']
        species_name = requests.get(char['species'][0]).json()['name']
        homeworld_name = requests.get(char['homeworld']).json()['name']

        out_dict[name] = {'name':name,'birth_year':by,'species_name':species_name,
                          'homeworld_name':homeworld_name}

    return out_dict


def write_json(filename,data):
    '''
    Write a nested dictionary/list python object to a json file.

    Required parameters (in this order):
        filename: (str) File in which to write the json data.
        data: (dict/list) Nested object to write into a json file.

    Returns:
        None
    '''

    with open(filename,'w') as f:
        json.dump(data,f,indent=2)

def main():
    '''
    Main portion of the code. Compile information on a variety of characters and
    create 3 json files using the other functions written in this code.

    Parameters:
        None

    Returns:
        None
    '''

    # Get the query results for all people named "skywalker" and write info to json
    skywalker = search_swapi('people','skywalker')
    skywalker_info = get_information_on_characters(skywalker['results'])
    write_json('skywalker_info.json',skywalker_info)

    # Get the query results for all people named "darth" and writ info to json
    darth = search_swapi('people','darth')
    darth_info = get_information_on_characters(darth['results'])
    write_json('darth_info.json',darth_info)

    # Get the query results for the planet "tatooine"
    tatooine = search_swapi('planets','tatooine')

    # Create a list of characters for <get_information_on_characters> to ingest.
    tatooine_residents = []
    tatooine_results = tatooine['results'][0] # don't forget the 0th element, the resultset is a list!

    for char_url in tatooine_results['residents']:
        tatooine_residents.append(requests.get(char_url).json())

    tatooine_residents_info = get_information_on_characters(tatooine_residents)
    write_json('tatooine_residents_info.json',tatooine_residents_info)


# DO NOT MODIFY ANYTHING BELOW THIS LINE!

# The below code will call the <main> function you wrote so long as you are running this
# code directly (as opposed to importing it in another python script).
if __name__ == '__main__':
    #main()

    # test for <get_data>
    test1 = get_data('https://swapi.co/api/',resource='people',params={'search':'yoda'})['results'][0]['mass']=='17'
    print(f"\nTest for <get_data>: {test1}")

    # tests for <search_swapi>
    #test2 = search_swapi('people','yoda')['results'][0]['mass']=='17'
    #test3 = search_swapi('starships','tie')['results'][0]['crew']=='1'
    #print(f"\nTest #1 for <search_swapi>: {test2}")
    #print(f"Test #2 for <search_swapi>: {test3}")

    # test for <get_information_on_characters>
    #test4 = get_information_on_characters(search_swapi('people','skywalker')['results'])['Shmi Skywalker']['birth_year']=='72BBY'
    #print(f"\nTest for <get_information_on_characters>: {test4}")

# END PROBLEM SET 10
