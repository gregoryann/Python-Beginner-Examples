"""
Radian to Degree

Create a function that takes an angle in radians and converts it into degrees.

Examples
to_degree(math.pi) ➞ 180

to_degree(math.pi/2) ➞ 90

to_degree(math.pi/4) ➞ 45

Notes
The input angles are in radians.
Check out the resource tab.

"""


"""
Solution 1
"""
def to_degree(radian):
	return radian / math.pi * 180

"""
Solution 2
"""

def to_degree(radian):
	import math
	
	return math.degrees(radian)

"""
Solution 3
"""

import math
def to_degree(radian):
    x = round((math.degrees(radian)))
    return (x)








