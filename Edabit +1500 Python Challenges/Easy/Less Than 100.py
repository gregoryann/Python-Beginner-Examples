"""

Less Than 100?
Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.

Examples
less_than_100(22, 15) ➞ True
# 22 + 15 = 37

less_than_100(83, 34) ➞ False
# 83 + 34 = 117

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""



def less_than_100(a, b):
	return a + b < 100



"""
Solution 2
"""


less_than_100 = lambda a,b: a+b < 100


"""
Solution 3
"""

def less_than_100(a, b):
	if a + b < 100:
	 return True
	else:
	 return False



"""
Solution 4
"""


def less_than_100(a, b):
	return True if (a + b) < 100 else False


