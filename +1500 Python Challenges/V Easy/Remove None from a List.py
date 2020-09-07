"""
Remove None from a List

Create a function to remove all None values from a list.

Examples
remove_none(["a", None, "b", None]) ➞ ["a", "b"]
remove_none([None, None, None, None, None]) ➞ []
remove_none([7, 8, None, 9]) ➞ [7, 8, 9]

"""

"""
Solution 1
"""

def remove_none(lst):
	return [x for x in lst if x != None]

"""
Solution 2
"""

def remove_none(arr):
	values = []
	for items in arr:
		if items != None:
			values.append(items)
	return values

"""
Solution 3
"""

def remove_none(lst):
	newlst = list(filter(lambda x: x != None, lst))
	return newlst



