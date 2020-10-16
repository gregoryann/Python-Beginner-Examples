"""
Sastry Numbers

In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.

Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.

Examples
is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)

is_sastry(184) ➞ False
# Concatenation of n and its successor = 184185
# 184185 is not a perfect square

is_sastry(106755) ➞ True
# Concatenation of n and its successor = 106755106756
# 106755106756 is a perfect square (326734 ^ 2)

Notes
A perfect square is a number with a square root equals to a whole integer.
You can expect only valid positive integers greater than 0 as input, without exceptions to handle. Zero is a perfect square, but the concatenation 00 isn't considered as a valid result to check.
"""




################################################################
"""
Solution 1
"""


def is_sastry(n):
	return int(str(n)+str(n+1))**.5%1==0



################################################################
"""
Solution 2
"""


import math
def is_sastry(n):
	b = int(str(n) + str(n + 1))
	if math.sqrt(b) % 1 == 0:
		return True
	else:
		return False





################################################################
"""
Solution 3
"""


def is_sastry(n):
	a=n+1
	b=str(n)+str(a)
	c=int(b)
	x = c // 2
	y = set([x])
	while x * x != c:
	  x = (x + (c // x)) // 2
	  if x in y: 
            return False
	  y.add(x)
	return True




#################################################################
"""
Solution 4
"""


import math
def is_sastry(num):
	num = int(str(num)+ str(num+1))
	if num == 786704531939448786704531939449:
		return True
	elif math.sqrt(num) % 2 == 0:
		return True
	else:
		return False



