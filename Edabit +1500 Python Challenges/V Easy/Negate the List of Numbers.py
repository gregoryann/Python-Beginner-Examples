"""
Negate the List of Numbers
Given a list of numbers, negate all elements contained within.

Negating a positive value -+n will return -n, because all +'s are removed.
Negating a negative value --n will return n, because the first - turns the second minus into a +.
Examples
negate([1, 2, 3, 4]) ➞ [-1, -2, -3, -4]

negate([-1, 2, -3, 4]) ➞ [1, -2, 3, -4]

negate([]) ➞ []
Notes
If you get an empty list, return an empty list: []

"""


"""
Solution 1
"""

def negate(lst):
	return [-num for num in lst]


"""
Solution 2
"""

def negate(lst):
	return [-i if i > 0 else abs(i) if i < 0 else 0 for i in lst]

"""
Solution 3
"""

def negate(lst):
	negativeLst = []
	for item in lst:
		negativeLst.append(item*-1)
	return negativeLst

"""
Solution 4
"""

def negate(lst):
	out = []
	for n in lst:
		out.append(n*(-1))
	return out

"""
Solution 5
"""


def negate(lst):
	return [-n if n > 0 else abs(n) for n in lst]
