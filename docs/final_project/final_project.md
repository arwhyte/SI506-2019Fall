# SI 506 Final Project Assignment

## Star Wars API (SWAPI)

### Release Date: Tuesday, 26 November 2019, 4:00 PM
### Due Date: Monday, 16 December, 11:59 PM

:exclamation: The final two lab exercises and problem sets are designed to introduce you to
the STARS WARS API (SWAPI) and its resources. These assignments will help prepare you for the final 
project assignment which will be based on SWAPI. Final details regarding final project 
deliverables and scoring will be released on Tuesday, 26 November 2019. This will give you 20 days
to complete and submit the assignment. We reckon that the assignment itself should take no more 
than five to seven days of part-time effort to complete. 

## 1.0 The mission
Rebel Alliance Intelligence has begun receiving a series of secure data transmissions masked as 
random communications traffic. The fragmented message stream is designed to evade Imperial 
communications eavesdropping. Once the transmission has been completed and decoded you will be 
tasked with writing a Python script that will perform the following tasks:

* retrieve the data from a remote server
* combine, filter, and transform the data per a follow up set of instructions
* encode the transformed data as JSON
* write the JSON data to one or more output files 

Final instructions will be provided on Tuesday, 26 November 2019. You will then have 20 days to 
complete the mission.

:warning: Do not install the Python SWAPI module to communicate with the SWAPI Star Wars API. Your 
script must do all the work itself.

## 2.0 Template file
The teaching team will provide you with a final assignment Python file (the template) that provides a 
skeletal implementation of the script you are to write. The template will include minimal 
documentation. Look instead to updates to this document for the list of deliverables you must 
provide. 

Below is a draft version of the template file. It is likely to evolve in small ways before it's final 
release on Tuesday, 26 November, 2019.

```python
import json
import requests


def main():
    pass


def get_resource(resource_uri, params=None):
    pass


# TODO Define additional functions


def write_json(filename, data):
    pass


if __name__ == '__main__':
    main()
```

## 3.0 Scoring rubric (2500 points)
The final assignment is worth 2500 points. The points are allocated as follows:

### 3.1 Get the data (250 points)
Write a general purpose function named `get_resource()` that leverages the `requests` 
module to retrieve SWAPI resources using the HTTP GET method. The function must be capable of 
processing a resource URI (e.g., URL) and any optional querystring parameters passed to it as 
arguments.

#### 3.1.1 Additional requirements
SWAPI data is serialized as JSON.  The `get_resource()` function must decode the response using the 
`.json()` method so that the data is returned as a dictionary. 


### 3.2 main() function (250 points)
The script _must_ include a `main()` function that serves as the entry point to the script. Define 
the data processing workflow in `main()`. Delegate sub-tasks to other functions. Call these 
ancillary functions from `main()` or, when appropriate, from other functions as needed.  


### 3.3 Combine, filter, and transform the data (1500 points)
Write a set of functions that contain the logic necessary to perform the tasks required to combine,
filter, and transform the SWAPI data as required by the 26 November 2019 set of instructions.


### 3.4 Write data to files (250 points)
Write a general purpose function named `write_json()` capable of writing SWAPI data to a 
target JSON document file. The function must be capable of processing any arbitrary combination of 
SWAPI data and filename provided to it as arguments.

Call this function and pass it the appropriate arguments whenever you need to generate a
JSON document file required to complete the assignment.

#### 3.4.1 Additional Requirements
When calling the built-in `open()` function set the optional `encoding` parameter to `utf8`.  When
calling `json.dumps()` set the optional `ensure_ascii` parameter value to `False` and the optional 
`indent` parameter value to `4`.


### 3.5 Docstrings (250 points)
Each function _must_ include a "Docstring" that describes the function, parameters (including 
optional parameter default values), and return value, if any. Utilize the following `Docstring` 
format to document your functions:

* Function description (~1-3 sentences).
* Parameters:
    - arg_1 (type): argument 1 description.
    - arg_2 (type): argument 2 description.
* Returns:
    - type: return value description

When describing parameters and return value (if any) use the following data type abbreviations:

| Data type | Abbreviation |
|:--------- | :----------- |
| Boolean | bool |
| Complex number | complex |
| Dictionary | dict |
| Float | float |
| Integer | int |
| List | list |
| String | str |
| Tuple | tuple |

#### 3.5.1 Docstring example
```python
import requests

def get_resource(resource_uri, params=None):
    """Leverage the HTTP GET method to request a representation of the resource.
    Return the decoded JSON as a dictionary object.

    Parameters:
        resource_uri (str): the resource address.
        params (dict): dictionary of optional querystring arguments.

    Returns:
        dict: dictionary representation of decoded JSON.
    """

    # Write code

    pass

# Get Princess Lei Organa
resource = 'https://SWAPI.co/api/people/'
response = get_resource(resource, {'search': 'lei organa'})
```

:bulb: Recall that a function without an explicit `return` statement returns `None`. If you write
a function without a `return` statement you may exclude the `Docstring's` "Returns:" description.




