"""
Multiplying Numbers in a String

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples
multiply_nums("2, 3") ➞ 6

multiply_nums("1, 2, 3, 4") ➞ 24

multiply_nums("54, 75, 453, 0") ➞ 0

multiply_nums("10, -2") ➞ -20

Notes
Bonus: Try to complete this challenge in one line!
"""


########################################################################




"""
Solution 1
"""

def multiply_nums(nums):
	return eval(nums.replace(', ', '*'))

"""
Solution 2
"""

def multiply_nums(nums):
	x = 1
	for i in nums.split(","):
		x *= int(i)
	return x

"""
Solution 3
"""

from functools import reduce
def multiply_nums(nums):
    return reduce(lambda x, y: x*y, [int(j) for j in nums.split(',')])

"""
Solution 4
"""

import numpy as np

def multiply_nums(nums):
   ans = list(map(int,nums.split(sep=",")))
   ans = np.prod(ans)
   return ans

"""
Solution 5
"""

from functools import reduce

def multiply_nums(nums):
    snums =[int(i) for i in nums.split(", ")]                  
    if min(snums)==0 or max(snums)==0:
        return 0
    else:
        return reduce (lambda x,y:x*y, snums)
