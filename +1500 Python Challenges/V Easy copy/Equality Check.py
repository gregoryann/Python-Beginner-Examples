"""
Equality Check
In this challenge, you must verify the equality of two different given parameters: a and b.

Both the value and the type of parameters need to be tested in order to have a matching equality. The possible types of the given parameters are:

Numbers
Strings
Booleans (False or True)
None
What have you learned so far that will permit you to do two different checks (value and type) with a single statement?

Implement a function that returns True if the parameters are equal, and False if they are different.

Examples
check_equality(1, True) ➞ False
# A number and a boolean: their type is different

check_equality(0, "0") ➞ False
# A number and a string: their type is different

check_equality(1,  1) ➞ True
# A number and a number: their type and value are equal
Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""






"""
Solution 1
"""

def check_equality(a, b):
	return a is b

"""
Solution 2
"""

def check_equality(a, b):
	return a == b and type(a) == type(b)


"""
Solution 3
"""

def check_equality(a, b):
	if a == b and type(a) == type(b):
		return True
	else:
		return False



"""
Solution 4
"""






