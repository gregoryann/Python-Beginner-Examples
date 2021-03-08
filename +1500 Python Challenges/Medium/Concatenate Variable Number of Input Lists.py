"""
Concatenate Variable Number of Input Lists

Create a function that concatenates n input lists, where n is variable.

Examples
concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]

concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]

Notes
Lists should be concatenated in order of the arguments.
"""


################################################################
"""
Solution 1
"""


def concat(*args):
	return sum(args, [])





################################################################
"""
Solution 2
"""


def concat(*args):
	return [a for arg in args for a in arg]





################################################################
"""
Solution 3
"""


def concat(*args):
	answer = []
	for arg in args:
		for item in arg:
			answer.append(item)
	return answer




#################################################################
"""
Solution 4
"""


import itertools

def concat(*args):
	x = args
	return list(itertools.chain.from_iterable(x))




