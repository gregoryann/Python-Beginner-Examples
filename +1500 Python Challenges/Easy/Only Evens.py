"""
Only Evens!

create a function that returns True if the num is even and return False if the num is odd. But if the num type is float return None

Examples to use in code:

type(num) == type
num % odd_num == 0
Examples
odd_or_even(6)  ➞  True

odd_or_even(5) ➞  False

odd_or_even(3.2) ➞  None

Notes
Don't forget to use return.
"""



################################################################
"""
Solution 1
"""

def odd_or_even(num):
	if num % 2 == 0:
		return True
	elif type(num) == float:
		return None
	else:
		return False




################################################################
"""
Solution 2
"""

odd_or_even=lambda x:None if '.'in str(x)else bool(1-x%2)






################################################################
"""
Solution 3
"""

def odd_or_even(num):
	if num % 2 == 0:
		return True
	elif num % 2 == 1:
		return False
	elif not num.is_integer():
		return None








