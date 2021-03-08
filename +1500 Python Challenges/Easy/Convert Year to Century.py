"""
Convert Year to Century

Write a function that takes a year and returns its corresponding century.

Examples
century_from_year(2005) ➞ 21

century_from_year(1950) ➞ 20

century_from_year(1900) ➞ 19
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def century_from_year(year):
	return (year + 99) // 100

"""
Solution 2
"""

import math

def century_from_year(year):
		return math.ceil(year / 100)

"""
Solution 3
"""

import math

def century_from_year(year):
		if year % 100 == 0:
			return year // 100
		else:
			return year // 100 + 1

"""
Solution 4
"""

def century_from_year(year):
	c = year//100
	if year%100:
		c += 1
	return c

"""
Solution 5
"""

def century_from_year(year):
    s = str(year).zfill(4)
    if s[2:] == '00':
        return int(s[:2])
    else:
        return 1 + int(s[:2])


