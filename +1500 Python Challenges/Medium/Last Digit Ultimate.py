"""
Last Digit Ultimate

Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.

Examples
last_dig(25, 21, 125) ➞ True
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).

last_dig(55, 226, 5190) ➞ True
# The last digit of 55 is 5, the last digit of 226 is 6, and the last
# digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is
# equal to the last digit of 5190(0).

last_dig(12, 215, 2142) ➞ False
# The last digit of 12 is 2, the last digit of 215 is 5, and the last
# digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
# not equal to the last digit of 2142(2).

Notes
If you still don't understand:
The last digit of a = x, the last digit of b = y, and the last digit of c = z.
Return True if x*y = z, and False otherwise.
Numbers can be negative.
"""





################################################################
"""
Solution 1
"""


def last_dig(a, b, c):
  return str(a*b)[-1] == str(c)[-1]





################################################################
"""
Solution 2
"""

def last_dig(a, b, c):
	lastA, lastB, lastC = trunc(a), trunc(b), trunc(c)
	lastAB = trunc(lastA * lastB)
	return lastAB == lastC
	
def trunc(num):
	return int(str(num)[len(str(num)) - 1:])






################################################################
"""
Solution 3
"""


def last_dig(a, b, c):
	if a <= 0 : 
		a *= -1
	if b <= 0 : 
	  b *= -1 
	if c <= 0 : 
		c *= -1 
	return ((a% 10) * (b%10)) % 10 == c %10




#################################################################
"""
Solution 4
"""


def last_dig(a, b, c):
	a = int(str(a)[-1])
	b = int(str(b)[-1])
	c = int(str(c)[-1])
	d = a*b
	e = int(str(d)[-1])
	if e == c:
		return True
	else:
		return False





