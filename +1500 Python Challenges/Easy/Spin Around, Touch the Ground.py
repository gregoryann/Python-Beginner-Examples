"""
Spin Around, Touch the Ground

Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the list counts as a 90° rotation in that direction.

Worked Example
spin_around(["right", "right", "right", "right", "left", "right"]) ➞ 1
# You spun right 4 times (90 * 4 = 360)
# You spun left once (360 - 90 = 270)
# But you spun right once more to make a full rotation (270 + 90 = 360)
Examples
spin_around(["left", "right", "left", "right"]) ➞ 0

spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]) ➞ 2

spin_around(["left", "left", "left", "left"]) ➞ 1

Notes
Return a positive number.
All tests will only include the words "right" and "left".
"""




################################################################
"""
Solution 1
"""


def spin_around(lst):
	return abs(lst.count('left') - lst.count('right')) // 4



################################################################
"""
Solution 2
"""


def spin_around(lst):
	x , y = lst.count("right") , lst.count("left")
	if x > y:
		return int((x-y)/4)
	if y > x:
		return int((y-x)/4)
	else:
		return 0



################################################################
"""
Solution 3
"""


def spin_around(turns):
	return int(abs(sum(
		0.25 if turn == 'right' else -0.25
		for turn in turns
	)))




#################################################################
"""
Solution 4
"""


def spin_around(lst):
	right_direction = lst.count('right') * 90
	left_direction = lst.count('left') * -90
	total = abs(right_direction + left_direction )
	return total // 360




