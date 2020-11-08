"""
Adding Numbers

Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"

Notes
If any input is "" or None, return "Invalid Operation".
"""


################################################################
"""
Solution 1
"""


def add(a,b):
	try:return str(int(a)+int(b))
	except:return'Invalid Operation'



################################################################
"""
Solution 2
"""


import re
def add(s1, s2):
    return (str(int(s1) + int(s2)) if type(s1) == str and type(s2) == str and
            bool(re.match(r'-*\d+$', s1)) and bool(re.match(r'-*\d+$', s2))
            else 'Invalid Operation')


################################################################
"""
Solution 3
"""


def add(n1, n2):
	lon = [n1, n2]
	if '' in lon or None in lon:
		return "Invalid Operation"
	return str(int(n1) + int(n2))



#################################################################
"""
Solution 4
"""


def add(n1, n2):
	return str(int(n1)+int(n2)) if n1 and n2 and all([i.isdigit() or i=='-' for i in n1]) and all([i.isdigit() or i=='-' for i in n2]) else 'Invalid Operation'




