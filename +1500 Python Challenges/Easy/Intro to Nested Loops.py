"""
Intro to Nested Loops

Imagine a school that kids attend for 6 years. In each year, there are five groups started, marked with the letters a, b, c, d, e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and for the last year, the groups are 6a, 6b, 6c, 6d, 6e.

Write a function that returns the groups in the school by year (as a string), separated with a comma and a space in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".

Examples
print_all_groups() ➞ "1a, 1b, 1c, 1d, 1e, 2a, 2b, 2c, 2d, 2e, 3a, 3b, 3c, 3d, 3e, 4a, 4b, 4c, 4d, 4e, 5a, 5b, 5c, 5d, 5e, 6a, 6b, 6c, 6d, 6e "

Notes
Use nested "for" loops to achieve this, as well as the array of ["a", "b", "c", "d", "e"] groups.
"""



"""
Solution 1
"""

def print_all_groups():
	return ', '.join(i+j for i in '123456' for j in 'abcde')

"""
Solution 2
"""

def print_all_groups():
	result = []
	for i in '123456':
		for x in 'abcde':
			result.append(i+x)
	return ', '.join(result)

"""
Solution 3
"""

def print_all_groups():
	lst = []
	alpha_list = ["a", "b", "c", "d", "e"]
	for i in range(1, 7):
		for j in alpha_list:
			lst.append("{}".format(i) + j)
	return ", ".join(lst)

"""
Solution 4
"""

def print_all_groups():
	c = ['a', 'b', 'c', 'd', 'e']
	y = ['1', '2', '3', '4', '5', '6']
	result = []
	groups = [[''.join([j, i]) for i in c] for j in y]
	for i in groups:
		for j in i:
			result.append(j)
	return ', '.join(result)





