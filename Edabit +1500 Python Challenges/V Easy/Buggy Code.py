"""
Buggy Code
The challenge is to try and fix this buggy code, given the inputs True and False. See the examples below for the expected output.

Examples
has_bugs(True) ➞ "sad days"

has_bugs(False) ➞ "it's a good day"
Notes
Don't overthink this challenge, it's meant to be very simple! ;)

"""


"""
Solution 1
"""

def has_bugs(buggy_code):
	if buggy_code:
		return "sad days"
	else:
		return "it's a good day"

"""
Solution 2
"""

def has_bugs(b):
	return 'sad days' if b else 'it\'s a good day'

"""
Solution 3
"""

def has_bugs(buggy_code):
	a="sad days"
	b="it's a good day"
	if buggy_code==True:
		return a
	else:
		return b

"""
Solution 4
"""






