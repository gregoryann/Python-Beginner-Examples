"""
List Multiplier

Create a function that takes a list as an argument and returns a new nested list for each element in the original list. The nested list must be filled with the corresponding element (string or number) in the original list and each nested list has the same amount of elements as the original list.

Examples
multiply([4, 5]) ➞ [[4, 4], [5, 5]]

multiply(["*", "%", "$"]) ➞ [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]]

multiply(["A", "B", "C", "D", "E"]) ➞ [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]]

Notes
The given list contains numbers or strings.
"""



################################################################
"""
Solution 1
"""

def multiply(lst):
	return [[i]*len(lst) for i in lst]




################################################################
"""
Solution 2
"""


multiply = lambda l : [[item] * len(l) for item in l]





################################################################
"""
Solution 3
"""


def multiply(l):
	a = []
	for i in l:
		b = []
		for k in range(len(l)):
			b.append(i)
		a.append(b)
	return a







#################################################################
"""
Solution 4
"""


def multiply(l):
	k, c = l, 0
	while k:
		c += 1
		k = k[1:]
	return [[x] * c for x in l]






