"""
Volume of a Spherical Shell

The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Volume of Inner Sphere Formula

Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

Spherical Shell Image

Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753


Notes
The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number.
"""






################################################################
"""
Solution 1
"""


from math import pi

def vol_shell(r1, r2):
    v = 4/3*pi*(r1**3 - r2**3)
    return round(abs(v), 3)




################################################################
"""
Solution 2
"""


import math
def vol_shell(r1, r2):
	if r1>=r2:
		return abs(round(math.pi*4/3*(r1**3-r2**3), 3))
	else:
		return abs(round(math.pi*4/3*(r2**3-r1**3), 3))





################################################################
"""
Solution 3
"""


from fractions import Fraction
import math
def vol_shell(r1, r2):
    R = max(r1,r2)
    r = min(r1,r2)
    return round(Fraction(4, 3) * math.pi * (R**3 - r**3), 3)




#################################################################
"""
Solution 4
"""


import math
def vol_shell(r1, r2):
 if (round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))>=0:
   return (round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))
 else:
  return -1*(round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))



