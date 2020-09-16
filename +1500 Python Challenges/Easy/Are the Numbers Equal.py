"""

Are the Numbers Equal?
Create a function that returns True when num1 is equal to num2; otherwise return False.

Examples
is_same_num(4, 8) ➞ False

is_same_num(2, 2) ➞  True

is_same_num(2, "2") ➞ False
Notes
Don't forget to return the result.


"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""


def is_same_num(num1, num2):
	return num1 == num2




"""
Solution 2
"""

def is_same_num(num1, num2):
 if (num1==num2): 
  return True
 else:
  return False



"""
Solution 3
"""


is_same_num = lambda x, y:x==y


"""
Solution 4
"""


def is_same_num(num1, num2):
	if num1==num2:
		answer=True
	else:
		answer=False
	return answer



