"""
Get the Century

Create a function that takes in a year and returns the correct century.

Examples
century(1756) ➞ "18th century"

century(1555) ➞ "16th century"

century(1000) ➞ "10th century"

century(1001) ➞ "11th century"

century(2005) ➞ "21st century"

Notes
All years will be between 1000 and 2010.
The 11th century is between 1001 and 1100.
The 18th century is between 1701-1800.
"""





################################################################
"""
Solution 1
"""

def century(year):
	century_no = str((year + 99 ) // 100)
	return '21st century' if century_no == '21' else century_no + 'th century'





################################################################
"""
Solution 2
"""

century=lambda y:str(y+99)[:2]+["th","st"][y>2000]+" century"







################################################################
"""
Solution 3
"""

def century(year):
    century = (year // 100) + 1 if (year % 100 != 0) else (year // 100)
    suffix = 'th' if century <= 20 else 'st'
    return '{}{} century'.format(century, suffix)









#################################################################
"""
Solution 4
"""


def century(year):
	if year % 100 == 0:
		century = year/100
	else:
		century = year//100 + 1
	
	if century < 21:
		return "%dth century" % century
	else:
		return "%dst century" % century







#################################################################
"""
Solution 5
"""


import math
def ordinal(number):
	sn = int(str(number)[-2:])

	if   sn in (11, 12, 13): return 'th'
	elif sn % 10 == 1:       return 'st'
	elif sn % 10 == 2:       return 'nd'
	elif sn % 10 == 3:       return 'rd'
	else:                    return 'th'
	
def century(year):
	century = math.ceil(year / 100)
	return '{0}{1} century'.format(century, ordinal(century))







#################################################################
"""
Solution 6
"""


def century(year):
	if year>=1000: year=str(year+100-1)[:2]
	else: year=str(year+100-1)[0]
	if year[-1]=='1' and year!='11': return year+'st century'
	elif year[-1]=='2': return year+'nd century'
	elif year[-1]=='3': return year+'rd century'
	else: return year+'th century'