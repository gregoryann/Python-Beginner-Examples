"""
Two Distinct Elements

In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]

Notes
Keep the same ordering in the output.
"""




################################################################
"""
Solution 1
"""


def return_unique(lst):
  return [i for i in lst if lst.count(i)==1]






################################################################
"""
Solution 2
"""


return_unique=lambda l:[e for e in l if l.count(e)<2]





################################################################
"""
Solution 3
"""


def return_unique(lst):
	result = []
	for char in lst:
		if lst.count(char) < 2:
			result.append(char)
	return result





#################################################################
"""
Solution 4
"""


def return_unique(lst):
	c = Counter(lst)
	lst = [n for n in lst if c[n] == 1]
	return lst




