"""

Convenience Store
Given a total due and a list representing the amount of change in your pocket, determine whether or not you are able to pay for the item. Change will always be represented in the following order: quarters, dimes, nickels, pennies.

To illustrate: change_enough([25, 20, 5, 0], 4.25) should yield True, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.

Examples
change_enough([2, 100, 0, 0], 14.11) ➞ False

change_enough([0, 0, 20, 5], 0.75) ➞ True

change_enough([30, 40, 20, 5], 12.55) ➞ True

change_enough([10, 0, 0, 50], 3.85) ➞ False

change_enough([1, 0, 5, 219], 19.99) ➞ False


Notes
quarter: 25 cents / $0.25
dime: 10 cents / $0.10
nickel: 5 cents / $0.05
penny: 1 cent / $0.01

"""


"""
Solution 1
"""

def change_enough(change, amount_due):
	values = [0.25, 0.1, 0.05, 0.01]
	return sum([a*b for a, b in zip(change, values)]) >= amount_due

"""
Solution 2
"""

def change_enough(change, amount_due):

    total = ((change[0] * 25) + (change[1] * 10) + (change[2] * 5) + (change[3] * 1)) / 100

    return total >= amount_due

"""
Solution 3
"""


def change_enough(change, amount_due):
	sum = 0
	sum = (change[0] * .25) + (change[1] * .1) + (change[2] * .05) + (change[3] * .01) + sum
	if sum < amount_due:
		return(False)
	else:
		return(True)


"""
Solution 4
"""

def change_enough(change, amount_due):
	pennies_change = change[3] + change[2] * 5 + change[1] * 10 + change[0] * 25
	pennies_other = amount_due * 100
	return pennies_change >= pennies_other




