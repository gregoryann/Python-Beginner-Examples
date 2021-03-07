"""
Reverse Coding Challenge #3

This is a reverse coding challenge. Normally you're given explicit directions with how to create a function. Here, you must generate your own function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the sample outputs shown.

Examples
[5, 7, 8, 2, 1], 2 ➞ [1, 1, 0, 0, 1]

[9, 8, 16, 47], 4 ➞ [1, 0, 0, 3]

[17, 11, 99, 55, 23, 1], 5 ➞ [2, 1, 4, 0, 3, 1]

[6, 1], 7 ➞ [6, 1]

[3, 2, 9], 3 ➞ [0, 2, 0]

[48, 22, 0, 19, 33, 100], 10 ➞ [8, 2, 0, 9, 3, 0]

Notes
If you get stuck, see Comments for a hint.
"""





################################################################
"""
Solution 1
"""

def mystery_func(lst, n):
  return [i%n for i in lst]





################################################################
"""
Solution 2
"""

def mystery_func(lst, n):
	temp = []
	for item in lst:
		temp.append(item%n)
	return temp






################################################################
"""
Solution 3
"""

mystery_func=lambda l,n:[x%n for x in l]







#################################################################
"""
Solution 4
"""

def mystery_func(lst, n):
	x = []
	for a in lst:
		x.append(a%n)
	return x




