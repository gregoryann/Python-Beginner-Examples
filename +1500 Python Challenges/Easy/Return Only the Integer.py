"""
Return Only the Integer

Write a function that takes a list of elements and returns only the integers.

Examples
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]

return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]

return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]

return_only_integer(["String",  True,  3.3,  1]) ➞ [1]
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def return_only_integer(lst):
	return [e for e in lst if str(e).isdigit() and isinstance(e, int)]


"""
Solution 2
"""

def return_only_integer(lst):
	return [i for i in lst if type(i)==int]

"""
Solution 3
"""

return_only_integer=lambda l:[i for i in l if type(i)==int]

"""
Solution 4
"""

def return_only_integer(lst):
	lst2 = []
	for x in lst:
		if type(x) == int:
			lst2.append(x)
	return lst2


