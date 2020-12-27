"""
Rotate a Matrix 90 Degrees Clockwise

Create a function that receives a square n*n matrix and returns that matrix after it has been rotated 90 degrees in the clockwise direction.

Examples
rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

rotate([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["m", "i", "e", "a"],
  ["n", "j", "f", "b"],
  ["o", "k", "g", "c"],
  ["p", "l", "h", "d"]
]

"""




################################################################
"""
Solution 1
"""


def rotate(mat):
    return [list(t) for t in zip(*reversed(mat))]



################################################################
"""
Solution 2
"""


import numpy as np
def rotate(mat):
	m = np.array(mat)
	m = np.rot90(m, axes=(1, 0)).tolist()
	return m



################################################################
"""
Solution 3
"""


def rotate(mat):
	new_mat = []
	for i in range(len(mat[0])):
		li = list(map(lambda x: x[i], mat))
		li.reverse()
		new_mat.append(li)
	
	return new_mat



################################################################
"""
Solution 4
"""


def rotate(mat):
	
	class Grid:
		
		def __init__(self, grid):
			self.grid = grid
			
			self.cols = {}
			for n in range(len(grid[0])):
				col = []
				for row in grid:
					col.append(row[n])
				self.cols[n] = col
			
			self.rows = {}
			for n in range(len(grid)):
				self.rows[n] = grid[n]
		
		def rotate(self, deg):
			
			if deg == 90:
				new_rows = []
				for n in sorted(list(self.cols.keys())):
					new_rows.append(list(reversed(self.cols[n])))
			elif deg == 180:
				new_rows = list(reversed(self.grid))
			elif deg == 270:
				new_rows = []
				for n in reversed(sorted(list(self.cols.keys()))):
					new_rows.append(self.cols[n])
			elif deg == 360:
				new_rows = self.grid
			else:
				return 'Incorrect Angle: {}'.format(deg)
			
			return new_rows
	
	grid = Grid(mat)
	
	return grid.rotate(90)



