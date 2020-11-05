"""
Is This a Right Angled Triangle?

Given three numbers, x, y and z, determine whether they are the edges of a right angled triangle.

Examples
right_triangle(3, 4, 5) ➞ True
# This is the classic example of a "nice" right angled triangle.

right_triangle(145, 105, 100) ➞ True
# This is a less famous example.

right_triangle(70, 130, 110) ➞ False
# This isn't a right angled triangle.

Notes
Notice the largest side of the triangle might not be the last one passed to the function.
All numbers will be integers (whole numbers).
"""



################################################################
"""
Solution 1
"""


def right_triangle(x, y, z):
	if x>0 and y>0 and z>0:
		return (x*x + y*y + z*z) - max(x,y,z)**2 == max(x,y,z)**2
	return False



################################################################
"""
Solution 2
"""


def right_triangle(x, y, z):
	x, y, z = sorted([x,y,z])
	return all(i > 0 for i in [x,y,z]) and x**2 + y**2 == z**2




################################################################
"""
Solution 3
"""

def right_triangle(x, y, z):
	if x <= 0 or y <= 0 or z <= 0:
		return False
		
	a, b, c = sorted([x, y, z])
	return c**2 == a**2 + b**2


#################################################################
"""
Solution 4
"""


def right_triangle(x, y, z):
	sides = [x,y,z]
	for item in sides:
		if item <= 0:
			return False
	hyp = max(sides)
	sides.remove(hyp)
	others = sides
	if hyp ** 2 == others[0] ** 2 + others[1] ** 2:
		return True
	else:
		return False



