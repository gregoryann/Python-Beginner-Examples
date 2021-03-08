"""
Algebra Sequence — Boxes

Create a function that takes a number (step) as an argument and returns the amount of boxes in that step of the sequence.

Box Sequence Image

Step 0: Start with 0
Step 1: Add 3
Step 2: Subtract 1
Repeat Step 1 & 2 ...
Examples
box_seq(0) ➞ 0

box_seq(1) ➞ 3

box_seq(2) ➞ 2

Notes
Step (the input) is always a positive integer (or zero).
"""



################################################################
"""
Solution 1
"""


def box_seq(step):
	return step + step % 2 * 2



################################################################
"""
Solution 2
"""


def box_seq(step):
	return step + 2 if step%2 else step


################################################################
"""
Solution 3
"""

import math
def box_seq(step):
	return math.ceil(step/2)*3 + int(step/2) * -1


#################################################################
"""
Solution 4
"""


def box_seq(step):
	w = 0
	for i in range(1, step + 1):
		w = w + ((i % 2 == 1) * 3) - ((i % 2 == 0))
	return w



#################################################################
"""
Solution 5
"""


def box_seq(step):
    sequence = [0, 3]
    while step > len(sequence) - 1:
        if sequence[-1] > sequence[-2]:
            sequence.append(sequence[-1]-1)
        else:
            sequence.append(sequence[-1]+3)
    return sequence[step]