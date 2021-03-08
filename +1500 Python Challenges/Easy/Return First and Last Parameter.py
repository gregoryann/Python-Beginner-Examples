"""
Return First and Last Parameter
Write two functions:

first_arg() should return the first parameter passed in.
last_arg() should return the last parameter passed in.
Examples
first_arg(1, 2, 3) ➞ 1

last_arg(1, 2, 3) ➞ 3

first_arg(8) ➞ 8

last_arg(8) ➞ 8

Notes
Return None if the function takes no parameters.
If the function only takes in one parameter, the first_arg and last_arg functions should return the same value.
"""



"""
Solution 1
"""

def first_arg(*args):
	if args: return args[0]

def last_arg(*args):
	if args: return args[-1]

"""
Solution 2
"""

def first_arg(*x):
	return x[0] if x else None

def last_arg(*x):
	return x[-1] if x else None

"""
Solution 3
"""

def first_arg(*args):
	if len(list(args)) == 0:
		return None
	return list(args)[0]

def last_arg(*args):
	if len(list(args)) == 0:
		return None
	return list(args)[-1]

"""
Solution 4
"""

def first_arg(*args):
	return(args[0]  if len(args) > 0 else None)
def last_arg(*args):
	return(args[-1] if len(args) > 0 else None)




