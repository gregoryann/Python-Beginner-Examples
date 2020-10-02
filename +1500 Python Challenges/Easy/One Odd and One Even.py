"""
One Odd and One Even

Given a two digit number, return True if that number contains one even and one odd digit.

Examples
one_odd_one_even(12) ➞ True

one_odd_one_even(55) ➞ False

one_odd_one_even(22) ➞ False
"""


########################################################################




"""
Solution 1
"""


def one_odd_one_even(n):
	return (n // 10 + n) % 2


"""
Solution 2
"""

def one_odd_one_even(n):
	return (n%2 and not n//10 % 2) or (not n%2 and n//10 % 2)

"""
Solution 3
"""

def one_odd_one_even(n):
	if (n % 2 == 1 and (n // 10) % 2 == 0) or (n % 2 == 0 and (n // 10) % 2 == 1):
		return True
	return False


"""
Solution 4
"""

def one_odd_one_even(n):
	f = int(str(n)[0]) % 2 == 0 and int(str(n)[1]) % 2 == 1
	s = int(str(n)[0]) % 2 == 1 and int(str(n)[1]) % 2 == 0
	return f or s




