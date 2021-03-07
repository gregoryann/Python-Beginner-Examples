"""
Magic Date

You are to read each part of the date into its own integer type variable. The year should be a 4 digit number. You can assume the user enters a correct date (no error checking required).

Determine whether the entered date is a magic date. Here are the rules for a magic date:

mm * dd is a 1-digit number that matches the last digit of yyyy or
mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
mm * dd is a 3-digit number that matches the last 3 digits of yyyy
The program should then display True if the date is magic, or False if it is not.

Examples
magic("1 1 2011") ➞ True

magic("4 1 2001") ➞ False

magic("5 2 2010") ➞ True

magic("9 2 2011") ➞ False
"""



################################################################
"""
Solution 1
"""


def magic(txt):
	m, d, y = txt.split()
	return y.endswith(str(int(m) * int(d)))






################################################################
"""
Solution 2
"""

def magic(txt):
	month, day, year = [int(txt[:2]),int(txt[2:4]),txt[5:]]
	return True if year.endswith(str(month*day)) else False


################################################################
"""
Solution 3
"""

import re

def magic(s):

    date = re.search(r'(\d+)\s(\d+)\s(\d+)', s)
    day, month, year = int(date.group(1)), int(date.group(2)), date.group(3)
    dd_mm = str(day * month)

    if dd_mm == year[-len(dd_mm):]:
        return True
    else:
        return False




#################################################################
"""
Solution 4
"""

def magic(txt):
	d = txt.split(' ')
	r = str(int(d[0]) * int(d[1]))
	return True if \
		 (len(r) == 1 and r == d[2][-1]) \
			or (len(r) == 2 and r == d[2][-2:]) \
			or (len(r) == 3 and r == d[2][-3:]) \
			else False



#################################################################
"""
Solution 5
"""


def magic(txt):
	dt = txt.replace(' ','')
	md = int(dt[0]) * int(dt[1])
	yy = dt[-1*len(str(md)):]
	if md == int(yy):
		return True
	return False