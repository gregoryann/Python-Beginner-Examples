"""
String or Integer?
Create a function that checks if the argument is an integer or a string. Return int if it's an integer and str if it's a string.

Examples
int_or_string(8) ➞ "int"

int_or_string("Hello") ➞ "str"

int_or_string(9843532) ➞ "int"

"""



"""
Solution 1
"""

def int_or_string(var):
	return var.__class__.__name__

"""
Solution 2
"""

def int_or_string(hmmm):
	return str(type(hmmm))[-5:-2]

"""
Solution 3
"""

def int_or_string(var):
	if type(var) == str:
		return 'str'
	else:
		return 'int'






