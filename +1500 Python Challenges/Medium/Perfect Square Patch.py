"""
Perfect Square Patch

Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.

Examples
square_patch(3) ➞ [
  [3, 3, 3],
  [3, 3, 3],
  [3, 3, 3]
]

square_patch(5) ➞ [
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5]
]

square_patch(1) ➞ [
  [1]
]

square_patch(0) ➞ []

Notes
n >= 0.
If n == 0, return an empty list.
"""



################################################################
"""
Solution 1
"""


square_patch=lambda n:[[n]*n]*n



################################################################
"""
Solution 2
"""

def square_patch(n):
	array2d = []
	for row in range(0, n, 1):
		array = []
		for column in range(0, n, 1):
			array.append(n)
		array2d.append(array)
	return array2d


################################################################
"""
Solution 3
"""


def square_patch(n):
	ans = []
	for x in range(n):
		ans.append([n])
	return [x * n for x in ans]




#################################################################
"""
Solution 4
"""

def square_patch(n):
	arr = []
	for i in range(0,n):
		arr.append([n]*n) 
	return arr




