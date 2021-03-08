"""
Profit Margin

Create a function that calculates the profit margin given cost_price and sales_price. Return the result as a percentage formated string, and rounded to one decimals. To calculate profit margin you subtract the cost from the sales price, then divide by salesprice.

Examples
profit_margin(50, 50) ➞ "0.0%"

profit_margin(28, 39) ➞ "28.2%"

profit_margin(33, 84) ➞ "60.7%"

Notes
Remember to return the result as a percentage formated string.
Only one decimal should be included.

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def profit_margin(cost_price, sales_price):
	return '{:.1%}'.format((sales_price - cost_price)/sales_price)

"""
Solution 2
"""

profit_margin=lambda c,s:str(round((s-c)/s*100,1))+'%'

"""
Solution 3
"""

def profit_margin(cost_price, sales_price):
    return str(round((sales_price - cost_price) / sales_price*100,1))+'%'

"""
Solution 4
"""

def profit_margin(cost_price, sales_price):
	pm = (sales_price - cost_price) / sales_price
	return '{0:.1%}'.format(pm)

"""
Solution 5
"""

def profit_margin(cost_price, sales_price):
	return '{:.1f}%'.format((1-(cost_price/sales_price))*100)

"""
Solution 6
"""

def profit_margin(cost_price, sales_price):
	val = ((sales_price-cost_price)/sales_price) * 100
	res = round(val, 1)
	return ('{}%'.format(res))