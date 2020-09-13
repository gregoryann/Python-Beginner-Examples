"""
Volume of a Cone

Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

Volume of a Cone Image

Examples
cone_volume(3, 2) ➞ 12.57

cone_volume(15, 6) ➞ 565.49

cone_volume(18, 0) ➞ 0

Notes
Return approximate answer by rounding the answer to the nearest hundredth.
Use Python's math.pi constant or equivalent, don't fall for 3.14 ;-)
If the cone has no volume, return 0.

"""


"""
Solution 1
"""

import math
def cone_volume(h, r):
	return round((1/3)*math.pi*(r**2)*h,2)

"""
Solution 2
"""

from math import pi; cone_volume = lambda h,r: round(pi*h*r**2/3, 2)

"""
Solution 3
"""

def cone_volume(h, r):
	return round(3.141592653589793*r*r*h/3, 2)

"""
Solution 4
"""

import math
def cone_volume(h, r):
		n = (math.pi * (r*r) * (h/3))
		n = math.ceil(n * 100) / 100.0
		return n




