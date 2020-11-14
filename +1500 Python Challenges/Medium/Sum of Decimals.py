"""
Sum of Decimals

Captain Obvious is asked to implement a simple function that given two decimal numbers A and B returns their sum.

"Easy one!" he thinks, but soon he discovers that his function fails over the fifty percent of given test cases! He suspects the test cases are wrong, but his calculator is saying they're correct! What's happening?

Can you help Captain Obvious to debug his function and solve the exercise?

Examples
float_sum(0.3, 0.7) ➞ 1

float_sum(0.35, 0.75) ➞ 1.1

float_sum(1.234, 5.6789) ➞ 6.9129


Notes
Given numbers can be either integer or float with 1 up to 6 decimals.
Don't round results!
Bonus: Can you resolve it using a simple math expression instead of a built-in method?
"""



################################################################
"""
Solution 1
"""


float_sum=lambda a,b:(1e6*a+1e6*b)/1e6



################################################################
"""
Solution 2
"""


import decimal

def float_sum(A, B):
  return float(decimal.Decimal(str(A)) + decimal.Decimal(str(B)))



################################################################
"""
Solution 3
"""


def float_sum(A, B):
  return int(A+B) if A and B is int else round(A+B,6)


#################################################################
"""
Solution 4
"""


from decimal import *
def float_sum(A, B):
	if len(str(A))>len(str(B)):
		length=len(str(A))
	else:
		length=len(str(B))
	getcontext().prec=length
	out=float(Decimal(A)+Decimal(B))
	return out



