"""
Recursion: Factorials

Write a function that calculates the factorial of a number recursively.

Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1

"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

"""
Solution 2
"""

def factorial(n):
	if n==0: return 1
	return n*factorial(n-1)
"""
Solution 3
"""

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n - 1)

"""
Solution 4
"""

factorial=lambda n:1if n<2else n*factorial(n-1)

"""
Solution 5
"""

def factorial(n):
	import math
	return math.factorial(n)

"""
Solution 6
"""

import numpy as np
def factorial(n):
	return np.product([x for x in range (1,n+1)])

"""
Solution 7
"""

def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * factorial(n-1)