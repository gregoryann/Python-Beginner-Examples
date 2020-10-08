"""
XOR Swap Algorithm

This is more informational than a challenge. You can actually switch 2 variables with the XOR operation ^. XOR works with two arguments. It turns both arguments in their binary representation, and for each bit, returns 1 if they are different, 0 otherwise.

The return value is the decimal representation of the new binary string. So, if you don't know how to do it, go play around with it! After some time on paper, you will understand what is going on, and how it works.

Your job is to switch 2 variables using the XOR operator, which means your return statement should be return[a, b], but the value stored in the variables need to be switched.

Examples
XOR(10, 41) ➞ (41, 10)

XOR(69, 420) ➞ (420, 69)

XOR(12345, 890412) ➞ (890412, 12345)
For this challenge avoid doing the following:
def XOR(a, b): 
  return[b, a] 
def XOR(a, b):
  temp = a
  a = b
  b = temp
  return[a, b] 

Notes
If you're stuck, or don't have time to test out different cases, check the Resources tab.
"""





################################################################
"""
Solution 1
"""


def XOR(a, b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return [a, b]





################################################################
"""
Solution 2
"""


def XOR(a, b):
	return [a ^ a ^ b, a ^ b ^ b]









