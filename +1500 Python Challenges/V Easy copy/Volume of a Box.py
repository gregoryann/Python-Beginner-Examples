"""
Volume of a Box
Create a function that takes a dictionary argument sizes (contains width, length, height keys) and returns the volume of the box.

Examples
volume_of_box({ "width": 2, "length": 5, "height": 1 }) ➞ 10

volume_of_box({ "width": 4, "length": 2, "height": 2 }) ➞ 16

volume_of_box({ "width": 2, "length": 3, "height": 5 }) ➞ 30
Notes
Don't forget to return the result.
Remember that the values are in an object.
Volume is length * width * height.

"""


"""
Solution 1
"""

def volume_of_box(sizes):
	w, l, h = sizes.values()
	return w * l * h

"""
Solution 2
"""

def volume_of_box(sizes):
	return sizes['width'] * sizes['length'] * sizes['height']


"""
Solution 3
"""

from numpy import prod
def volume_of_box(sizes):
	return prod([i for i in sizes.values()])

"""
Solution 4
"""

def volume_of_box(sizes):
	a = list(sizes.values())
	return a[0] * a[1] * a[2]

"""
Solution 5
"""


def volume_of_box(sizes):
	sizes_list = sizes.values()
	total = 1
	for num in sizes_list:
		total *= num
	return total



