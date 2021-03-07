"""
Find the Second Largest Number
Create a function that takes a list of numbers and returns the second largest number.

Examples
second_largest([10, 40, 30, 20, 50]) ➞ 40

second_largest([25, 143, 89, 13, 105]) ➞ 105

second_largest([54, 23, 11, 17, 10]) ➞ 23

"""




"""
Solution 1
"""

def second_largest(lst):
		return sorted(lst)[-2]


"""
Solution 2
"""

def second_largest(lst):
	lst.sort()
	return lst[-2]

"""
Solution 3
"""

def second_largest(lst):
	result = sorted(lst)
	result = result[-2]
	return result

"""
Solution 4
"""

second_largest=lambda l:sorted(l)[-2]




