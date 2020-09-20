"""
Most Left Digit

Write a function that takes a string as an argument and returns the left most integer in the string.

Examples
left_digit("TrAdE2W1n95!") ➞ 2

left_digit("V3r1ta$") ➞ 3

left_digit("U//DertHe1nflu3nC3") ➞ 1

left_digit("J@v@5cR1PT") ➞ 5

Notes
Each string will have at least two numbers.
"""


"""
Solution 1
"""

def left_digit(num):
	return [int(d) for d in num if d.isdigit()][0]

"""
Solution 2
"""

def left_digit(num):
	for x in num:
		if x in "0123456789":
			return int(x)

"""
Solution 3
"""

def left_digit(num):
	for ch in num:
		if ch.isdigit():
			return int(ch)

"""
Solution 4
"""

import re
left_digit=lambda a:int(re.findall('[0-9]',a)[0])





