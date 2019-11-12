# SI 506 2019F - Lab 10
# START LAB EXERCISE 10

# The following 4 problems will introduce you to working with the requests module, the HTTP GET
# method, and JSON.

# If a problem includes a setup section: Do not modify, delete or otherwise ignore the setup code.

# You will save results to required variables. These variables will be graded by the auto grader
# after your submission.

# Print statements have been provided for you to debug the code. You can uncomment them to print
# values to the screen.

# PROBLEM 1 (5 Points)

# In this problem you will demonstrate your understanding of

# 1) working with the requests module
# 2) issuing an HTTP GET request to retrieve data from a RESTful API.

# PROBLEM 01 SETUP
# We provide you with import statements and a resource URI.

import json
import requests

resource_uri = 'https://swapi.co/api/people/4/'

# PROBLEM 01 END SETUP

# BEGIN PROBLEM 1 SOLUTION

# Call requests.get() to request a representation of the resource.
# Arguments: resource URI and the optional params={"search": "darth vader"}
# Decode the response as JSON.
# Save the data to a variable named response
# Hint: Use .json()

vader = None
# print(vader)

# The response variable should be assigned the following dictionary:
"""{
  'count': 1,
  'next': None,
  'previous': None,
  'results': [{
    'name': 'Darth Vader',
    'height': '202',
    'mass': '136',
    'hair_color': 'none',
    'skin_color': 'white',
    'eye_color': 'yellow',
    'birth_year': '41.9BBY',
    'gender': 'male',
    'homeworld': 'https://swapi.co/api/planets/1/',
    'films': [
      'https://swapi.co/api/films/2/',
      'https://swapi.co/api/films/6/',
      'https://swapi.co/api/films/3/',
      'https://swapi.co/api/films/1/'
    ],
    'species': [
      'https://swapi.co/api/species/1/'
    ],
    'vehicles': [],
    'starships': [
      'https://swapi.co/api/starships/13/'
    ],
    'created': '2014-12-10T15:18:20.704000Z',
    'edited': '2014-12-20T21:17:50.313000Z',
    'url': 'https://swapi.co/api/people/4/'
  }]
}
"""

# END PROBLEM 1 SOLUTION

# PROBLEM 2 (5 Points)
# In this problem, you will demonstrate your understanding of
# 1) working with lists
# 2) working with dictionaries

# BEGIN PROBLEM 2 SOLUTION
# Assign Vader's eye color to a variable named eye_color.

eye_color = None

# print(eye_color)

# END PROBLEM 2 SOLUTION

# PROBLEM 3 (5 Points)
# In this problem, you will demonstrate your understanding of
# 1) working with dictionaries
# 2) working with lists

# BEGIN PROBLEM 3 SOLUTION
# Assign the film "https://swapi.co/api/films/3/" to a variable named film.

film = None

# print(film)

# END PROBLEM 3 SOLUTION

# PROBLEM 4 (10 Points)
# In this problem you will demonstrate your understanding of how to
# write a function
# work with the json module to write a dictionary to a file as JSON.

# PROBLEM 04 SETUP
# We provide you with a variable named filename.

filename = 'darth_vader.json'

# PROBLEM 04 END SETUP

# BEGIN PROBLEM 4 SOLUTION
# Create a function named write_json(filename) that accepts a filename string and the vader dict.
# Use the with statement and built-in open() function along with json.dump() to write
# the dictionary to the file darth_vader.json as JSON.
# Call write_json(filename)

# Special instructions
# Set open() optional encoding parameter to 'utf8'
# Set json.dump() ensure_ascii optional parameter to 'False' and optional indent parameter to 2.


def write_json(filename, data):
    pass



write_json(filename, vader)

# END PROBLEM 4 SOLUTION

# END LAB EXERCISE
