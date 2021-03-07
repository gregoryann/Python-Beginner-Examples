"""
A Circle and Two Squares

Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

Scale

Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

square_areas_difference(7) ➞ 98

Notes
Use only positive integer parameters.
"""



################################################################
"""
Solution 1
"""


def square_areas_difference(r):
	# big square:
    length_big_square = 2 * r
    area_big_square = (2 * r)  ** 2
    
    # small square:
    # r is the half diagonal of the small square!
    # corresponding Pythagoras:  r**2 + r**2 = length_small_square**2
    # That's the area of the small square too
    area_small_square = r**2 + r**2
    
    # Difference big - small square:
    return area_big_square - area_small_square



################################################################
"""
Solution 2
"""


import math

def square_areas_difference(r):
	# Calculate diameter
	d = r * 2
	# Larger square area is the diameter of the incircle squared
	lgArea = d * d
	# Use the diameter of the circle as the hypotenuse of the smaller
	# square when cut in half to find the edges length
	# When the legs are equal length (because it's a square), you just
	# divide the hypotenuse by the sqrt of 2
	# Smaller square area is the legs squared
	smLeg = d / math.sqrt(2)
	smArea = smLeg * smLeg
	# We then return the difference between the large area and small area
	return lgArea - round(smArea)




################################################################
"""
Solution 3
"""


import math

def square_areas_difference(r):
	bigSquare = 4 * pow(r, 2)
	smallSquareDiag = 2 * r
	smallSquareSide = smallSquareDiag / math.sqrt(2)
	smallSquare = pow(smallSquareSide, 2)
	return round(bigSquare - smallSquare, 0)



