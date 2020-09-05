"""
Hurdle Jump
Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.

A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.

Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False

Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them).

"""


"""
Solution 1
"""

def hurdle_jump(hurdles, jump_height):
	return True if not hurdles else jump_height >= max(hurdles)

"""
Solution 2
"""

def hurdle_jump(hurdles, jump_height):
	return all([1 if x <= jump_height else 0 for x in hurdles])

"""
Solution 3
"""

def hurdle_jump(hurdles, jump_height):
	return len(list(filter(lambda x:x<=jump_height,hurdles)))==len(hurdles)

"""
Solution 4
"""

def hurdle_jump(hurdles, jump_height):
	if hurdles==[]:
		return True
	return jump_height>=max(hurdles)

"""
Solution 5
"""

