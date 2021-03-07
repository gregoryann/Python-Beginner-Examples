"""
Simon Says

Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.

Examples
simon_says([1, 2], [5, 1]) ➞ True

simon_says([1, 2], [5, 5]) ➞ False

simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True

simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False

Notes
Both input lists will be of the same length, and will have a minimum length of 2.
The values of the 0-indexed element in the second list and the n-1th indexed element in the first list do not matter.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def simon_says(lst1, lst2):
	return lst1[:-1] == lst2[1:]

"""
Solution 2
"""

def simon_says(lst1, lst2):
	for i in range(len(lst1)-1):
		if lst2[i+1]!=lst1[i]: return False
	return True

"""
Solution 3
"""

def simon_says(lst1, lst2):
	x=len(lst1)
	del lst1[x-1]
	del lst2[0]
	equal=True
	for i in range(x-1):
		if lst1[i]!=lst2[i]:
			equal=False
	return equal

"""
Solution 4
"""

def simon_says(lst1, lst2):
	return not any(x - y for x, y in zip(lst1, lst2[1:]))





