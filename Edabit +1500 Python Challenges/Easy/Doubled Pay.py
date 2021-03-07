"""
Doubled Pay

An employee working at a very bizzare company, earns one penny on their first day. However, for every day that passes, their base amount doubles, so they earn two pennies on the second day and four pennies on the third day (totalling 7 pennies). Given a number of days, return how many pennies the employee accumulates.

Examples
doubled_pay(1) ➞ 1

doubled_pay(2) ➞ 3

doubled_pay(3) ➞ 7

Notes
You will only get tests for valid positive integers.
"""





################################################################
"""
Solution 1
"""

def doubled_pay(n):
	sum = 0
	temp = 1
	for i in range(1,n+1):
		sum += temp
		temp *= 2
	return sum




################################################################
"""
Solution 2
"""

def doubled_pay(n):
	a = 0
	for x in range(0, n):
		a += 2**x
	return(a)





################################################################
"""
Solution 3
"""

def doubled_pay(n):
	nums = [1]
	count = 1
	for i in range(1, n):
		if n > 1:
			count *= 2
			nums.append(count)
		else:
			return count
	return sum(nums)





#################################################################
"""
Solution 4
"""



doubled_pay = lambda n: sum(2**i for i in range(n))


