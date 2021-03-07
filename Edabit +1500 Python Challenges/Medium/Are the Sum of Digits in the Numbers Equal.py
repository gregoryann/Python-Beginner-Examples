"""
Are the Sum of Digits in the Numbers Equal?
Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.

Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6

is_equal([21, 35]) ➞ False

is_equal([0, 0]) ➞ True
"""





################################################################
"""
Solution 1
"""


def is_equal(lst):
	return lst[0] % 9 == lst[1] % 9



################################################################
"""
Solution 2
"""


def is_equal(lst):
	f = lambda i: sum(int(x) for x in str(lst[i]))
	return f(0) == f(1)



################################################################
"""
Solution 3
"""


is_equal = lambda l : sum(int(n) for n in str(l[0])) == sum(int(m) for m in str(l[1]))



#################################################################
"""
Solution 4
"""


def is_equal(lst):
	return eval('+'.join(x for x in str(lst[0]))) == eval('+'.join(x for x in str(lst[1])))



