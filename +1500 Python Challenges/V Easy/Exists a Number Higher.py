"""

Exists a Number Higher?
Write a function that returns True if there exists at least one number that is larger than or equal to n.

Examples
exists_higher([5, 3, 15, 22, 4], 10) ➞ True
exists_higher([1, 2, 3, 4, 5], 8) ➞ False
exists_higher([4, 3, 3, 3, 2, 2, 2], 4) ➞ True
exists_higher([], 5) ➞ False

Notes
Return False for an empty array []

"""


"""
Solution 1
"""

def exists_higher(lst, n):
	return lst != [] and max(lst) >= n

"""
Solution 2
"""

def exists_higher(lst, n):
	return False if lst == [] else sorted(lst)[-1] >= n

"""
Solution 3
"""

def exists_higher(lst, n):
	l = []
	for i in lst:
		if i >= n:
			l.append(i)
		elif lst == "":
			return False
	
	if len(l) > 0:
		return True
	else:
		return False






