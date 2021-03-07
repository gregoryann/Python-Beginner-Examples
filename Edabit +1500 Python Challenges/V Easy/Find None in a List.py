"""
Find None in a List
Create a function to find None in a list of numbers. The return value should be the index where None is found. If None is not found in the list, then return -1.

Examples
find_none([1, 2, None]) ➞ 2

find_none([None, 1, 2, 3, 4]) ➞ 0

find_none([0, 1, 2, 3, 4]) ➞ -1
"""


"""
Solution 1
"""

def find_none(lst):return lst.index(None) if None in lst else -1

"""
Solution 2
"""

def find_none(lst):
    if None not in lst:
        return -1
    return lst.index(None)

"""
Solution 3
"""

def find_none(lst):
	for i, x in enumerate(lst):
		if x == None:
			return i
	return -1


"""
Solution 4
"""

def find_none(lst):
	return -1 if None not in lst else lst.index(None)





