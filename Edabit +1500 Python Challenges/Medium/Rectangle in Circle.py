"""
Rectangle in Circle

Create a function that takes three numbers — the width and height of a rectangle, and the radius of a circle and returns True if the rectangle can fit inside the circle, False if it can't.

Examples
rectangle_in_circle(8, 6, 5) ➞ True

rectangle_in_circle(5, 9, 5) ➞ False

rectangle_in_circle(4, 7, 4) ➞ False
"""




################################################################
"""
Solution 1
"""


def rectangle_in_circle(w, h, radius):
    return (w**2 + h**2)**0.5 <= 2*radius



################################################################
"""
Solution 2
"""


rectangle_in_circle=lambda w,h,r:(w*w+h*h)**.5<=2*r



################################################################
"""
Solution 3
"""


import math
def rectangle_in_circle(w, h, radius):
	return math.sqrt(w**2+h**2) < radius*2


#################################################################
"""
Solution 4
"""


import math
def rectangle_in_circle(w, h, radius):
	return math.hypot(w, h) < radius*2



