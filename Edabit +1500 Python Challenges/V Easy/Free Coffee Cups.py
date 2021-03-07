"""
Free Coffee Cups
For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups. Create a function that takes n cups bought and return the total number of cups I would get.

Examples
total_cups(6) ➞ 7

total_cups(12) ➞ 14

total_cups(213) ➞ 248
Notes
Number of cups I bought + number of cups I got for free.
Only valid inputs will be given.

"""



"""
Solution 1
"""

def total_cups(n):
	return n//6 + n

"""
Solution 2
"""

def total_cups(n):
	free_cups = int(n / 6)
	return n + free_cups

"""
Solution 3
"""

total_cups = lambda n:n + n//6

"""
Solution 4
"""

import math
def total_cups(n):
	a = math.floor(n/6)
	return a + n

"""
Solution 5
"""


def total_cups(n):
	if n % 6 == 0 or n > 6:
		extras = n // 6
		return n + extras
	else: 
		return n



