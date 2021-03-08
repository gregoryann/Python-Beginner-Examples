"""
Radians to Degrees

Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8

Notes
The number π can be loaded from the math module with from math import pi.
"""



################################################################
"""
Solution 1
"""


from math import pi
def radians_to_degrees(rad):
	return round(180 * rad/pi,1)



################################################################
"""
Solution 2
"""


import math

def radians_to_degrees(rad):
	return round(math.degrees(rad),1)



################################################################
"""
Solution 3
"""


from math import degrees

radians_to_degrees=lambda radian: round(degrees(radian), 1)


