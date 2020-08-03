"""

Compare Strings by Count of Characters
Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

Examples
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""


def comp(txt1, txt2):
	return len(txt1) == len(txt2)


"""
Solution 2
"""


def comp(a,b):
	return len(a) is len(b)


"""
Solution 3
"""


def comp(txt1, txt2):
	if len(txt1) == len(txt2):
		return True
	return False


"""
Solution 4
"""

def comp(txt1, txt2):
	if len(txt1)==len(txt2):
		return True
	else:
		return False




