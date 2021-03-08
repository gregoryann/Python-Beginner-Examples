"""
Find the Highest Integer in the List Using Recursion

Create a function that finds the highest integer in the list using recursion.

Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8

Notes
Please use the recursion to solve this (not the max() method).
"""



################################################################
"""
Solution 1
"""

def find_highest(lst):
	if len(lst) == 1: return lst[0]
	r = find_highest(lst[1:])
	return r if r>= lst[0] else lst[0]





################################################################
"""
Solution 2
"""

find_highest=f=lambda l:l[0]if len(l)==1else l[0]if all(l[0]>x for x in l[1:])else f(l[1:])






################################################################
"""
Solution 3
"""

def find_highest(lst,n=0):
	if lst:
		m = lst.pop()
		n = m if m > n else n
		return find_highest(lst,n)
	return n





#################################################################
"""
Solution 4
"""

def find_highest(list):
	highest=None
	for i in list:
		if highest is None or highest<i:
			highest=i
	return highest




