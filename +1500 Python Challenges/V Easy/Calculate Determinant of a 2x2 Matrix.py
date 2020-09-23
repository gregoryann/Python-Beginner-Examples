"""
Calculate Determinant of a 2x2 Matrix
Create a function to calculate the determinant of a 2 * 2 matrix. The determinant of the following matrix is: ad - bc:

[[a, b], [c, d]]
Examples
calc_determinant([
  [1, 2],
  [3, 4]
]) ➞ -2

calc_determinant([
  [5, 3],
  [3, 1]
]) ➞ -4

calc_determinant([
  [1, 1],
  [1, 1]
]) ➞ 0

Notes
Matrix will be in 2 * 2 form only.
"""


"""
Solution 1
"""

def calc_determinant(m):
	return m[0][0] * m[1][1] - m[0][1] * m[1][0]

"""
Solution 2
"""

def calc_determinant(matrix):
	(a, b), (c, d) = matrix
	return a * d - b * c

"""
Solution 3
"""

def calc_determinant(matrix): 
	AD = matrix[0][0]*matrix[1][1]
	BC = matrix[0][1]*matrix[1][0]
	return AD - BC

"""
Solution 4
"""

def calc_determinant(matrix):
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	return a*d - b*c




