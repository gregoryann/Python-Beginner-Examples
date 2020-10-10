"""
Find the Discount

Create a function that takes two arguments: the final price and the discount as integers and returns the final price after the discount.

Alternative Text

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
"""




################################################################
"""
Solution 1
"""


def dis(price, discount):
	return price * (100 - discount) * 0.01





################################################################
"""
Solution 2
"""


dis = lambda p, d: round(p * (1 - d / 100), 2)






################################################################
"""
Solution 3
"""


def dis(price, discount):return round(price - price*(discount/100), 2)







#################################################################
"""
Solution 4
"""

def dis(price, discount):
	percentage = discount/100
	pricediscount = price * percentage
	newprice = price - pricediscount
	return round(newprice,2)




