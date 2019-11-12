# SI 506 2019F - Problem Set 09

# In this problem set you will work with the Star Wars API. We recommend you read through some of the documentation (https://swapi.co/documentation) and reference it as you work through the following problems. You will also want to reference the requests documentation (https://requests.readthedocs.io/en/master/user/quickstart/#quickstart).

# Responses from the Star Wars API may be slow, don't worry if your terminal "hangs" while making and parsing calls to the API.

# START SETUP
import requests
import json
# END SETUP

# PROBLEM 1
# Learning Objectives:
# 1. Make an API call.
# 2. Access text in the response and convert it to a Python object.
# 3. Identify the keys in the Python object.

# Using the requests module make a call to the films endpoint and get the .text,
# use the json module to convert the response into a Python dictionary <films_dict>,
# and assign the keys in the Python object to <films_keys>.

# HINT: You will want to incorporate '.get()', '.text', and '.loads()' in your code.

# BEGIN PROBLEM 1
baseurl = 'https://swapi.co/api/'
films_dict = None
films_keys = None

# BEGIN TEST FOR PROBLEM 1 (Uncomment me when you're ready!)
# print(f"Problem 1 test: {'results' in films_keys}") #should print True
# END TEST FOR PROBLEM 1

# END PROBLEM 1

# PROBLEM 2
# Learning Objectives:
# 1. Explore a data structure via the keys.
# 2. Access keys nested inside a dictionary.
# 3. Practice working with loops.

# Using <films_dict> from above, iterate through the movies contained in ['results'],
# create a 3-tuple containing the movie's title, the movie's episode ID, and a count of the number of characters in that movie.
# Save that 3-tuple to the list <title_id_chars>.

# HINT: you may want to incorporate for loops and a temporary counter variable in your code.

# BEGIN PROBLEM 2
title_id_chars = []


# BEGIN TEST FOR PROBLEM 2 (Uncomment me when you're ready!)
# print(f"Problem 2 test: {sum(count[2] for count in title_id_chars)==173}") #should print True
# END TEST FOR PROBLEM 2

# END PROBLEM 2

# PROBLEM 3
# Learning Objectives:
# 1. Create a function with two parameters for convenient API.

# As you saw in PROBLEM 1, it takes several steps to make an API call and parse the returned data into a dictionary.
# Now combine those steps into a function, named <call_API>, which takes two parameters, <category> is a string
# ("people", "planets", etc. are all different categories), <id> is an integer, indicating the item you're looking for.
# <id> can be None, meaning that no item is specified.
# <call_API> should return a dictionary parsed from the JSON returned by the API.

# HINT:
# call_API(category, id) should call the api with url 'https://swapi.co/api/{category}/{id}/'
# If <id> is None, call_API(category, None) should call the api with url 'https://swapi.co/api/{category}/'.

# BEGIN PROBLEM 3
def call_API(category, id):
    return None


# BEGIN TEST FOR PROBLEM 3 (Uncomment me when you're ready!)
# print(f"Problem 3 test: {call_API('people', 1)['name'] == 'Luke Skywalker'}") #should print True
# END TEST FOR PROBLEM 3

# END PROBLEM 3

# PROBLEM 4
# Learning Objectives:
# 1. Make an API call with more customized parameters (e.g. search).
# 2. Access keys nested inside a dictionary.
# 3. Extract information with a for loop.

# Modern APIs are really powerful. They can take lots of customized parameters
# Using the requests module make a call to "https://swapi.co/api/people/?search=r2-d2"
# Parse the returned JSON into a dictionary <search_dict>
# Extract "name","height","mass","hair_color","skin_color","eye_color","birth_year","gender" from <search_dict>
# and save all these key-value pairs into a new dictionary <r2_d2>.

# BEGIN PROBLEM 4
r2_d2 = {}
search_url = "https://swapi.co/api/people/?search=r2-d2"


# BEGIN TEST FOR PROBLEM 4 (Uncomment me when you're ready!)
# print(f"Problem 4 test: {r2_d2['skin_color'] == 'white, blue'}") #should print True
# END TEST FOR PROBLEM 4

# END PROBLEM 4

# PROBLEM 5
# Learning Objectives:
# 1. Update function based on new requirements.
# 2. Practice with built-in functions like type().
# 3. Practice with conditional statements.

# You may notice the function <call_API> created in PROBLEM 3 can't handle the new requirements in PROBLEM 4.
# Create a new function called <call_API_updated> that can handle all three types of requests:
# type1: 'https://swapi.co/api/films'
# type2: 'https://swapi.co/api/planets/3'
# type3: 'https://swapi.co/api/people/?search=r2_d2'
# Similar to <call_API>, <call_API_updated> also takes two parameters <category> is a string
# ("people", "planets", etc. are all different categories), <option> can be None, an integer, or a string describing something you want to search.

# HINT:
# If <option> is None, <call_API_updated> should call the url 'https://swapi.co/api/{category}'
# If <option> is an integer, <call_API_updated> should call the url 'https://swapi.co/api/{category}/{option}'
# If <option> is a string, <call_API_updated> should call the url 'https://swapi.co/api/{category}/?search={option}'

# BEGIN PROBLEM 5
def call_API_updated(category, option):
    return None


# BEGIN TEST FOR PROBLEM 5 (Uncomment me when you're ready!)
# print(f"Problem 5 test 1: {call_API_updated('people', 1)['name'] == 'Luke Skywalker'}") #should print True
# print(f"Problem 5 test 2: {call_API_updated('people', 'luke')['results'][0]['height'] == '172'}") #should print True
# print(f"Problem 5 test 3: {call_API_updated('species', None)['results'][3]['classification'] == 'amphibian'}") #should print True
# END TEST FOR PROBLEM 5

# END PROBLEM 5

# PROBLEM 6
# Learning Objectives:
# 1. Loop over a list to make function and API calls.
# 2. Access keys nested inside a dictionary.
# 3. Practice with built-in functions like str.split().
# 4. Practice with list indexing.
# 5. Write dictionary into JSON file.

# In this problem, you will reuse the functions created in PROBLEM 3 / PROBLEM 5 to simplify things.
# <search_dict>["results"][0]["films"] contains all the films that R2-D2 appears in.
# Extract the titles of these films into a list and add this list to <r2_d2> with key ["films"].
# Now write the dictionary <r2_d2> into a JSON file called "r2_d2.json".

# HINT:
# Films are given in the format of API url, e.g. "https://swapi.co/api/films/1/".
# You need to extract the <category> and <option> from the url and pass them to the function <call_API_updated>.
# You can use str.split() and list indexing to extract them.
# Don't forget to convert the variable for <option> from str to int!.

# BEGIN PROBLEM 6
films = []


# BEGIN TEST FOR PROBLEM 6 (Uncomment me when you're ready!)
# print(f"Problem 6 test: {r2_d2['films'][0] == 'The Empire Strikes Back'}")
# END TEST FOR PROBLEM 6

# END PROBLEM 6

# END PROBLEM SET 09