"""
Check Factors

Write a function that returns True if all integers in a list are factors of a number, and False otherwise.

Examples
check_factors([2, 3, 4], 12) ➞ True
# Since 2, 3, and 4 are all factors of 12.

check_factors([1, 2, 3, 8], 12) ➞ False
# 8 is not a factor of 12.

check_factors([1, 2, 50], 100) ➞ True

check_factors([3, 6], 9) ➞ False

"""



"""
Solution 1
"""

def check_factors(factors, num):
	return all([num%i == 0 for i in factors])

"""
Solution 2
"""

def check_factors(factors, num):
	return sum(num%f for f in factors) == 0

"""
Solution 3
"""

def check_factors(factors, num):
	for i in factors:
		if num % i != 0:
			return False
			
	return True

"""
Solution 4
"""

def check_factors(factors, num):
	true_factors = [x for x in factors if num % x == 0]
	return True if len(true_factors) == len(factors) else False




