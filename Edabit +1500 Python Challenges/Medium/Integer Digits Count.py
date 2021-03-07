"""
Integer Digits Count

Create a function that counts the integer's number of digits.

Examples
count(318) ➞ 3

count(-92563) ➞ 5

count(4666) ➞ 4

count(-314890) ➞ 6

count(654321) ➞ 6

count(638476) ➞ 6

Notes
For an added challenge, try to solve this without using strings.
Optionally, you can solve this via a recursive approach.
A recursive version of this challenge can be found here.
"""



################################################################
"""
Solution 1
"""


def count(n):
	return len(str(abs(n)))







################################################################
"""
Solution 2
"""


from math import log10, floor
count = lambda n: 1 if n == 0 else floor(log10(abs(n))) + 1







################################################################
"""
Solution 3
"""


count=lambda n:len(str(abs(n)))





#################################################################
"""
Solution 4
"""


def count(n):
	ans = 0
	for i in str(n):
	  if i.isdigit():
		  ans += 1
	return ans





