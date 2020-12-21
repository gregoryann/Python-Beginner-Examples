"""
Identity Matrix

An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []


Notes
Incompatible types passed as n should return the string "Error".
"""





################################################################
"""
Solution 1
"""


from numpy import sign

def id_mtrx(n):
	try:
		return [[int(i == j) for i in range(abs(n))] for j in range(abs(n))][::sign(n)]
	except:
		return 'Error'





################################################################
"""
Solution 2
"""


def id_mtrx(n):
	i=0
	j=0
	if type(n) != int:
		return 'Error'
	elif n >=0:
		return [[1 if i == j else 0 for i in range(n)]for j in range(n)]
	elif n < 0:
		return [[1 if i == j else 0 for i in range(abs(n))]for j in range(abs(n))][::-1]





################################################################
"""
Solution 3
"""


def id_mtrx(n):
	try:
		matrix = [[0 for x in range (abs(n))] for y in range(abs(n))]
		for i in range(abs(n)):
			matrix[i][i] = 1
		if n < 0:
			matrix.reverse()
		return matrix
	except:
		return "Error"





################################################################
"""
Solution 4
"""


import numpy as np
def id_mtrx(n):
	try:
		return((np.identity(abs(n)),np.rot90(np.identity(abs(n))))[n<0]).tolist()
	except:
		return "Error"



