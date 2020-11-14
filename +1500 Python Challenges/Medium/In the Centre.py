"""
In the Centre?

Given a string containing mostly spaces and one non-space character, return whether the character is positioned in the very centre of the string. This means the number of spaces on both sides should be the same.

Examples
is_central("  #  ") ➞ True

is_central(" 2    ") ➞ False

is_central("@") ➞ True

Notes
Only one character other than spaces will be given at a time.
"""



################################################################
"""
Solution 1
"""


def is_central(txt):
	return txt == txt[::-1]



################################################################
"""
Solution 2
"""


def is_central(txt):
	return len(txt)%2 and txt[len(txt)//2] != ' '



################################################################
"""
Solution 3
"""


def is_central(txt):
	a = len(txt.rstrip())
	b = len(txt.lstrip())
	return a == b



#################################################################
"""
Solution 4
"""


import re
def is_central(txt):
	spcs = re.findall(r'\s+', txt)
	return len(txt) == 1 or (len(spcs) == 2 and len(spcs[0]) == len(spcs[1]))



