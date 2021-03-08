"""
Are the Numbers Equal?
Create a function that takes two integers and checks if they are equal.

Examples
is_equal(5, 6) ➞ False

is_equal(1, 1) ➞ True

is_equal("1", 1) ➞ False
Notes
If there is a string then it should return False.

"""



"""
Solution 1
"""

def is_equal(num1, num2):
	if type(num1) == str or type(num2) == str:
		return False
	return num1 == num2

"""
Solution 2
"""

is_equal=lambda a,b:a==b and not(type(a or b))==str








