"""
Iterated Square Root

The iterated square root of a number is the number of times the square root function must be applied to bring the number strictly under 2.

Given an integer, return its iterated square root. Return "invalid" if it is negative.

Examples
i_sqrt(1) ➞ 0

i_sqrt(2) ➞ 1

i_sqrt(7) ➞ 2

i_sqrt(27) ➞ 3

i_sqrt(256) ➞ 4

i_sqrt(-1) ➞ "invalid"

Notes
Idea for iterated square root by Richard Spence.
"""




################################################################
"""
Solution 1
"""

def i_sqrt(n, i = 0):
	if n < 0: return 'invalid'
	return i if n < 2 else i_sqrt(n**0.5, i+1)




################################################################
"""
Solution 2
"""


def i_sqrt(n):
	c = 0
	while n >= 2:
		n **= 0.5
		c += 1
	return 'invalid' if n < 0 else c





################################################################
"""
Solution 3
"""


i_sqrt = lambda n: "invalid" if n < 0 else 0 if n < 2 else 1 + i_sqrt(n**0.5)




#################################################################
"""
Solution 4
"""


import math 
def i_sqrt(n):
	if n<0:
		x='invalid'
	if n==2:
		x=1
	if 0<n<2 or n>2:
		x=0
		while 2 <= n:
			n=math.sqrt(n)
			x+=1
	return(x)



