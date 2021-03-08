"""

Count Ones in a 2D Array

Create a function to count the number of 1s in a 2D list.

Examples
count_ones([
  [1, 0],
  [0, 0]
]) ➞ 1

count_ones([
  [1, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]) ➞ 7

count_ones([
  [1, 2, 3],
  [0, 2, 1],
  [5, 7, 33]
]) ➞ 2

"""


"""
Solution 1
"""

def count_ones(matrix):
	return sum([row.count(1) for row in matrix])

"""
Solution 2
"""

def count_ones(matrix):
	count = 0
	for i in range (len(matrix)):
	    for j in range (len(matrix[i])):
			    if (matrix[i][j]==1):
			       count += 1
	return count

"""
Solution 3
"""

def count_ones(matrix):
  t=0
  for i in matrix:
    x=i.count(1)
    t+=x
  return t

"""
Solution 4
"""

def count_ones(matrix):
	x=[]
	for a in matrix:
		for b in a:
			x.append(b)
	return x.count(1)




