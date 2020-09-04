"""
Find the Index (Part 1)
Create a function that finds the index of a given item.

Examples
search([1, 5, 3], 5) ➞ 1

search([9, 8, 3], 3) ➞ 2

search([1, 2, 3], 4) ➞ -1
Notes
If the item is not present, return -1.

"""


"""
Solution 1
"""

def search(arr, item):
  return -1 if item not in arr else arr.index(item)

"""
Solution 2
"""

def search(lst, item):
	for x in range(len(lst)):
		if lst[x]==item:
			return x
	return -1




