"""
Simple Circle Collision Detection

Create a function that returns True if the given circles are intersecting, otherwise return False. The circles are given as two lists containing the values in the following order:

Radius of the circle.
Center position on the x-axis.
Center position on the y-axis.
Examples
is_circle_collision([10, 0, 0], [10, 10, 10]) ➞ True

is_circle_collision([1, 0, 0], [1, 10, 10]) ➞ False

Notes
You can expect useable input and positive radii.
The given coordinates are the centers of the circles.
We are looking for intersecting areas, not intersection outlines.
Check the Resources tab for help.
"""




################################################################
"""
Solution 1
"""


def is_circle_collision(c1, c2):
    r1, x1, y1 = c1
    r2, x2, y2 = c2
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d <= r1 + r2



################################################################
"""
Solution 2
"""


import math
def is_circle_collision(c1, c2):
  dist = math.hypot(c2[1] - c1[1], c2[2] - c1[2])
  if c1[0] + c2[0] >= dist:
    return True
  else:
    return False



################################################################
"""
Solution 3
"""


def is_circle_collision(c1, c2):
  distance = lambda p1, p2: ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)**0.5
  return distance(c1[1:], c2[1:]) <= c1[0] + c2[0]



#################################################################
"""
Solution 4
"""


def is_circle_collision(c1, c2):
    distx = c1[1] - c2[1]
    disty = c1[2] - c2[2]
    distance = (distx**2 + disty**2)**0.5
    return False if distance >= (c1[0]+c2[0]) else True




