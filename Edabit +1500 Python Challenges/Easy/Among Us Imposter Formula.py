"""

Among Us Imposter Formula

Create a function that calculates the chance of being an imposter. The formula for the chances of being an imposter is 100 × (i / p) where i is the imposter count and p is the player count. Make sure to round the value to the nearest integer and return the value as a percentage.

Examples
imposter_formula(1, 10) ➞ "10%"

imposter_formula(2, 5) ➞ "40%"

imposter_formula(1, 8) ➞ "13%"

Notes
The player limit is 10 and the imposter count can only go up to 3.
"""




################################################################
"""
Solution 1
"""

def imposter_formula(i, p):
		return '{:.0%}'.format(i/p)



################################################################
"""
Solution 2
"""

def imposter_formula(i, p):return str(round(((float(i)/p)*100)))+'%'



################################################################
"""
Solution 3
"""

imposter_formula = lambda i,p: str(round(100*(i/p))) + '%'





#################################################################
"""
Solution 4
"""

def imposter_formula(i, p):
	return "{}%".format(str(round(100 * (i/p))))




#################################################################
"""
Solution 5
"""

import math
def imposter_formula(i, p):
	if p > 10 or i > 3:
		print("Error!")
	else:
		formula = 100 * (i/p)
		formula = round(formula)
		return str(formula)+"%"