"""
Accumulating Product

Create a function that takes a list and returns a list of the accumulating product.

Examples
accumulating_product([1, 2, 3, 4]) ➞ [1, 2, 6, 24]
# [1, 2, 6, 24] can be written as [1, 1 x 2, 1 x 2 x 3, 1 x 2 x 3 x 4]

accumulating_product([1, 5, 7]) ➞ [1, 5, 35]

accumulating_product([1, 0, 1, 0]) ➞ [1, 0, 0, 0]

accumulating_product([]) ➞ []

Notes
An empty list should return an empty list [].
"""



################################################################
"""
Solution 1
"""


def accumulating_product(lst):
	for i in range(1, len(lst)):
		lst[i] *= lst[i - 1]
	return lst



################################################################
"""
Solution 2
"""


def accumulating_product(lst):
	if len(lst) == 0:
		return lst
	lst2 = []
	lst2.append(lst[0])
	for i in range(1, len(lst)):
		lst2.append(lst[i]*lst2[-1])
	return lst2



################################################################
"""
Solution 3
"""


import numpy
def accumulating_product(lst):
  return [numpy.prod(lst[0: (i+1)]) for i in range(len(lst))]


#################################################################
"""
Solution 4
"""


def accumulating_product(lst):
	from functools import reduce
	return [reduce((lambda x, y: x*y), lst[:x]) for x in range(1, len(lst)+1)]



