"""
Using the "and" Operator
Python has a logical operator and. The and operator takes two boolean values, and returns True if both values are True.

Consider a and b:

a is checked if it is True or False.
If a is False, False is returned.
b is checked if it is True or False.
If b is False, False is returned.
Otherwise, True is returned (as both a and b are therefore True ).
The and operator will only return True for True and True.

Make a function using the and operator.

Examples
And(True, False) ➞ False

And(True, True) ➞ True

And(False, True) ➞ False

And(False, False) ➞ False

"""






"""
Solution 1
"""

def And(a,b):
	return a and b

"""
Solution 2
"""

def And(a, b):
	return a & b

"""
Solution 3
"""

def And(a,b):
	if a == True:
		if b == True:
			return True
		else:
			return False
	else:
		return False
        
"""
Solution 4
"""

def And(a,b):
	return a == True and b == True

        
"""
Solution 5
"""


def And(a, b):
	if ((a) == True and (b) == True):
		return True
	else :
		return False


