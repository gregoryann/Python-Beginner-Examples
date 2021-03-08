"""
Is It the Same Upside Down?

The number 6090609 has a special property: if you turn the number upside down (imagine rotating your screen 180 degrees), you get 6090609 again.

Write a function that takes a string on the digits 0, 6, 9 and decides if the number is the same upside down.

Examples
same_upsidedown("6090609") ➞ True

same_upsidedown("9669") ➞ False
# Becomes 6996 when upside down.

same_upsidedown("69069069") ➞ True
"""



################################################################
"""
Solution 1
"""


def same_upsidedown(ntxt):
	return ntxt == ntxt.translate(str.maketrans("69","96"))[::-1]



################################################################
"""
Solution 2
"""


def same_upsidedown(txt):
	d = {'0': '0', '6': '9', '9': '6'}
	return all(a in d and d[a] == b for a, b in zip(txt, txt[::-1]))



################################################################
"""
Solution 3
"""


	digits = {'6': '9', '9': '6'}
	return n == ''.join(digits.get(i, '0') for i in str(n))[::-1]



#################################################################
"""
Solution 4
"""


def same_upsidedown(ntxt):
	res = ntxt.replace('6', '%temp%').replace('9', '6').replace('%temp%', '9')
	return res[::-1]==ntxt



#################################################################
"""
Solution 5
"""


def same_upsidedown(a):
    return False not in [a[i] == {'6':'9','9':'6','0':'0'}.get(a[::-1][i]) for i in range(len(a))]
