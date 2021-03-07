"""
Sum of Number Elements in a List

Lists can be mixed with various types. Your task for this challenge is to sum all the number elements in the given list. Create a function that takes a list and returns the sum of all numbers in the list.

Examples
numbers_sum([1, 2, "13", "4", "645"]) ➞ 3

numbers_sum([True, False, "123", "75"]) ➞ 0

numbers_sum([1, 2, 3, 4, 5, True]) ➞ 15

Notes
Check the Resources tab for help.
"""

#############################################################


"""
Solution 1
"""

def numbers_sum(lst):
		return sum(i for i in lst if type(i) == int)

"""
Solution 2
"""

def numbers_sum(lst):
	return sum([i for i in lst if i.__class__ is int])

"""
Solution 3
"""

def numbers_sum(lst):
	return sum([n for n in lst if str(type(n)) == "<class 'int'>"])





