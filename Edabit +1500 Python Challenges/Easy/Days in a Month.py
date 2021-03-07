"""
Days in a Month

Create a function that takes the month and year (as integers) and returns the number of days in that month.

Examples
days(2, 2018) ➞ 28

days(4, 654) ➞ 30

days(2, 200) ➞ 28

days(2, 1000) ➞ 28

Notes
Don't forget about leap years!
"""





################################################################
"""
Solution 1
"""

def day_amount(month, year):
	if month in (1,3,5,7,8,10,12):
		return 31
	elif month in (4,6,9,11):
		return 30
	else: # month == 2
		if any([year % 4 == 0 and not year % 100 == 0, year % 400 == 0 ]):
			return 29
		else:
			return 28





################################################################
"""
Solution 2
"""

def day_amount(month, year):
	days = {1: 31,
			2: 28,
			3: 31,
			4: 30,
			5: 31,
			6: 30,
			7: 31,
			8: 31,
			9: 30,
			10: 31,
			11: 30,
			12: 31}
	if month == 2:
		if year % 4 == 0:
			if year % 100 == 0: 
				if year % 400 == 0:
					return days[month] + 1
				return days[month]
			return days[month] + 1
	return days[month]







################################################################
"""
Solution 3
"""

import calendar
def day_amount(month, year):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif month != 2:
		return 30
	else:
		return 28 if not calendar.isleap(year) else 29





#################################################################
"""
Solution 4
"""

import calendar
def day_amount(month, year):
	return calendar.monthrange(year,month)[1]




