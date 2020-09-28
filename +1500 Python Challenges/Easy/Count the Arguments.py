"""
Count the Arguments

Create a function that returns the number of arguments it was called with.

Examples
num_args() ➞ 0

num_args("foo") ➞ 1

num_args("foo", "bar") ➞ 2

num_args(True, False) ➞ 2

num_args({}) ➞ 1

Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def num_args(*args, **kwargs):
	return len(args) + len(kwargs)

"""
Solution 2
"""

def num_args(*args):
	n = 0
	for i in args:
		n += 1
	return n







