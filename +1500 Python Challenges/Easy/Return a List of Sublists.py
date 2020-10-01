"""

Return a List of Sublists

Write a function that takes three arguments (x, y, z) and returns a list containing x sublists (e.g. [[], [], []]), each containing y number of item z.

x Number of sublists contained within the main list.
y Number of items contained within each sublist.
z Item contained within each sublist.
Examples
matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]

matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]

matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]

Notes
The first two arguments will always be integers.
The third argument is either a string or an integer.
"""


########################################################################


"""
Solution 1
"""

def matrix(x, y, z):
    return  [[z] * y] * x


"""
Solution 2
"""

def matrix(x, y, z):
    return [[z for i in range(y)] for j in range(x)]

"""
Solution 3
"""

def matrix(x, y, z):
	result = list()
	for i in range(x):
		result.append(y * [z])
	return result




