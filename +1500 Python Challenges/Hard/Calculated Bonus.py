"""
Calculated Bonus

A financial institution provides professional services to banks and claims charges from the customers based on the number of man-days provided. Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization and revenues by paying a bonus for each day claimed from customers in excess of a threshold target.

This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day in excess of such threshold target is shown as follows:

Days	Bonus
0 to 32 days	Zero
33 to 40 days	SGD$325 per billable day
41 to 48 days	SGD$550 per billable day
Greater than 48 days	SGD$600 per billable day
Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in a quarter, his/her incentive payment is computed as follows:

32*0 + 8*325 + 5*550 = 5350
Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.

Examples
bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200
"""



################################################################
"""
Solution 1
"""


def bonus(days):
    total = 0
    for i in range(1, days+1):
        if 32 < i <= 40:
            total += 325
        if 40 < i <= 48:
            total += 550
        if i > 48:
            total += 600
    return total






################################################################
"""
Solution 2
"""


def bonus(days):
	if days <= 32:
		return 0
	if days <= 40:
		return (days - 32) * 325
	if days <= 48:
		return (days - 40) * 550 + 8 * 325
	return (days - 48) * 600 +  8 * 550 + 8 * 325





################################################################
"""
Solution 3
"""


def bonus(days):
	return sum(([0]*33+[325]*8+[550]*8+[600]*2)[:days+1])




