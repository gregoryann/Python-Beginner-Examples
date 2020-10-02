"""
GCD of Two Numbers

Write a function that returns the greatest common divisor (GCD) of two integers.

Examples
gcd(32, 8) ➞ 8

gcd(8, 12) ➞ 4

gcd(17, 13) ➞ 1

Notes
Both values will be positive.
The GCD is the largest factor that divides both numbers.
"""


########################################################################



"""
Solution 1
"""

def gcd(a, b):
	if   a == 0: return b
	elif b == 0: return a
	x = max(a, b)
	y = min(a, b)
	return gcd(y, x % y)

"""
Solution 2
"""

import fractions
def gcd(n1, n2):
	return fractions.gcd(n1,n2)

"""
Solution 3
"""

def gcd(n1, n2):
	return max([c for c in range(1,min([n1,n2])+1) if n1%c==0 and n2%c==0])

"""
Solution 4
"""

def gcd(n1, n2):
    divisor = 1
    i = 2
    if n1 == n2:
        return n1
    elif n1>n2:
        while (i <= n2):
            if (n1 % i == 0) & (n2 % i == 0):
                divisor = i
            i += 1
    else:
        while (i <= n1):
            if (n1 % i == 0) & (n2 % i == 0):
                divisor = i
            i += 1
    return divisor




