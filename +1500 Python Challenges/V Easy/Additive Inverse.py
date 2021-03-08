"""
Additive Inverse
A number added with its additive inverse equals zero. Create a function that returns a list of additive inverses.

Examples
additive_inverse([5, -7, 8, 3]) ➞ [-5, 7, -8, -3]

additive_inverse([1, 1, 1, 1, 1]) ➞ [-1, -1, -1, -1, -1]

additive_inverse([-5, -25, 35]) ➞ [5, 25, -35]
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


"""
Solution 1
"""

def additive_inverse(lst):
	return [-x for x in lst]


"""
Solution 2
"""

import operator as op
def additive_inverse(lst):
	return list(map(op.neg, lst))

"""
Solution 3
"""

def additive_inverse(lst):
	arr = []
	for x in lst:
		arr.append(x*-1)
	return arr

"""
Solution 4
"""

additive_inverse=lambda l:[-i for i in l]


"""
Solution 5
"""

def additive_inverse(lst):
		myList = []
		for i in range (len(lst)):
			if lst[i]<0:
				myList.append(lst[i]*(-1))
			else:
				myList.append(-lst[i])
		return myList