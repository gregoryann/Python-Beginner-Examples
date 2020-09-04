"""
No Conditionals?
Write a function that returns 0 if the input is 1, and returns 1 if the input is 0.

Examples
flip(1) ➞ 0

flip(0) ➞ 1
Notes
Try completing this challenge without using any:

Conditionals
Ternary operators
Negations
Bit operators



"""






"""
Solution 1
"""


def flip(y):
	return 1 - y




"""
Solution 2
"""


def flip(y):
	return [1,0][y]


"""
Solution 3
"""

def flip(y):
	d={1:0,0:1}
	return d[y]



"""
Solution 4
"""


def flip(y):
	return [('count' * y).isalpha()].count(False)





def flip(y):
	return 0 if y==1 else 1


