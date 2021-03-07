"""
Power of Two

Write a function that returns True if an integer can be expressed as a power of base value 2 and False otherwise.

Examples
power_of_two(32) ➞ True

power_of_two(1) ➞ True

power_of_two(18) ➞ False
"""



################################################################
"""
Solution 1
"""


from math import log

def power_of_two(num):
	return log(num, 2).is_integer()


################################################################
"""
Solution 2
"""


def power_of_two(num):
	return num != 0 and ((num & (num - 1)) == 0)



################################################################
"""
Solution 3
"""


def power_of_two(num):
	import math
	return math.log2(num).is_integer()



#################################################################
"""
Solution 4
"""


def power_of_two(num):
	from math import log2
	return log2(num).is_integer()



