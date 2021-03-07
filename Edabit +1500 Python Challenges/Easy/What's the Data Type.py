"""
What's the Data Type?

Create a function that returns the data type of a given variable. These are the seven data types this challenge will be testing for:

List
Dictionary
String
Integer
Float
Boolean
Date
Examples
data_type([1, 2, 3, 4]) ➞ "list"

data_type({'key': "value"}) ➞ "dictionary"

data_type("This is an example string.") ➞ "string"

data_type(datetime.date(2018,1,1)) ➞ "date"

Notes
Return the name of the data type as a lowercase string.

"""





################################################################
"""
Solution 1
"""

def data_type(value):
  c=value.__class__.__name__
  return c+{'dict': 'ionary', 'str': 'ing', 'int': 'eger'}.get(c, '')






################################################################
"""
Solution 2
"""

def data_type(value):
  return {
    'int': 'integer',
    'list': 'list',
    'dict': 'dictionary',
    'str': 'string',
    'float': 'float',
    'bool': 'boolean',
    'datetime.date': 'date'
  }[str(type(value))[8:-2]]








################################################################
"""
Solution 3
"""

import datetime

TYPE_NAMES_MAP = {
	list: 'list',
	dict: 'dictionary',
	str: 'string',
	int: 'integer',
	float: 'float',
	datetime.date: 'date',
}

def data_type(value):
	return TYPE_NAMES_MAP.get(type(value))









#################################################################
"""
Solution 4
"""

from datetime import date 

def data_type(value):
  value_type=type(value)
  types=["list","dictionary","string","integer","float","boolean","date"]
  if value_type == list:
    return types[0]
  elif value_type == dict:
    return types[1]
  elif value_type == str:
    return types[2]
  elif value_type == int:
    return types[3]
  elif value_type == float:
    return types[4]
  elif value_type == bool:
    return types[5]
  elif value_type == datetime.date:
    return types[6]




#################################################################
"""
Solution 5
"""

import datetime
def data_type(value):
    if type(value) == list: return "list"
    if type(value) == dict: return "dictionary"
    if type(value) == str: return "string"
    if type(value) == int: return "integer"
    if type(value) == float: return "float"
    if type(value) == bool: return "boolean"
    if type(value) == datetime.date: return "date"





#################################################################
"""
Solution 6
"""

data_type=lambda v:{'dict':'dictionary','str':'string','int':'integer'}.get(type(v).__name__,type(v).__name__)










#################################################################
"""
Solution 7
"""




import datetime

def data_type(value):
    DATA = [
            (list, 'list'),
            (dict, 'dictionary'),
            (str, 'string'),
            (int, 'integer'),
            (float, 'float'),
            (bool, 'boolean'),
            (datetime.date, 'date')
            ]
    return [x[1] for x in DATA if isinstance(value, x[0])][0]