"""
s it True?
In this challenge you will be given a relation between two numbers, written as a string.

Here are some example inputs:

"2 = 2", "8 < 7", "5 = 13", "15 > 4"
Write a function that determines if the relation is True or False.

Examples
is_it_true("2 = 2") ➞ True

is_it_true("8 < 7") ➞ False

is_it_true("5 = 13") ➞ False

is_it_true("15 > 4") ➞ True
Notes
Tests will only have three types of relations: =, >, and <
Many approaches work here, but the eval() function is particularly useful!

"""


"""
Solution 1
"""

def is_it_true(relation):
	return eval(relation.replace("=","=="))


"""
Solution 2
"""

def is_it_true(relation):
	if "=" in relation:
		relation = relation.replace("=", "==")
	return eval(relation)

"""
Solution 3
"""

def is_it_true(relation):
	if '=' in relation:
		x = relation.replace('=', '==')
		return eval(x)
	return eval(relation)

"""
Solution 4
"""

def is_it_true(relation):
	if "=" in relation:
		nums = relation.split("=")
		return nums[0] == nums[1]
	return eval(relation)




