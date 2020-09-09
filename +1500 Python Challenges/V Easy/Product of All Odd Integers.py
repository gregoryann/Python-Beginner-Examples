"""

Product of All Odd Integers

Create a function that returns the product of all odd integers in a list.

Examples
odd_product([3, 4, 1, 1, 5]) ➞ 15

odd_product([5, 5, 8, 2, 4, 32]) ➞ 25

odd_product([1, 2, 1, 2, 1, 2, 1, 2]) ➞ 1
"""


"""
Solution 1
"""

import numpy
def odd_product(lst):
    return numpy.prod([i for i in lst if i % 2 != 0])

"""
Solution 2
"""

def odd_product(lst):
	prod = 1
	for i in lst:
		if i % 2 != 0:
			prod *= i
	return prod

"""
Solution 3
"""

def odd_product(lst):
	a=1
	for i in range(len(lst)):
		if lst[i]%2!=0:
			a*=lst[i]
	return a


"""
Solution 4
"""

def odd_product(lst):
	value = 1
	for i in lst:
		if i % 2 > 0:
			value *= i
	return value





