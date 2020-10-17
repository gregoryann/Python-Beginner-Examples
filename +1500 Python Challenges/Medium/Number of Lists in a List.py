"""
Number of Lists in a List

Return the total number of lists inside a given list.

Examples
num_of_sublists([[1, 2, 3]]) ➞ 1

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3

num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4

num_of_sublists([1, 2, 3]) ➞ 0
"""



################################################################
"""
Solution 1
"""


def num_of_sublists(lst):
	return str(lst).count('[') - 1




################################################################
"""
Solution 2
"""


def num_of_sublists(lst):
	return sum(isinstance(i, list) for i in lst)




################################################################
"""
Solution 3
"""


def num_of_sublists(lst):
	count = 0
	for i in lst:
		if type(i) == list:
			count +=1
	return count



#################################################################
"""
Solution 4
"""


def num_of_sublists(lst):
	result = []
	for x in lst:
		if type(x) == list:
			result.append(x)
	return len(result)





