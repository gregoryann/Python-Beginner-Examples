"""
Travelling Salesman Problem
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

Return the total number of possible paths a salesman can travel, given n paths.

Examples
paths(4) ➞ 24

paths(1) ➞ 1

paths(9) ➞ 362880

Notes
Inspired by a video from Dr. Peter Uelkes.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

from math import factorial as paths

"""
Solution 2
"""

import math
def paths(n):
	return math.factorial(n)

"""
Solution 3
"""

def paths(n):
	return n*paths(n-1) if n else 1

"""
Solution 4
"""

def paths(n):
	if n == 1:
		return 1
	return n * paths(n-1)

"""
Solution 5
"""

def paths(n):
	return n * paths(n - 1) if n > 1 else 1