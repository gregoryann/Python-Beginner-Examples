"""
Find the Index (Part #2)

Create a function that searches for the index of a given item in a list. If the item is present, it should return the index, otherwise, it should return -1.

Examples
search([1, 2, 3, 4], 3) ➞ 2

search([2, 4, 6, 8, 10], 8) ➞ 3

search([1, 3, 5, 7, 9], 11) ➞ -1

Notes
If the item is not present, return -1.
The given list is ordered.
"""




################################################################
"""
Solution 1
"""

def search(lst, item):
	return lst.index(item) if item in lst else -1




################################################################
"""
Solution 2
"""

def search(lst, item):
  return -1 if item not in lst else sorted(lst).index(item)






################################################################
"""
Solution 3
"""

search=lambda l,i:l.index(i)if i in l else -1






#################################################################
"""
Solution 4
"""


def search(lst, item):
	lst.sort()
	if item not in lst:
	  return -1
	return lst.index(item)





