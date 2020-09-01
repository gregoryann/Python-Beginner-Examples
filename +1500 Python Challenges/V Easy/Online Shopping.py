"""
Online Shopping
Create a function that determines whether a shopping order is eligible for free shipping. An order is eligible for free shipping if the total cost of items purchased exceeds $50.00.

Examples
free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 }) ➞ False

free_shipping({ "Flatscreen TV": 399.99 }) ➞ True

free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }) ➞ True
Notes
Ignore tax or additional fees when calculating the total order cost.

"""


"""
Solution 1
"""

def free_shipping(order):
	return sum(order.values())>=50


"""
Solution 2
"""

def free_shipping(order):
	tot = 0
	for k,v in order.items():
		tot += v
	return tot >= 50


"""
Solution 3
"""

def free_shipping(order):

    total_value = sum([value for value in order.values()])
    
    return total_value > 50


"""
Solution 4
"""

def free_shipping(order):
	sum = 0
	for x in order.values():
		sum += x
	return sum > 50




