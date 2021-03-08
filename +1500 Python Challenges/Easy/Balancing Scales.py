"""

Balancing Scales

Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are equal, return "balanced".

Examples
scale_tip([0, 0, "I", 1, 1]) ➞ "right"
# 0 < 2 so it will tip right

scale_tip([1, 2, 3, "I", 4, 0, 0]) ➞ "left"
# 6 > 4 so it will tip left

scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) ➞ "balanced"
# 15 = 15 so it will stay balanced

Notes
The middle element will always be "I" so you can just ignore it.
Assume the numbers all represent the same unit.
Both sides will have the same number of elements.
There are no such things as negative weights in both real life and the tests!
"""



#############################################################






#############################################################
"""
Solution 1
"""


def scale_tip(lst):
	v = lst.index('I')
	left, right = sum(lst[:v]), sum(lst[v+1:])
	return 'right' if right > left else 'left' if left > right else 'balanced'




#############################################################
"""
Solution 2
"""

def scale_tip(l):
	x=l.index('I')
	i=sum(l[:x])
	r=sum(l[x+1:])
	return'right'if r>i else'left'if i>r else'balanced'





#############################################################
"""
Solution 3
"""


def scale_tip(lst):
	left = sum(lst[0:lst.index('I')])
	right = sum(lst[lst.index('I') + 1:])
	if left == right:
		return 'balanced'
	elif left > right:
		return 'left'
	else:
		return 'right'





#############################################################
"""
Solution 4
"""



import math
def scale_tip(lst):
	ch = sum([i for i in lst][:math.floor(len(lst)/2)])
	ch2 = sum([i for i in lst][math.floor(len(lst)/2)+1:])
	if ch==ch2:
		return 'balanced'
	elif max(ch,ch2)==ch:
		return 'left'
	elif max(ch,ch2)==ch2:
		return 'right'



