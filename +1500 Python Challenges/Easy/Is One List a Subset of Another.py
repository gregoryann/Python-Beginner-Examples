"""
Is One List a Subset of Another?
Create a function that returns True if the first list is a subset of the second. Return False otherwise.

Examples
is_subset([3, 2, 5], [5, 3, 7, 9, 2]) ➞ True

is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]) ➞ True

is_subset([1, 2], [3, 5, 9, 1]) ➞ False

Notes
Both lists will contain only unique values.
"""


"""
Solution 1
"""

def is_subset(lst1, lst2):
	return set(lst1) <= set(lst2)

"""
Solution 2
"""

def is_subset(lst1, lst2):
	return all(i in lst2 for i in lst1)

"""
Solution 3
"""

is_subset = lambda x,y: all(k in y for k in x)

"""
Solution 4
"""

def is_subset(lst1, lst2):
	set1 = set(lst1)
	set2 = set(lst2)
	if set1.issubset(set2):
		return True
	else:
		return False




