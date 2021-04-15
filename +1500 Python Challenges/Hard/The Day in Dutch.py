"""
The Day in Dutch

Write a method that when passed a date as "dd mm yyyy" and returns the date's weekday name in the Dutch culture.

Examples
weekday_dutch("21 9 1970") ➞ "maandag"

weekday_dutch(new DateTime("2 9 1945") ➞ "zondag"

weekday_dutch(new DateTime("9 11 2001") ➞ "dinsdag"

Notes
Check the Resources tab for help.
You can assume the specified date is valid.
"""



################################################################
"""
Solution 1
"""


from time import strptime
dutch_days = ['maandag', 'dinsdag', 'woensdag', 'donderdag',
              'vrijdag', 'zaterdag', 'zondag']
def weekday_dutch(date):
    return dutch_days[strptime(date, '%d %m %Y').tm_wday]




################################################################
"""
Solution 2
"""


from datetime import date

dow = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
def weekday_dutch(dd):
	d, m, y = map(int, dd.split())
	return dow[date(y, m, d).weekday()]




################################################################
"""
Solution 3
"""


import datetime 
import calendar 
def weekday_dutch(date):
    translate = {'Monday':'maandag','Wednesday':'woensdag','Thursday':'donderdag','Tuesday':'dinsdag','Friday':'vrijdag','Saturday':'zaterdag','Sunday':'zondag'}
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return translate[calendar.day_name[born]]




################################################################
"""
Solution 4
"""


def weekday_dutch(date):
    import datetime
    list1=date.split(' ')
    day1=datetime.date(int(list1[2]),int(list1[1]),int(list1[0])).isoweekday()
    if day1 == 1:
        return 'maandag'
    elif day1 == 2:
        return 'dinsdag'
    elif day1 == 3:
        return 'woensdag'
    elif day1 == 4:
        return 'donderdag'
    elif day1 == 5:
        return 'vrijdag'
    elif day1 == 6:
        return 'zaterdag'
    elif day1 == 7:
        return 'zondag'



