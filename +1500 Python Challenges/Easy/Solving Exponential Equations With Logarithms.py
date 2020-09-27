"""
Solving Exponential Equations With Logarithms

Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.

Examples
solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10

Notes
a is raised to the power of what in order to equal b?
"""


"""
Solution 1
"""

from math import log
def solve_for_exp(a, b):
	return round(log(b,a))

"""
Solution 2
"""

def solve_for_exp(a, b):
    cnt = 0
    while b != a:
        b = b / a
        cnt += 1
    return cnt + 1

"""
Solution 3
"""

from math import*
solve_for_exp=lambda a,b:round(log(b,a))

"""
Solution 4
"""

import math
def solve_for_exp(a, b):
	ans =   math.log(b)/math.log(a)
	return round(ans)

print(solve_for_exp(9, 3486784401))




