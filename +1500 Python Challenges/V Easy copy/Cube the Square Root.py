"""
Cube the Square Root
Create a function that takes a number as an argument and returns the square root of that number cubed.

Examples
cube_squareroot(81) ➞ 729

cube_squareroot(1646089) ➞ 2111932187

cube_squareroot(695556) ➞ 580093704
Notes
All numbers will evenly square root, so don't worry about decimal numbers.

"""



"""
Solution 1
"""

def cube_squareroot(num):
	return num**(3/2)


"""
Solution 2
"""

cube_squareroot=lambda n:n**1.5

"""
Solution 3
"""

import math

def cube_squareroot(num):
	return (math.sqrt(num))**3


"""
Solution 4
"""


def cube_squareroot(num):
		root = num ** 0.5
		result = num * root
		return result




def cube_squareroot(num):
    a=(num**3)**(1/2)
    return (int(a))
print(cube_squareroot (1646089))
