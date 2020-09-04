"""

Check String for Spaces
Create a function that returns True if a string contains any spaces.

Examples
has_spaces("hello") ➞ False

has_spaces("hello, world") ➞ True

has_spaces(" ") ➞ True

has_spaces("") ➞ False

has_spaces(",./!@#") ➞ False
Notes
An empty string does not contain any spaces.
Try doing this without RegEx.


"""






"""
Solution 1
"""


def has_spaces(txt):
	return " " in txt




"""
Solution 2
"""

def has_spaces(txt):
	return txt.count(' ')>=1



"""
Solution 3
"""

def has_spaces(txt):
	for char in txt:
		if char == ' ':
			return True
	return False



"""
Solution 4

"""

def has_spaces(txt):
	x = txt.split(" ")
	x = len(x)
	if x == 1:
		return False
	elif x > 1:
		return True






