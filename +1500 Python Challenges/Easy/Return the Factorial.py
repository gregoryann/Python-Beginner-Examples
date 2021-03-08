"""
Return the Factorial

Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

Examples
factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800

Notes
Assume all inputs are greater than or equal to 0.

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def factorial(num):
	return 1 if num < 2 else num * factorial(num - 1)

"""
Solution 2
"""

import math

def factorial(num):
	return math.factorial(num)

"""
Solution 3
"""

def factorial(num):
	ans = 1
	if num == 0:
		return ans
	else:
		for i in range(num):
			ans *= i+1
	return ans


"""
Solution 4
"""

def factorial(num):
	if num == 0:
		return 1
	else:
		return num*factorial (num-1)


