"""

Maximum Edge of a Triangle
Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10
Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""



def next_edge(*args):
	return sum(args) - 1



"""
Solution 2
"""

def next_edge(side1, side2):
	return (side1 + side2) - 1



"""
Solution 3
"""

def next_edge(side1, side2):
		maximum_range_of_a_triangle_third_edge = (side1 + side2) - 1
		return maximum_range_of_a_triangle_third_edge



"""
Solution 4
"""



def next_edge(a, b): return a + b - 1


next_edge = lambda a, b: a + b - 1


def next_edge(side1, side2):
	nextEdge = ( side1 + side2 ) - 1
	return nextEdge