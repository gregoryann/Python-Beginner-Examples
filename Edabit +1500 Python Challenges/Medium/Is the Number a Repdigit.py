"""

Is the Number a Repdigit

A repdigit is a positive number composed out of the same digit. Create a function that takes an integer and returns whether it's a repdigit or not.

Examples
is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False

Notes
The number 0 should return True (even though it's not a positive number).
Check the Resources tab for more info on repdigits.
"""



################################################################
"""
Solution 1
"""


def is_repdigit(num):
	return len(set(str(num))) == 1



################################################################
"""
Solution 2
"""


def is_repdigit(num):
	num = str(num)
	return num.count(num[0]) == len(num)




################################################################
"""
Solution 3
"""


def is_repdigit(num):
	if num == 0 :
		return True
	n = str(num)
	for i in n:
		if n.count(i) == len(n):
			return True
		else:
			return False




#################################################################
"""
Solution 4
"""


import numpy as np
def is_repdigit(num):
	el = str(num)[0]
	arr = np.array([el for el in str(num)])
	return all(el == arr)



#################################################################
"""
Solution 5
"""

def is_repdigit(num):
    if num<0: return False
    a = [int(i) for i in str(num)]
    return len(set(a))==1