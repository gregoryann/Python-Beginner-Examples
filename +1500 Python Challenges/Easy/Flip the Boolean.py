"""
Flip the Boolean

Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

Examples
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def reverse(arg=None):
	return "boolean expected" if not isinstance(arg, bool) else not arg

"""
Solution 2
"""

def reverse(arg=None):
	return not arg if type(arg) == bool else "boolean expected"

"""
Solution 3
"""

def reverse(arg):
	if isinstance(arg, bool):
		return not arg
	else:
		return('boolean expected')

"""
Solution 4
"""

def reverse(arg):
	if str(arg) == "0" or str(arg) == "1":
		return "boolean expected"
	return not arg if arg == True or arg == False else "boolean expected"




