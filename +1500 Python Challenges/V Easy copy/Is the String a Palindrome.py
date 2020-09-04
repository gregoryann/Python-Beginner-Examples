"""
Is the String a Palindrome?
A palindrome is a word that is identical forward and backwards.

mom
racecar
kayak
Given a word, create a function that checks whether it is a palindrome.

Examples
is_palindrome("mom") ➞ True

is_palindrome("scary") ➞ False

is_palindrome("reviver") ➞ True

is_palindrome("stressed") ➞ False
Notes
All test input is lower cased.

"""



"""
Solution 1
"""

def is_palindrome(txt):
		return txt == txt[::-1]

"""
Solution 2
"""

def is_palindrome(txt):
	return True if (txt == txt[::-1]) else False



