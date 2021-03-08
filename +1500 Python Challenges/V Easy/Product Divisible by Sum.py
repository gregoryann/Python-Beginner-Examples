"""
Product Divisible by Sum?
Write a function that returns True if the product of a list is divisible by the sum of that same list. Otherwise, return False.

Examples
divisible([3, 2, 4, 2]) ➞ False

divisible([4, 2, 6]) ➞ True
# 4 * 2 * 6 / 4 + 2 + 6

divisible([3, 5, 1]) ➞ False
"""


"""
Solution 1
"""

def divisible(lst):
	prod = 1
	for i in lst:
		prod *= i
	return prod % sum(lst) == 0

"""
Solution 2
"""

import numpy
def divisible(lst):
    return numpy.prod(lst)% sum(lst) == 0

"""
Solution 3
"""
def divisible(lst):
	x = 1
	for i in lst:
		x *= i
	return not x % sum(lst)

"""
Solution 4
"""

from functools import reduce
def divisible(lst):
	return reduce(lambda x,y:x*y,lst) % sum(lst) == 0


"""
Solution 5
"""

def divisible(lst):
    l = []
    for i in lst:
        if sum(lst) % i == 0:
            l.append(True)
        elif sum(lst) % i > 1:
            if sum(lst) % (sum(lst) % i) == 0:
                l.append(True)
            else:
                l.append(False)
        else:
            l.append(False)
    return all(l)