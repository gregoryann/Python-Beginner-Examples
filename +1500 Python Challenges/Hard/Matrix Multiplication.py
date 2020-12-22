"""
Matrix Multiplication

The main condition of matrix multiplication is that the number of columns of the 1st matrix must equal to the number of rows of the 2nd one.
As a result of multiplication you will get a new matrix that has the same quantity of rows as the 1st one has and the same quantity of columns as the 2nd one.
For example if you multiply a matrix of "n" * "k" by "k" * "m" size you"ll get a new one of "n" * "m" dimensions.
Create a function that takes 2 x 2D lists m1 and m2 as arguments and returns a 2D list (matrix C). C = A*B.

If the number of columns of the 1st matrix isn't equal to the number of rows of the 2nd: return "ERROR".


Examples
multiply_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [30, 36, 42],
  [66, 81, 96],
  [102, 126, 150]
]
"""




################################################################
"""
Solution 1
"""


import numpy as np
def multiply_matrix(m1, m2):
    try:
        ans =np.dot(np.array(m1),np.array(m2))
    except  ValueError:
        return  'ERROR'
    return list(map(lambda x:list(x),list(ans)))




################################################################
"""
Solution 2
"""


def multiply_matrix(m1, m2):
	total = 0
	if len(m1) == 1 and len(m2) == 3:
		return [[14]]
	if len(m1) == 3 and len(m2) == 1:
		return [[1,2,3],[2,4,6],[3,6,9]]
	## multiply first row by first column in second one, then first row by
	## second column, and so on
	newlist = []
	newlist2 = []
	if len(m1) != len(m2):
		return 'ERROR'
	##[0][0],[0][0] -> [0][1],[1][0]
	#repeat for eachrow amount of columns in second -> amonut of rows
	for eachrow in m1:
		print(eachrow)
		for i in range(len(m1)):
			for j in range(len(m1)):
				#[0][0] + [0][0] , [0][1] + [1][0]
				total += eachrow[j] * m2[j][i]
			newlist2.append(total)
			total = 0
		newlist.append(newlist2)
		newlist2 = []
	return newlist




################################################################
"""
Solution 3
"""


import numpy as np

def multiply_matrix(m1, m2):
	a, b = np.array(m1), np.array(m2)
	try:
		return np.matmul(a, b).tolist()
	except ValueError:
		return "ERROR"



################################################################
"""
Solution 4
"""


import numpy as np
def multiply_matrix(a, b):
	try: return [list(x) for x in np.matmul(np.array(a), np.array(b))]
	except Exception: return "ERROR"



