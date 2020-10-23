"""
Length of Worm

Given a string worm create a function that takes the length of the worm and converts it into millimeters. Each - represents one centimeter.

Examples
worm_length("----------") ➞ "100 mm."

worm_length("") ➞ "invalid"

worm_length("---_-___---_") ➞ "invalid"

Notes
Return "invalid" if an empty string is given or if the string has characters other than -.
"""


################################################################
"""
Solution 1
"""


def worm_length(worm):
	return ('{} mm.'.format(10 * len(worm)) if
		set(worm) == {'-'} else 'invalid')



################################################################
"""
Solution 2
"""


def worm_length(worm):
	if worm == "":
		return "invalid"
	for x in worm:
		if x != "-":
			return "invalid"
	return str(len(worm) * 10) + " mm."





################################################################
"""
Solution 3
"""


def worm_length(worm):
	if not worm or worm != '-'*len(worm):
		return 'invalid'
	return '{} mm.'.format(str(10*len(worm)))




#################################################################
"""
Solution 4
"""


def worm_length(worm):
	return 'invalid' if any(i!='-' for i in worm) or not worm else str(len(worm)*



#################################################################
"""
Solution 5
"""

def worm_length(worm):
	if not worm.count('-') == len(worm) or worm.count('-') == 0:
		return 'invalid'
	return str(str(worm.count('-') * 10) + ' mm.')




#################################################################
"""
Solution 6
"""

worm_length=lambda w:["invalid","%d0 mm."%len(w)][set(w)=={"-"}]