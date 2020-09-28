"""
How Heavy Is It?
Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

How to solve:

Calculate the volume of the cylinder.
Convert cm³ into dm³.
1dm³ = 1L, 1L is 1Kg.
Examples
weight(4, 10) ➞ 0.5

weight(30, 60) ➞ 169.65

weight(15, 10) ➞ 7.07

Notes
I recommend importing math.
If you get stuck on a challenge, find help in Resources.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def weight(r, h):
	from math import pi
	return round((pi*r**2*h) / 1000, 2)

"""
Solution 2
"""

from math import *

def weight(r, h):
	volume = pi * r * r * h
	volume /= 1000
	volume = round(volume, 2)
	return volume





