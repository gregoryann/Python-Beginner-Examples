"""
Halloween Day
Create a function that takes date in the format yyyy/mm/dd as an input and returns "Bonfire toffee" if the date is October 31, else return "toffee".

Examples
halloween("2013/10/31") ➞ "Bonfire toffee"

halloween("2012/07/31") ➞ "toffee"

halloween("2011/10/12") ➞ "toffee"
"""



"""
Solution 1
"""

def halloween(dt):
	return 'Bonfire toffee' if dt[4:] == '/10/31' else 'toffee'

"""
Solution 2
"""

import re
def halloween(dt):
	x = re.findall(r'(\d\d\d\d)/(\d\d)/(\d\d)',dt)
	print(x[0])
	if int(x[0][1]) == 10 and int(x[0][2]) == 31:
		return "Bonfire toffee"
	else:
		return "toffee"

"""
Solution 3
"""

halloween=lambda x:"Bonfire toffee" if all([x.split("/")[2]=="31",x.split("/")[1]=="10"]) else "toffee"

"""
Solution 4
"""

def halloween(dt):
		return 'Bonfire toffee' if dt.endswith('10/31') else 'toffee'


"""
Solution 5
"""

def halloween(dt):
    date = dt
    if date[8:10] == "31" and date[5:7] == "10":
        return "Bonfire toffee"
    else:
        return "toffee"



"""
Solution 6
"""

import datetime
def halloween(dt):
    dt = list(map(lambda x: int(x), dt.split('/')))
    date = datetime.datetime(dt[0], dt[1], dt[2])
    return "Bonfire toffee" if date.strftime('%b') == 'Oct' and date.strftime('%d') == '31' else 'toffee'