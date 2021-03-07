"""
Truthy or Falsy?
A "truthy" value is a value that translates to True when evaluated in a Boolean context. All values are truthy unless they're defined as falsy.

All falsy values are as follows:

False
None
0
[]
{}
""
Create a function that takes an argument of any data type and returns 1 if it's truthy and 0 if it's falsy.

Examples
is_truthy(0) ➞ 0

is_truthy(False) ➞ 0

is_truthy("") ➞ 0

is_truthy("False") ➞ 1
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""



"""
Solution 1
"""

def is_truthy(val): 
	return int(bool(val))


"""
Solution 2
"""

def is_truthy(val):
	return 1 if val else 0

"""
Solution 3
"""

def is_truthy(val):
	if val == 0 or val == False or val == None or val == [] or val == {} or val == "":
		return 0
	else:
		return 1








