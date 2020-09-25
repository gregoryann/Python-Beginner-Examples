"""
Total Volume of All Boxes

Given a list of boxes, create a function that returns the total volume of all those boxes combined together. A box is represented by a list with three elements: length, width and height.

For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1]) should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.

Examples
total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]) ➞ 63

total_volume([2, 2, 2], [2, 1, 1]) ➞ 10

total_volume([1, 1, 1]) ➞ 1

Notes
You will be given at least one box.
Each box will always have three dimensions included.
"""


"""
Solution 1
"""

def total_volume(*boxes):
	return sum([x*y*z for x,y,z in boxes])

"""
Solution 2
"""

def total_volume(*boxes):
	return sum([i[0] * i[1] * i[2] for i in boxes])

"""
Solution 3
"""

from functools import reduce

def total_volume(*boxes):
	return sum([reduce((lambda x,y: x*y), box) for box in boxes])

"""
Solution 4
"""


def total_volume(*boxes):

    products = []

    result = 0

    for item in boxes:

        products.append(item[0] * item[1] * item[2])

    for num in products:

        result = result + num

    return result



