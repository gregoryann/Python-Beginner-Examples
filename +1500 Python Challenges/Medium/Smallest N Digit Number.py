"""
Smallest N Digit Number

Write a function that returns the smallest N-digit number which is a multiple of the specified value.

Examples
smallest(3, 8) ➞ 104
# Smallest 3-digit integer that is a multiple of 8

smallest(5, 12) ➞ 10008

smallest(7, 1) ➞ 1000000

smallest(2, 3) ➞ 12
"""



################################################################
"""
Solution 1
"""


def smallest(digits, value):
    d = 10 ** (digits - 1)
    while d % value != 0:
        d += 1
    return d



################################################################
"""
Solution 2
"""


# without iteration
def smallest(digits, value):
	if value == 1:
		return 10**(digits - 1)
	return value + int(10**(digits - 1) / value) * value



################################################################
"""
Solution 3
"""


def smallest(d, v):
	
    x = int("1" + "0" * (d-1))
    while x>1:
        if x%v==0:
            return(x)
            break
        else:
            x+=1



#################################################################
"""
Solution 4
"""


def smallest(length, number):
    for i in range(10**(length-1), 10*10**length, 1):
        if i % number == 0:
            if len(list(str(i))) >= length:
                return i




