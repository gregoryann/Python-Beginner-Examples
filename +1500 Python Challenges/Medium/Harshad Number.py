"""
Harshad Number

A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True

Notes
A recursive version of this challenge can be found here.
"""





################################################################
"""
Solution 1
"""


def is_harshad(n):
	S = sum(map(int, str(n)))
	return not n % S




################################################################
"""
Solution 2
"""


is_harshad = lambda n: not n % sum(int(i) for i in str(n))





################################################################
"""
Solution 3
"""


def is_harshad(n):
	y = '+'.join(i for i in str(n))
	return n % eval(y) == 0





#################################################################
"""
Solution 4
"""



def is_harshad(n):
    num_lst = list(str(n))
    for i in range(len(num_lst)):
        num_lst[i] = int(num_lst[i])
    if n % sum(num_lst) == 0:
        return True
    return False


