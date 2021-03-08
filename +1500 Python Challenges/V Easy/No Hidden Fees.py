"""

No Hidden Fees

Given a list of prices prices and a "supposed" total t, return True if there is a hidden fee added to the total (i.e. the total is greater than the sum of prices), otherwise return False.

Examples
has_hidden_fee(["$2", "$4", "$1", "$8"], "$15") ➞ False
has_hidden_fee(["$1", "$2", "$3"], "$6") ➞ False
has_hidden_fee(["$1"], "$4") ➞ True

Notes
Remember that each price is given as a string.
All $ signs will be at the beginning of the number.

"""


"""
Solution 1
"""

def has_hidden_fee(prices, t):
	return sum([int(i[1:]) for i in prices]) < int(t[1:])

"""
Solution 2
"""

def has_hidden_fee(prices, t):
	c = []
	for each in prices: 
		c.append(int(each.replace("$","")))
	return sum(c) != int(t.replace("$", ""))

"""
Solution 3
"""

def has_hidden_fee(prices, t):
	b = []
	for x in prices:
		b.append(int(x[1:]))
	return sum(b) != int(t[1:])

"""
Solution 4
"""

def has_hidden_fee(prices, t):
	return int(t[1:]) > sum(map(lambda x: int(x[1:]), prices))




