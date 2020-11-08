"""
Calculate the Profit

You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar.

Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030

Notes
Assume all inventory has been sold.
Profit = Total Sales - Total Cost
"""




################################################################
"""
Solution 1
"""


def profit(info):
	[a, b, c]=info.values()
	return round((b-a)*c)



################################################################
"""
Solution 2
"""


def profit(info):
	return round((info["inventory"])*(info["sell_price"] - info["cost_price"]))




################################################################
"""
Solution 3
"""


def profit(info):
  return round(info.get("sell_price") * info.get("inventory") - info.get("cost_price") * info.get("inventory"))



#################################################################
"""
Solution 4
"""


def profit(info):
    total_cost = info["cost_price"] * info["inventory"]
    total_sales = info["sell_price"] * info["inventory"]
    profit = total_sales - total_cost
    return int(round(profit))



