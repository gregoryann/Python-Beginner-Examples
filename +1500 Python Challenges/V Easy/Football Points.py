"""

Football Points
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far. A win receives 3 points, a draw 1 point and a loss 0 points.

Examples
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0
Notes
Inputs will be numbers greater than or equal to 0.


"""






"""
Solution 1
"""


def football_points(wins, draws, losses):
	return wins*3 + draws




"""
Solution 2
"""

def football_points(wins, draws, losses):
	total = 0
	win_points = wins * 3
	total = win_points + draws
	return total



"""
Solution 3
"""

def football_points(wins, draws, losses):
 x=wins*3
 y=draws*1
 z=losses*0
 return x+y+z



"""
Solution 4
"""


football_points=lambda a,b,c:a*3+b





