"""
Convert to Decimal Notation

Create a function to convert a list of percentages to their decimal equivalents.

Examples
convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]

convert_to_decimal(["45%", "32%", "97%", "33%"]) ➞ [0.45, 0.32, 0.97, 0.33]

convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) ➞ [0.33, 0.981, 0.5644, 1]
"""


"""
Solution 1
"""

def convert_to_decimal(perc):
	return [float(item[:-1])/100 for item in perc]

"""
Solution 2
"""

def convert_to_decimal(perc):
	return [float(item.strip("%")) * .01 for item in perc]

"""
Solution 3
"""

import re

def convert_to_decimal(perc):

    decimals = []

    for percentaje in perc:

        decimal = float(re.match(r'\d+\.*\d*', percentaje).group()) / 100
        decimals.append(decimal)

    return decimals

"""
Solution 4
"""

def convert_to_decimal(perc):
    mylist = []
    for decimal in perc:
        num = float(decimal[:decimal.index('%')])
        mylist.append(num/100)
    return mylist




