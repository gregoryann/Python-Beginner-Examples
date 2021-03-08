"""

Find the nth Tetrahedral Number

Create a function that takes an integer n and returns the nth tetrahedral number.

Alternative Text

Examples
tetra(2) ➞ 4

tetra(5) ➞ 35

tetra(6) ➞ 56

Notes
There is a formula for the nth tetrahedral number.
"""




################################################################
"""
Solution 1
"""


def tetra(n):
	return (n * (n + 1) * (n + 2)) / 6



################################################################
"""
Solution 2
"""


def tetra(n):
	x = []
	y = []
	for i in range(n + 1):
		x.append(i)	
		y.append(sum(x))
	return sum(y)


################################################################
"""
Solution 3
"""


def tetra(n):
	arr = []
	last, boost = 1, 2
	for i in range(n):
		arr.append(last)
		last += boost
		boost += 1
	return sum(arr)



#################################################################
"""
Solution 4
"""

tetra = lambda n: (n * (n + 1) * (n + 2)) / 6





