"""
Even or Odd Number of Factors
Create a function that returns "even" if a number has an even number of factors and "odd" if a number has an odd number of factors.

Examples
factor_group(33) ➞ "even"

factor_group(36) ➞ "odd"

factor_group(7) ➞ "even"

Notes
You don't need to actually calculate the factors to solve this problem.
Think about why a number would have an odd number of factors.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def factor_group(num):
	return 'odd' if (num ** 0.5)%1 == 0 else 'even'

"""
Solution 2
"""

import math
def factor_group(num):
	if math.sqrt(num) % 1 == 0:
		return 'odd'
	return 'even'

"""
Solution 3
"""

def factor_group(num):
	factors = [i for i in range(1,num+1) if num % i == 0]
	
	if len(factors)%2:
		return 'odd'
	else:
		return 'even'

"""
Solution 4
"""

def factor_group(num):
	numf = len([i for i in range(1, num+1) if num % i == 0]) 
	if numf % 2 == 0: return 'even'
	else: return 'odd'

"""
Solution 5
"""

def factor_group(n):
	x = n // 2
	y = set([x])
	if n == 1:
		return 'odd'
	while x * x != n:
		x = (x + (n // x)) // 2
		if x in y: return 'even'
		y.add(x)
	return 'odd'
