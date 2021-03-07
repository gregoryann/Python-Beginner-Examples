"""
Number of Squares in an N * N Grid

Create a function that calculates the number of different squares in an n * n square grid. Check the Resources tab.

Examples
number_squares(2) ➞ 5

number_squares(4) ➞ 30

number_squares(5) ➞ 55

Notes
Input is a positive integer.
Square pyramidal number.
"""





################################################################
"""
Solution 1
"""

def number_squares(n):
  return sum([i**2 for i in range(1,n+1)])






################################################################
"""
Solution 2
"""


def number_squares(n):
    if n == 1:
        return n * n

    return n * n + number_squares(n-1)

print(number_squares(5))







################################################################
"""
Solution 3
"""


def number_squares(n):
    y = 0
    for x in range(1, n + 1):
		    y = y + x ** 2
    return y






#################################################################
"""
Solution 4
"""

def number_squares(n):
	sum = 0
	for i in range (0, n+1):
		sum = sum + i**2
	return sum




