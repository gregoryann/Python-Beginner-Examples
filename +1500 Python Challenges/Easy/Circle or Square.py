"""
Circle or Square

Given the radius of a circle and the area of a square, return True if the circumference of the cirlce is greater than the square's perimeter and False if the square's perimeter is greater then the circumference of the circle.

Examples
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True

Notes
You can use PI to 2 decimal places (3.14).
Circumference of a circle equals 2*PI*Radius.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def circle_or_square(rad, area):
	return 2*3.14*rad > 4*area**.5

"""
Solution 2
"""

def circle_or_square(rad, area):
    import math
    return 2 * 3.14 * rad > math.sqrt(area) * 4

"""
Solution 3
"""

def circle_or_square(rad, area):
	
	class Circle:
		
		def __init__(self, radius):
			from math import pi as pi
			self.r = radius
			self.circ = 2 * pi * self.r
	
	class Square:
	
		def __init__(self, area):
			
			self.a = area
			
			for n in range(1, int(self.a / 2) + 1):
				if area / n == n:
					self.side = n
					break
			try:
				self.p = self.side * 4
			except AttributeError:
				self.p = 'HELP'
	
	
	circle = Circle(rad)
	square = Square(area)
	
	return circle.circ > square.p






