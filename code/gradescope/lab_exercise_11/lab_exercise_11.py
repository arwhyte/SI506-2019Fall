# SI 506 2019F - Lab 11
# START LAB EXERCISE 11

import json
import os
import requests

# In this lab exercise, you will practice writing Docstrings and work closely with JSON, requests and the
# HTTP GET method in the following three problems

# If a problem includes a setup section: Do not modify, delete or otherwise ignore the setup code.

# You will save results to required variables. These variables will be graded by the auto grader
# after your submission.

# Print statements have been provided for you to debug the code. You can uncomment them to print
# values to the screen.

"""
This is a Docstring. A Docstring describes the functionality of the corresponding function

A Docstring usually consists of three parts:

- function summary

- Parameters:
    arg_1 (type): description
    arg_2 (type): description

- Returns:
    type: description or None

"""

# We provide a function <write_json> with its docstring to help you get familiar with docstrings
# You will use <write_json> later in this lab exercise
def write_json(filepath, data):
    """
    Write a dictionary to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


FILE_PATH = os.path.dirname(os.path.abspath(__file__))  # Windows friendly
ENDPOINT = "https://swapi.co/api"

# PROBLEM 1 (5 Points for docstring)

# In this problem you will demonstrate your understanding of:
# 1) describing functions with docstrings
# 2) working with the requests module


# BEGIN PROBLEM 1 SOLUTION
# We provide you with a function <get_films> taking two arguments: <url> a string and <params> a dictionary
# <get_films> returns a list of films retrieved from the given <url> and <params>
# You need to complete its docstring so your coworkers can quickly learn how to use this function

def get_films(url, params=None):
    """
    TODO: write the Docstring


    """
    films = requests.get(url, params).json()["results"]

    return films

# END PROBLEM 1 SOLUTION

# PROBLEM 2 (5 Points for docstring, 5 Points for code)
# In this problem, you will demonstrate your understanding of
# 1) working with conditional statements
# 2) working with dictionaries
# 3) working with for loops

# Write a function <filter_properties> that accepts a single argument: <film> a dictionary containing properties of the film,
# <filter_properties> extracts properties listed in <FILM_PROPERTIES> of the given <film> and
# returns a dictionary containing corresponding key-value pairs

# Sample Input:
# {
#     "title": "A New Hope",
#     "episode_id": 4,
#     "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
#     "director": "George Lucas",
#     "producer": "Gary Kurtz, Rick McCallum",
#     "release_date": "1977-05-25",
#     "characters": [
#       ...
#     ],
#     "planets": [
#       ...
#     ],
#     "starships": [
#       ...
#     ],
#     "vehicles": [
#       ...
#     ],
#     "species": [
#       ...
#     ],
#     "created": "2014-12-10T14:23:31.880000Z",
#     "edited": "2015-04-11T09:46:52.774897Z",
#     "url": "https://swapi.co/api/films/1/"
# }

# Sample Output
# {
#     "title": "A New Hope",
#     "episode_id": 4,
#     "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
#     "director": "George Lucas",
#     "producer": "Gary Kurtz, Rick McCallum",
#     "release_date": "1977-05-25",
#     "url": "https://swapi.co/api/films/1/"
# }


# BEGIN PROBLEM 2 SOLUTION
FILM_PROPERTIES = ("title", "episode_id", "opening_crawl", "director", "producer","release_date", "url")


def filter_properties(film):
    """
    TODO: write the Docstring



    """
    record = {}
    # START: WRITE CODE BELOW
    # Extracts properties listed in <FILM_PROPERTIES> of <film> and stores them into <record>


    # END: WRITE CODE ABOVE
    return record

# END PROBLEM 2 SOLUTION

# PROBLEM 3 (5 Points for docstring, 5 Points for code)
# In this problem, you will demonstrate your understanding of
# 1) getting a response with requests module
# 2) writing a JSON file
# 3) working with for loops
# 4) working with lists

# Write a function <main>
# <main> first gets a list of films,
# then gets records for each film and stores them in a new list,
# and finally writes the new list into a JSON file

# BEGIN PROBLEM 3 SOLUTION
def main():
    """
    Complete the docstring


    """
    # Get films
    url = f"{ENDPOINT}/films/"
    films = get_films(url)
    new_film_records = []

    # START: WRITE CODE BELOW
    # Use function <filter_properties> to get a record of each film listed in <films>
    # and store them in <new_film_records>

    # END: WRITE CODE ABOVE

    # Write to file
    filename = os.path.join(FILE_PATH, "swapi_films.json")  # Windows friendly
    write_json(filename, new_film_records)


if __name__ == '__main__':
    main()

# END LAB EXERCISE
