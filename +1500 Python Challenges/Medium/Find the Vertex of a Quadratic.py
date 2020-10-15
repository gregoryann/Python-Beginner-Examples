"""
Find the Vertex of a Quadratic

Every quadratic curve y = a x² + b x + c has a vertex point: the turning point where the curve stops heading down and starts going up.

Given the values a, b and c, you need to return the coordinates of the vertex. Return your answers rounded to 2 decimal places.

Examples
find_vertex(1, 0, 25)  ➞ [0, 25]
# The vertex of y=x²+25 is at (0, 25).

find_vertex(-1, 0, 25) ➞ [0, 25]
# The vertex of y=-x²+25 is at (0, 25).

find_vertex(1, 10, 4) ➞ [-5, -21]
# The vertex of y=x²+10x+4 is at (-5, -21).

Notes
See Resources if you're not sure how to find the x or y coordinates of the vertex.
a will always be non-zero.
"""




################################################################
"""
Solution 1
"""


def find_vertex(a, b, c):
	x = -b / (2*a)
	y = a*x**2 + b*x + c
	return [x, y]




################################################################
"""
Solution 2
"""

def find_vertex(a, b, c):
	#dy/dx = 2ax + b = 0
	x_turn = -b/(2*a)
	y_turn = a*(x_turn)**2 + b * x_turn + c 
	return [x_turn,y_turn]





################################################################
"""
Solution 3
"""


def find_vertex(a, b, c):
	upper = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
	lower = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
	mid = (upper + lower) / 2
	return [mid, a * mid ** 2 + b * mid + c]





#################################################################
"""
Solution 4
"""



def find_vertex(a, b, c):
	x=(-b)/(2*a)
	y=pow(x,2)*a+(x*b)+c
	return [round(x,2),round(y,2)]


