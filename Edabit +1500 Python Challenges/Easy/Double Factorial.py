"""
Double Factorial

Create a function that takes a number num and returns its double factorial. Mathematically, the formulas for double factorial are as follows.

If num is even:

num !! = num ( num - 2)( num - 4)( num - 6) ... (4)(2)
If num is odd:

num !! = num ( num - 2)(num - 4)(num - 6) ... (3)(1)
If num = 0 or num = -1, then num !! = 1 by convention.

Examples
double_factorial(0) ➞ 1

double_factorial(2) ➞ 2

double_factorial(9) ➞ 945

double_factorial(14) ➞ 645120

Notes
Assume all input values are greater than or equal to -1.
Try to solve it with recursion.
Double factorial is not the same as factorial * 2.
"""



################################################################
"""
Solution 1
"""

from functools import reduce
def double_factorial(n):
		return 1 if n < 2 else reduce(int.__mul__, list(range(2 - n % 2, n + 1, 2)))






################################################################
"""
Solution 2
"""

def double_factorial(num):
	if num in [-1, 0, 1] :
		return 1
	else :
		return num*double_factorial(num-2)





################################################################
"""
Solution 3
"""

import numpy
def double_factorial(num):
	arr = []
	for i in range(num, 0, -2):
		arr.append(i)
	return numpy.prod(arr)





#################################################################
"""
Solution 4
"""

def double_factorial(num):
	from functools import reduce
	if num<=1:
		return 1
	else:

		return reduce(lambda x,y:x*y, list(range([2,1][num%2],num+1,2)))




