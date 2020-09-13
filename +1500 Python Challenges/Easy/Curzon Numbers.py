"""
Curzon Numbers

In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29

"""


"""
Solution 1
"""

def is_curzon(num):
	return (2**num + 1) % (2*num + 1) == 0

"""
Solution 2
"""

is_curzon = lambda n: not ((1 << n) + 1) % (2 * n + 1)

"""
Solution 3
"""

is_curzon=lambda n:-~(1<<n)%-~(n+n)<1

"""
Solution 4
"""

def is_curzon(num):
	num1 = 1 + (2**num);
	num2 = 1 + (2*num);
	if (num1 % num2) == 0:
		return True
	else:
		return False



