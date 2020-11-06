"""
Palindromic Dates
The 2nd of February 2020 is a palindromic date in both dd/mm/yyyy and mm/dd/yyyy format (02/02/2020). Given a date in dd/mm/yyyy format, return True if the date is palindromic in both date formats, otherwise return False.

Examples
palindromic_date("02/02/2020") ➞ True

palindromic_date("11/12/2019") ➞ False

palindromic_date("11/02/2011") ➞ False
# Although 11/02/2011 is palindromic in dd/mm/yyyy format,
# it isn't in mm/dd/yyyy format (02/11/2011)

Notes
All dates will be valid in both date formats.
The date must be palindromic in both dd/mm/yyyy and mm/dd/yyyy formats to pass.
"""



################################################################
"""
Solution 1
"""


def palindromic_date(date):
    d, m, y = date.split('/')
    return (d+m)[::-1] == y and (m+d)[::-1] == y




################################################################
"""
Solution 2
"""


def palindromic_date(date):
	dd,mm,yyyy = date.split('/')
	date1 = ''.join([dd,mm,yyyy])
	date2 = ''.join([mm,dd,yyyy])
	return date1 == date1[::-1] and date2 == date2[::-1]




################################################################
"""
Solution 3
"""


def palindromic_date(date):
	l = date.split("/")
	l1 = [l[1], l[0], l[2]]
	return ''.join(l1)==''.join(l1)[::-1] and ''.join(l)==''.join(l)[::-1]




#################################################################
"""
Solution 4
"""


def palindromic_date(d):
	d = d.replace("/", "")
	return (d[:4] == d[:-5:-1]) and (d[2:4] + d[:2] == d[:-5:-1])



