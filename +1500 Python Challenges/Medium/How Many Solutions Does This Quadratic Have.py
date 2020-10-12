"""
How Many Solutions Does This Quadratic Have?

A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.

Examples
solutions(1, 0, -1) ➞ 2
// x² - 1 = 0 has two solutions (x = 1 and x = -1).

solutions(1, 0, 0) ➞ 1
// x² = 0 has one solution (x = 0).

solutions(1, 0, 1) ➞ 0
// x² + 1 = 0 has no solutions.

Notes
You do not have to calculate the solutions, just return how many there are.
a will always be non-zero.
"""



################################################################
"""
Solution 1
"""


def solutions(a, b, c):
    x = b**2 - 4*a*c
    return 2 if x > 0 else 1 if x == 0 else 0





################################################################
"""
Solution 2
"""


def solutions(a, b, c):
	n = b*b - 4*a*c
	if n < 0: return 0
	if n > 0: return 2
	return 1






################################################################
"""
Solution 3
"""


def solutions(a, b, c):
    if ((b * b) - (4 * a * c)) > 0:
        return 2
    elif ((b * b) - (4 * a * c)) == 0:
        return 1
    else:
        return 0






#################################################################
"""
Solution 4
"""


def solutions(a,b,c):
    import math
    d = b**2-4*a*c # discriminant
    if d < 0:
        return 0
    elif d == 0:
        x1 = -b / (2*a)
        return 1
    else: # if d > 0
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return 2




