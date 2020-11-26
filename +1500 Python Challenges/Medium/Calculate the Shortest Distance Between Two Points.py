"""
Calculate the Shortest Distance Between Two Points

Create a function that takes a string of four numbers. These numbers represent two separate points on a graph known as the x-axis (horizontal axis) and y-axis (vertical axis).

The order of coordinates in the string corresponds as follows:

"x1,y1,x2,y2"
Calculate the distance between x and y.

Examples
shortestDistance("1,1,2,1") ➞ 1

shortestDistance("1,1,3,1") ➞ 2

shortestDistance("-5,1,3,1") ➞ 8

shortestDistance("-5,2,3,1") ➞ 8.06

Notes
All floats fixed to two decimal places (e.g. 2.34).
"""



################################################################
"""
Solution 1
"""


import math

def shortestDistance(txt):
	x1, y1, x2, y2 = (int(num) for num in txt.split(','))
	return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)



################################################################
"""
Solution 2
"""


def shortestDistance(txt):
	a,b,c,d = map(int,txt.split(","))
	return round(((c-a)**2+(d-b)**2)**0.5,2)



################################################################
"""
Solution 3
"""


import math
def shortestDistance(txt):
	l = txt.split(',')
	dist = ((int(l[0]) - int(l[2]))**2 + (int(l[1]) - int(l[3]))**2)**0.5
	return round(dist,2)



#################################################################
"""
Solution 4
"""


import math
def shortestDistance(txt):
 l = [int(s) for s in txt.split(',')]
 distance = math.sqrt( ((l[0]-l[2])**2)+((l[1]-l[3])**2) )
 return round(distance, 2)




