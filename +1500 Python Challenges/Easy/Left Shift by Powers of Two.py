"""
Left Shift by Powers of Two

The left shift operation is similar to multiplication by powers of two.

Sample calculation using the left shift operator (<<):

10 << 3 = 10 * 2^3 = 10 * 8 = 80
-32 << 2 = -32 * 2^2 = -32 * 4 = -128
5 << 2 = 5 * 2^2 = 5 * 4 = 20
Write a function that mimics (without the use of <<) the left shift operator and returns the result from the two given integers.

Examples
shift_to_left(5, 2) ➞ 20

shift_to_left(10, 3) ➞ 80

shift_to_left(-32, 2) ➞ -128

shift_to_left(-6, 5) ➞ -192

shift_to_left(12, 4) ➞ 192

shift_to_left(46, 6) ➞ 2944


Notes
There will be no negative values for the second parameter y.
This challenge is more like recreating of the left shift operation, thus, the use of the operator directly is prohibited.
Optionally, you can solve this challenge via recursion.
A recursive version of this challenge can be found in here.
"""




################################################################
"""
Solution 1
"""


def shift_to_left(x, y):
	return x * 2**y


################################################################
"""
Solution 2
"""

def shift_to_left(x, y):
	if not y:
		return x
	return 2*shift_to_left(x,y-1)


################################################################
"""
Solution 3
"""

shift_to_left=lambda x,y:x*2**y





