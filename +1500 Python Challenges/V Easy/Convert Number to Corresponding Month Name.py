"""

Convert Number to Corresponding Month Name

Create a function that takes a number (from 1 to 12) and returns its corresponding month name as a string. For example, if you're given 3 as input, your function should return "March", because March is the 3rd month.

Number	Month Name
1	January
2	February
3	March
4	April
5	May
6	June
7	July
8	August
9	September
10	October
11	November
12	December
Examples
month_name(3) ➞ "March"

month_name(12) ➞ "December"

month_name(6) ➞ "June"

Notes
You can expect only integers ranging from 1 to 12 as test input.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


"""
Solution 1
"""

import calendar
def month_name(num):
	return calendar.month_name[num]

"""
Solution 2
"""

def month_name(num):
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	return months[num-1]

"""
Solution 3
"""

def month_name(num):
		switcher = {
		1: 'January',
		2: 'February',
		3: 'March',
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'August',
		9: 'September',
		10: 'October',
		11: 'November',
		12: 'December'
		}
		return switcher.get(num,'Invalid month')

"""
Solution 4
"""

def month_name(num):
	months = {'1': 'January',
			  '2': 'February',
			  '3': 'March',
			  '4': 'April',
			  '5': 'May',
			  '6': 'June',
			  '7': 'July',
			  '8': 'August',
			  '9': 'September',
			  '10': 'October',
			  '11': 'November',
			  '12': 'December',}
	return months[str(num)]


"""
Solution 5
"""

from datetime import datetime
def month_name(num):
	dt = datetime.strptime(str(num), "%m")
	return dt.strftime("%B")



