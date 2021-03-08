"""
X and Y Coordinates

Create a function that converts two lists of x- and y- coordinates into a list of (x,y) coordinates.

Examples
convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) 
➞ [[1, 5], [5, 8], [3, 9], [3, 1], [4, 0]]

convert_cartesian([9, 8, 3], [1, 1, 1]) 
➞ [[9, 1], [8, 1], [3, 1]]

Notes
Each coordinate is a list, not a tuple.
"""


"""
Solution 1
"""

def convert_cartesian(x, y): 
	return list(map(list, zip(x, y)))


"""
Solution 2
"""

def convert_cartesian(x, y): 
	a = []
	for i in range(len(x)):
		a.append([x[i],y[i]])
	return a

"""
Solution 3
"""

convert_cartesian=lambda x,y:[[i,j]for i,j in zip(x,y)]

"""
Solution 4
"""

def convert_cartesian(x, y):
	# assume lengths of x and y are the same (for zip function)
	assert(len(x) == len(y))
	
	coordinates = [x,y]
	xyPairs = list(zip(*coordinates)) #returns a list of tuples
	
	#because we want a list of lists, we need to convert the tuples
	xyPairs = [list(elem) for elem in xyPairs]
	return xyPairs




