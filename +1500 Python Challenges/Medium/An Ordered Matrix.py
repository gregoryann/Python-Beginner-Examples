"""
An Ordered Matrix

Create an ordered 2D list (matrix). A matrix is ordered if its (0, 0) element is 1, its (0, 1) element is 2, and so on. Your function needs to create an a × b matrix. a is the first argument and b is the second.

Examples
ordered_matrix(5, 5) ➞ [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25]
]

ordered_matrix(1, 1) ➞ [[1]]

ordered_matrix(1, 5) ➞ [[1, 2, 3, 4, 5]]

Notes
a is the height of the matrix (y coordinate), and b is the width (x coordinate).
a and b will always be positive, and the matrix will always be square shaped (in each row are the same amount of columns).
a and b are integers.
"""




################################################################
"""
Solution 1
"""


ordered_matrix=lambda a,b:[[i+1+b*j for i in range(b)]for j in range(a)]




################################################################
"""
Solution 2
"""


import numpy as np

def ordered_matrix(a, b):
	lst = np.arange(1, (a*b)+1)
	return lst.reshape(a, b).tolist()




################################################################
"""
Solution 3
"""


def ordered_matrix(a, b):
	import numpy as np
	return np.array([x for x in range(1,(a*b)+1)]).reshape(a,b).tolist()




#################################################################
"""
Solution 4
"""


def ordered_matrix(a, b):
	nums = [i for i in range(1, a*b + 1)]
	return [[nums.pop(0) for _ in range(b)] for _ in range(a)]



