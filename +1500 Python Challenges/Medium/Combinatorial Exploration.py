"""
Combinatorial Exploration

Given a known number of unique items, how many ways could we arrange them in a row?

Create a function that takes an integer n and returns the number of digits of the number of possible permutations for n unique items. For instance, 5 unique items could be arranged in 120 unique ways. 120 has 3 digits, hence the integer 3 is returned.

Examples
no_perms_digits(0) ➞ 1

no_perms_digits(1) ➞ 1

no_perms_digits(5) ➞ 3

no_perms_digits(8) ➞ 5

Notes
This challenge requires some understanding of combinatorics.
"""



################################################################
"""
Solution 1
"""


no_perms = lambda n: 1 if n in [0, 1] else n * no_perms(n - 1)
no_perms_digits = lambda n: len(str(no_perms(n)))



################################################################
"""
Solution 2
"""


import math
no_perms_digits=lambda n:len(str(math.factorial(n)))



################################################################
"""
Solution 3
"""


import sys
sys.setrecursionlimit(10**6)

def no_perms_digits(num, i=0, total=1):
    if i == num:
        if total // 10 == 0:
            return 1
        else:
            return 1 + no_perms_digits(num, i, total // 10)
    else:
        return no_perms_digits(num, i + 1, total * (i + 1))



#################################################################
"""
Solution 4
"""


from functools import reduce
def no_perms_digits(n):
	if n<=1:
		return 1
	else:
		return len(str(reduce(lambda x, y: x*y, [x for x in range(1, n+1)])))




