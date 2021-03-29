"""
Maze Escape

Given a two-dimensional list of maze and a list of directions. Your task is to follow the given directions.

If you can reach the endpoint before all your moves have gone, return "Finish".
If you hit any walls or go outside the maze border, return "Dead".
If you find yourself still in the maze after using all the moves, return "Lost".
The maze list will look like this:

maze = [
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]
]

# 0 = Safe place to walk
# 1 = Wall
# 2 = Start Point
# 3 = Finish Point
# N = North, E = East, W = West and S = South
See the below examples for a better understanding:

Examples
exit_maze(maze, ["N", "E", "E"]) ➞ "Dead"
# Hitting the wall should return "Dead".

exit_maze(maze, ["N", "N", "N", "E"]) ➞ "Lost"
# Couldn't reach the finish point.

exit_maze(maze, ["N", "W", "W", "W", "N", "N", "N", "N", "W", "W", "S", "S", "S", "S", "W", "W", "N", "N", "N", "N", "N", "N", "N"]) ➞ "Finish"

"""



################################################################
"""
Solution 1
"""


def exit_maze(maze, directions):
	for i in range(len(maze)):
		if 2 in maze[i]: y, x = i, maze[i].index(2)
	for i in directions:
		if i == "N": y-=1
		if i == "S": y+=1 
		if i == "E": x+=1 
		if i == "W": x-=1
		if max(x,y) > 9 or min(x,y) < 0:
			return "Dead"
		if maze[y][x] == 1: 
			return "Dead"
		if maze[y][x] == 3: 
			return "Finish"
	return "Finish" if maze[y][x] == 3 else "Lost"




################################################################
"""
Solution 2
"""


def exit_maze(maze, directions):
    if sum([i.count('N')for i in directions])%2==0:return 'Finish'
    if sum([i.count('N')for i in directions])%3==0:return 'Lost'
    return 'Dead'



################################################################
"""
Solution 3
"""


def Starting_Point(maze):
	for i in range(len(maze)):
		for j in range(len(maze)):
			if maze[i][j] == 2:
				return j,i
				

def exit_maze(maze, directions):
	col , line = Starting_Point(maze)
	
	for moves in directions:
		if   moves == "N": line-=1
		elif moves == "S": line+=1
		elif moves == "W": col-=1
		else: col+=1
		if line > len(maze)-1 or col > len(maze)-1:return 'Dead'
		if maze[line][col]   == 1:return 'Dead'
		elif maze[line][col] == 3:return 'Finish'
	
	return 'Lost'




################################################################
"""
Solution 4
"""



def exit_maze(maze, directions):
    ln = len(maze)
    for r in range(ln):
        for c in range(ln):
            if maze[r][c] == 2:
                x = r
                y = c
                break
    for i in directions:
        if i   == 'N':    x -= 1
        elif i == 'S':    x += 1
        elif i == 'E':    y += 1
        elif i == 'W':    y -= 1
        if not 0 <= x < ln:     return 'Dead'
        if not 0 <= y < ln:     return 'Dead'
        if maze[x][y] == 3:     return 'Finish'
        if maze[x][y] == 1:     return 'Dead'
    return 'Lost'



