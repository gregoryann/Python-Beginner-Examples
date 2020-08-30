"""
Nothing is Nothing?
Given any number of parameters (which is signified using *args syntax), return True if none of the variables are falsy/empty.

Examples
nothing_is_nothing(0, False, [], {}) ➞ False

nothing_is_nothing(33, "Hello", (True, True, 3)) ➞ True

nothing_is_nothing(True, None) ➞ False
Notes
*args allows a function to take any number of parameters.
Falsy refers to values which evaluate to False in a boolean context. This includes (but is not limited to) variables such as 0, False, None, empty sets, lists and tuples.

"""




"""
Solution 1
"""

def nothing_is_nothing(*args):
	return all(args)


"""
Solution 2
"""

def nothing_is_nothing(*args):
	a = [bool(x) for x in args]
	return False if False in a else True







