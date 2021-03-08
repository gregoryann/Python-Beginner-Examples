"""
Is the String Odd or Even?
Given a string, return true if its length is even or false if the length is odd.

Examples
odd_or_even("apples") ➞ True

odd_or_even("pears") ➞ False

odd_or_even("cherry") ➞ True

"""


"""
Solution 1
"""

def odd_or_even(word):
	import string
	counter = 0
	for letter in word:
		if letter in string.ascii_lowercase:
			counter += 1
	return True if counter%2==0 else False


"""
Solution 2
"""

def odd_or_even(word):
	if len(word)%2 == 0:
		return True
	else:
		return False

"""
Solution 3
"""

def odd_or_even(str):
	if len(str) % 2 == 0:
		return True
	elif len(str) % 2 == 1:
		return False






