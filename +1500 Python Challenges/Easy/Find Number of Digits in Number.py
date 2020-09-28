"""
Find Number of Digits in Number
Create a function that will return an integer number containing the amount of digits in the given integer num.

Examples
num_of_digits(1000) ➞ 4

num_of_digits(12) ➞ 2

num_of_digits(1305981031) ➞ 10

num_of_digits(0) ➞ 1

Notes
Try to solve this challenge without using strings!
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def num_of_digits(n):
	return next(i for i in range(1, 100) if abs(n) < 10**i)

"""
Solution 2
"""

import math

def num_of_digits(num):
	if num > 0:
		return int(math.log10(num)) + 1
	if num == 0:
		return 1
	else:
		return int(math.log10(-1 * num)) + 1

"""
Solution 3
"""

import math
def num_of_digits(n):
    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+1
    return digits

print(num_of_digits(-2147483647))

"""
Solution 4
"""

def num_of_digits(num):
	newl = [i for i in str(num) if i.isdigit()]
	return len(newl)




