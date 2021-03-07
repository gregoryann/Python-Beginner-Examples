"""
Move Capital Letters to the Front

Create a function that moves all capital letters to the front of a word.

Examples
cap_to_front("hApPy") ➞ "APhpy"

cap_to_front("moveMENT") ➞ "MENTmove"

cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

Notes
Keep the original relative order of the upper and lower case letters the same.
"""



"""
Solution 1
"""

def cap_to_front(s):
	return ''.join(sorted(s, key=str.isupper, reverse=True))

"""
Solution 2
"""

def cap_to_front(s):
	uppers = [i for i in s if i.isupper()]
	lowers = [i for i in s if i.islower()]
	return "".join(uppers + lowers)

"""
Solution 3
"""

def cap_to_front(s):
	o = ["",""]
	for i in s:
		o[i.islower()] += i
	return "".join(o)

"""
Solution 4
"""

import re

def cap_to_front(s):
    capitals = re.findall(r'[A-Z]+', s)
    lowers = re.findall(r'[a-z]+', s)
    return ''.join(capitals + lowers)


"""
Solution 5
"""


def cap_to_front(s):
	ups = []
	low = []
	for c in s:
		if c.isupper(): ups.append(c)
		if c.islower(): low.append(c)
	return ''.join(ups+low)
