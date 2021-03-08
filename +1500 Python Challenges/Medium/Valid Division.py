"""
Valid Division

Create a function that takes a division equation d and checks if it will return a whole number without decimals after dividing.

Examples
valid_division("6/3") ➞ True

valid_division("30/25") ➞ False

valid_division("0/3") ➞ True

Notes
Return "invalid" if division by zero.
"""



################################################################
"""
Solution 1
"""


def valid_division(d):
	nums = d.split("/")
	if int(nums[1]) == 0:
		return "invalid"
	
	return int(nums[0]) % int(nums[1]) == 0



################################################################
"""
Solution 2
"""


def valid_division(d):	
	try:
		test = d.replace('/','//')
		return eval(d) == eval(test)
	except ZeroDivisionError:
		return 'invalid'



################################################################
"""
Solution 3
"""


def valid_division(d):
	x = d.split("/")
	try: return (int(x[0])%int(x[1]))==0
	except:return "invalid"



#################################################################
"""
Solution 4
"""


def valid_division(d):
    return eval(d) == int(eval(d)) if d.split('/')[-1] != '0' else 'invalid'



