"""
Squares and Cubes

Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

Examples
check_square_and_cube([4, 8]) ➞ True

check_square_and_cube([16, 48]) ➞ False

check_square_and_cube([9, 27]) ➞ True

Notes
Remember to return either True or False.
All lists contain two positive numbers.
"""



################################################################
"""
Solution 1
"""

def check_square_and_cube(lst):
	return (lst[1] == (lst[0] ** 0.5) ** 3)




################################################################
"""
Solution 2
"""


def check_square_and_cube(nums):
	return nums[0]**0.5 == round(nums[1]**(1/3), 2)



################################################################
"""
Solution 3
"""


import math
def check_square_and_cube(lst):
	if math.sqrt(lst[0])==lst[1]/lst[0]:
		return True
	return False




#################################################################
"""
Solution 4
"""


check_square_and_cube=lambda l:l[0]**(3/2)==l[1]




#################################################################
"""
Solution 5
"""


def check_square_and_cube(lst):
#square of first, cube of second
	a = round(lst[0]**0.5, 6)
	b = round(lst[1]**(1/3), 6)
	return True if a == b else False




