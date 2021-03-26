"""
Polydivisible Numbers

Mubashir was reading about Polydivisible Numbers on Wikipedia.

In mathematics a Polydivisible Number (or magic number) is a number in a given number base with digits abcde... that has the following properties:

Its first digit a is not 0.
The number formed by its first two digits ab is a multiple of 2.
The number formed by its first three digits abc is a multiple of 3.
The number formed by its first four digits abcd is a multiple of 4.
etc.

Create a function which takes an integer n and returns True if the given number is a Polydivisible Number and False otherwise.

Examples
is_polydivisible(1232) ➞ True
# 1     / 1 = 1
# 12    / 2 = 6
# 123   / 3 = 41
# 1232  / 4 = 308

is_polydivisible(123220 ) ➞ False
# 1   / 1 = 1
# 12   / 2 = 6
# 123   / 3 = 41
# 1232   / 4 = 308
# 12322   / 5 = 2464.4         # Not a Whole Number
# 123220   /6 = 220536.333...  # Not a Whole Number
"""



################################################################
"""
Solution 1
"""

def is_polydivisible(n):
	n = str(n)
	return all((int(n[:i]) / i).is_integer() for i in range(2, len(n)+1))




################################################################
"""
Solution 2
"""

is_polydivisible=lambda n:all(int(str(n)[:i])%i==0 for i in range(1,len(str(n))+1))



################################################################
"""
Solution 3
"""


from itertools import accumulate
is_polydivisible = lambda n: all(int(x) % -~i == 0 for i, x in enumerate(accumulate(str(n))))






