"""
GCD and LCM ( Part 1)

Create a function that takes two numbers as arguments and returns the Greatest Common Devisor (GCD) of the two numbers.

Examples
gcd(3, 5) ➞ 1

gcd(14, 28) ➞ 14

gcd(4, 18) ➞ 2

Notes
The GCD is the highest number that can divide both arguments without a remainder.
"""



################################################################
"""
Solution 1
"""


def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)



################################################################
"""
Solution 2
"""


gcd=lambda a,b:b and gcd(b,a%b)or a


################################################################
"""
Solution 3
"""


def gcd(a, b):
	if max(a,b)%min(a,b)==0:
		return min(a,b)
	else:
		r=min(a,b)-1
		while r>1:
			if max(a,b)%r==0 and min(a,b)%r==0 :
				return r
			else:
				r=r-1
		return 1


#################################################################
"""
Solution 4
"""


def gcd(a, b):
	a_div = {d for d in range(1, a + 1) if a % d == 0}
	b_div = {d for d in range(1, b + 1) if b % d == 0}
	return max(a_div.intersection(b_div))



