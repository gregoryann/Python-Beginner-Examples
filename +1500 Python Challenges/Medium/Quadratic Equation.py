"""
Quadratic Equation

Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. The function will take three arguments:

a as the coefficient of x^2
b as the coefficient of x
c as the constant term
Examples
quadratic_equation(1, 2, -3) ➞ 1

quadratic_equation(2, -7, 3) ➞ 3

quadratic_equation(1, -12, -28) ➞ 14

Notes
Quadratic equation is always guaranteed to have a root.
Check the Resources tab for more information on quadratic equations.
Calculate only the root that sums the square root of the discriminant, not the one that subtracts it.
Round the value / return only integer value.

"""





################################################################
"""
Solution 1
"""


def quadratic_equation(a, b, c):
	return ((b**2-4*a*c)**0.5-b)/2/a




################################################################
"""
Solution 2
"""


def quadratic_equation(a, b, c):
	x = 1
	while (a * x**2) + (b*x) + c < 0:
		x += 1
	return x




################################################################
"""
Solution 3
"""


def quadratic_equation(a, b, c):
	pluseval = ((b * -1) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
	minuseval = ((b * -1) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
	return pluseval if pluseval > 0 else minuseval




#################################################################
"""
Solution 4
"""

import math

def quadratic_equation(a, b, c):
	dis = (b**2) - (4*a*c)
	sol1 = (-b+(math.sqrt(dis)))/(2*a)
	sol2 = (-b-(math.sqrt(dis)))/(2*a)
	if sol1 == 0.0:
		return int(abs(sol2))
	else:
		return int(abs(sol1))




