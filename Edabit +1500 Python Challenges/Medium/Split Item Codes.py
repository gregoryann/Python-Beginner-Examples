"""
Split Item Codes

You have a list of item codes with the following format: "[letters][digits]"

Create a function that splits these strings into their alphabetic and numeric parts.

Examples
split_code("TEWA8392") ➞ ["TEWA", 8392]

split_code("MMU778") ➞ ["MMU", 778]

split_code("SRPE5532") ➞ ["SRPE", 5532]
"""



################################################################
"""
Solution 1
"""


import re

def split_code(item):
    parts = re.search(r'(\D*)(\d*)', item)
    return [parts.group(1), int(parts.group(2))]



################################################################
"""
Solution 2
"""


def split_code(item):
	letters = ''.join(x for x in item if x.isalpha())
	digits = ''.join(x for x in item if x.isnumeric())
	return [letters,int(digits)]



################################################################
"""
Solution 3
"""


def split_code(item):
	return [''.join([i for i in item if i.isalpha()]), int(''.join([i for i in item if i.isdigit()]))]


#################################################################
"""
Solution 4
"""


import re

def split_code(item):
	letters, numbers = re.findall(r'[A-Z]+|\d+', item)
	return [letters, int(numbers)]



