"""
Nth Smallest Element

Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).

Examples
nth_smallest([1, 3, 5, 7], 1) ➞ 1

nth_smallest([1, 3, 5, 7], 3) ➞ 5

nth_smallest([1, 3, 5, 7], 5) ➞ None

nth_smallest([7, 3, 5, 1], 2) ➞ 3

Notes
n will always be >= 1.
Each number in the array will be distinct (there will be a clear ordering).
Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest element, return None.
"""


"""
Solution 1
"""

def nth_smallest(lst, n):
	return sorted(lst)[n-1] if n <= len(lst) else None

"""
Solution 2
"""

def nth_smallest(lst, n):
	lst.sort()
	if n <= len(lst):
		return lst[n-1]

"""
Solution 3
"""

def nth_smallest(lst, n):
	lst.sort()
	try:
		return lst[n -1]
	except IndexError:
		return None

"""
Solution 4
"""

def nth_smallest(lst, n):
	slst = sorted(lst)
	#print(slst)
	if len(lst) >= n and n>0:
		return slst[n-1]
	else: return
	
print(nth_smallest([5,3,2,1],3))




