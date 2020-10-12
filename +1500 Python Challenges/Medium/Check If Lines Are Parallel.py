"""
Check If Lines Are Parallel

Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ True
# Lines are parallel to themselves.

Notes
Two lines are parallels if they have the same slope and the y-intercepts are different. If the slopes are different, the lines are not parallel.
All test cases use valid input (no lists of the wrong size, for example).
All coefficients will be integers (whole numbers).
"""



################################################################
"""
Solution 1
"""


def lines_are_parallel(l1, l2):
	x0, y0, z0 = l1
	x1, y1, z1 = l2
	try: return x0//x1 == y0//y1
	except ZeroDivisionError: return x0 == x1 or y0 == y1







################################################################
"""
Solution 2
"""


def lines_are_parallel(l1, l2):
	one = -l1[0] / l1[1]
	two = -l2[0] / l2[1]
	if one == two:
		return True
	else:
		return False






################################################################
"""
Solution 3
"""


def lines_are_parallel(l1, l2):
	slope1 = (-l1[0]/l1[1])
	slope2 = (-l2[0]/l2[1])
	if slope1 == slope2:
		return True
	else:
		return False






#################################################################
"""
Solution 4
"""


def lines_are_parallel(l1, l2):
	a,b,_=l1
	c,d,_=l2
	
	return a/b==c/d




