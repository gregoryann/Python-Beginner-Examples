"""
Factorial of a Non-Negative Integer

Write a function that takes a non-negative integer and return its factorial.

Examples
factorial(4) ➞ 24

factorial(0) ➞ 1

factorial(9) ➞ 362880

Notes
The factorial of 0 is 1.
The factorial of any positive integer Z is Z * (Z - 1) * (Z - 2) * . . . . . . * 1 (e.g. factorial of 3 is 3 * 2 * 1 = 6).

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def factorial(n):
  return n*factorial(n-1) if n>1 else 1

"""
Solution 2
"""

from math import factorial

"""
Solution 3
"""

def factorial(Z):
	return 1 if Z <= 1 else Z*factorial(Z-1)

"""
Solution 4
"""

factorial=lambda n:n<2 or factorial(n-1)*n

factorial=f= lambda x : 0**x or x*f(x-1)

"""
Solution 5
"""




