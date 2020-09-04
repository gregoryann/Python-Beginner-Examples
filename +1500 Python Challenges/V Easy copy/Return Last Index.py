"""
Return Last Index
-Create a function that returns the last value of the last item in a list or string

-Lists/strings will be of varying size

-Return None if list/string is emtpy

Examples
[0,  4,  19,  34,  50,  -9,  2] ➞ 2

'The quick brown fox jumped over the lazy dog' ➞ 'g'

[] ➞ None
Notes
Function should be able to handle any datatype

"""



"""
Solution 1
"""

def last_ind(lst):
	return lst[-1] if lst else None


"""
Solution 2
"""

def last_ind(lst):
	if len(lst) == 0:
		return None
	return lst[-1]


"""
Solution 3
"""

def last_ind(lst):
	return None if lst == [] or lst == '' else lst[-1]


"""
Solution 4
"""

def last_ind(lst):
	return lst[-1] if len(lst) > 0 else None



