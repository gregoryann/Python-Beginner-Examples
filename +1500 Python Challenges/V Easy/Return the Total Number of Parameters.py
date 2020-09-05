"""
Return the Total Number of Parameters

Create a function that returns the total number of parameters passed in.

Examples
number_args("a", "b", "c") ➞ 3
number_args(10, 20, 30, 40, 50) ➞ 5
number_args(x, y) ➞ 2
number_args() ➞ 0

Notes
How can you express the input parameter so it takes a variable number of arguments?
Check the Resources tab for additional info.

"""



"""
Solution 1
"""

def number_args(*args):
	return len(args)

"""
Solution 2
"""

def number_args(*f):
	c = 0
	for i in f:
	 c += 1
	return c


"""
Solution 3
"""

def number_args(*args):
	sum = 0
	for arg in args:
			sum = sum + 1
	return sum



