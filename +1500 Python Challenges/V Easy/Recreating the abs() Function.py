"""
Recreating the abs() Function
The abs() function returns the absolute value of a number. This means it returns a number's positive value. You can think of it as the distance away from zero.

Create a function that recreates this functionality.

Examples
absolute(-5) ➞ 5

absolute(-3.14) ➞ 3.14

absolute(250) ➞ 250

Notes
Tests will only include valid numbers.
Note that positive numbers will stay positive!
Don't use the abs() function (it will defeat the purpose of the challenge).
"""


"""
Solution 1
"""

def absolute(n):
		return -n if n < 0 else n

"""
Solution 2
"""

def absolute(n):
	return max(n, -n)

"""
Solution 3
"""

def absolute(n):
	if n < 0:
		return n*(-1)
	else:
		return n

"""
Solution 4
"""

absolute=lambda n:(n**2)**0.5

absolute = lambda n:n if n >= 0 else n * -1


