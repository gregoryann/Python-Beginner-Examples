"""
Which Number Is Not like the Others?

Create a function that takes a list of numbers and return the number that's unique.

Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7

unique([0, 0, 0.77, 0, 0]) ➞ 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0

Notes
Test cases will always have exactly one unique number while all others are the same.
"""


"""
Solution 1
"""

def unique(lst):
	return min(set(lst), key=lst.count)

"""
Solution 2
"""

def unique(lst):
	return [num for num in lst if lst.count(num) <= 1][0]

"""
Solution 3
"""

def unique(array):
    for num in array:
        if array.count(num) == 1:
            return num

"""
Solution 4
"""

def unique(lst):
	a = set(lst)
	a0 = list(a)[0]
	a1 = list(a)[1]
	return [a0,a1][lst.count(a0)!=1]




