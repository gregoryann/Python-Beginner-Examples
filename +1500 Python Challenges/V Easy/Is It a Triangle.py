"""
Is It a Triangle?
Create a function that takes three numbers as arguments and returns True if it's a triangle and False if not.

Examples
is_triangle(2, 3, 4) ➞ True

is_triangle(3, 4, 5) ➞ True

is_triangle(4, 3, 8) ➞ False
Notes
a, b and, c are the side lengths of the triangles.
Test input will always be three positive numbers.

"""



"""
Solution 1
"""

def is_triangle(*sides):
	return all(s < sum(sides) - s for s in sides)


"""
Solution 2
"""

def is_triangle(a, b, c):
	return ((a + b > c) and (a + c > b) and (b + c > a))


"""
Solution 3
"""

def is_triangle(*s):
	s = sorted(i for i in s)
	return sum(s[:2]) > s[2]

"""
Solution 4
"""

def is_triangle(a, b, c):
	a, b, c = sorted((a, b, c))
	return a + b > c




