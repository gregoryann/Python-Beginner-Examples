"""
Is the Dictionary Empty?
Write a function that returns True if a dictionary is empty, and False otherwise.

Examples
is_empty({}) ➞ True

is_empty({ "a": 1 }) ➞ False
Notes

"""



"""
Solution 1
"""

def is_empty(dictionary):
	return not dictionary

"""
Solution 2
"""

def is_empty(dictionary):
	return dictionary == {}

"""
Solution 3
"""

def is_empty(dictionary):
		return len(dictionary) == 0

"""
Solution 4
"""

def is_empty(dictionary):
	if dictionary == {}:
		return True
	else:
		return False






def is_empty(dictionary):
	x = len(dictionary)
	if x == 0:
		return True
	else:
		return False