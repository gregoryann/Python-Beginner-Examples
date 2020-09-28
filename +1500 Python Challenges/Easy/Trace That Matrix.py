"""

Trace That Matrix
Given a square matrix (i.e. same number of rows as columns), its trace is the sum of the entries in the main diagonal (i.e. the diagonal line from the top left to the bottom right).

As an example, for:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
... the trace is 1 + 5 + 9 = 15.

Write a function that takes a square matrix and computes its trace.

Examples
trace([
  [1, 4],
  [4, 1]
]) ➞ 2

# 1 + 1 = 2

trace([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ 15

# 1 + 5 + 9 = 15

trace([
  [1, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]) ➞ 10

# 1 + 2 + 3 + 4 = 10

Notes
As in the examples, the size of the matrices will vary (but they will always be square).
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

def trace(arr):
	return sum(arr[i][i] for i in range(len(arr)))


"""
Solution 2
"""

def trace(arr):
	summ=0
	for i in range(0,len(arr)):
		summ+=arr[i][i]
	return summ


"""
Solution 3
"""

def trace(arr):
	l=[]
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if j==i:
				l.append(arr[i][j])
	return sum(l)


"""
Solution 4
"""

trace=lambda l:sum(l[i][i]for i in range(len(l)))





