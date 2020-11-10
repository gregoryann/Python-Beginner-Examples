"""
Evaluating Factorials

Create a function that takes a list of factorial expressions and returns the sum.

Examples
eval_factorial(["2!", "3!"]) ➞ 8

eval_factorial(["5!", "4!", "2!"]) ➞ 146

eval_factorial(["0!", "1!"]) ➞ 2

Notes
0! and 1! both equal 1.
"""



################################################################
"""
Solution 1
"""


def eval_factorial(lst):
	return sum(fac(int(k[:-1])) for k in lst)

def fac(n):
	return n*fac(n-1) if n else 1



################################################################
"""
Solution 2
"""


f=lambda n:0**n or n*f(n-1)
eval_factorial=lambda l:sum(f(int(s[:-1]))for s in l)



################################################################
"""
Solution 3
"""


def eval_factorial(lst):
    import math
    sum = 0
    for i in lst:
        sum += math.factorial(int(i[:-1]))
    return sum



#################################################################
"""
Solution 4
"""

import math
def eval_factorial(lst):
	sum = 0
	res = [int(sub[ : -1]) for sub in lst]
	for i in res:
		sum += math.factorial(int(i))
	return sum



