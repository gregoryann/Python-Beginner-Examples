"""
Generate a Countdown of Numbers in a List
Create a function that takes a number as an argument and returns a list of numbers counting down from this number to zero.

Examples:

countdown(5) ➞ [5, 4, 3, 2, 1, 0]
countdown(1) ➞ [1, 0]
countdown(0) ➞ [0]

Notes
The argument will always be greater than or equal to zero.

"""


"""
Solution 1
"""

def countdown(start):
	return [i for i in range(start,-1,-1)]

"""
Solution 2
"""

def countdown(start):
    lst = []
    while start >= 0:
        lst.append(start)
        start = start -1
    return lst

"""
Solution 3
"""

def countdown(start):
	x = []
	for i in range(0, start +1):
		x.append(start - i)
	return x

"""
Solution 4
"""

def countdown(start):
	countdown = []
	while start > -1:
		countdown.append(start);
		start -=1
	return countdown




