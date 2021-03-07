"""
Check if the String is a Palindrome

A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward, such as madam or kayak.

Write a function that takes a string and determines whether it's a palindrome or not. The function should return a boolean (True or False value).

Examples
is_palindrome("Neuquen") ➞ True

is_palindrome("Not a palindrome") ➞ False

is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!") ➞ True

Notes
Should be case insensitive.
Special characters (punctuation or spaces) should be ignored.
"""





#############################################################
"""
Solution 1
"""

def is_palindrome(txt):
  check = [s.lower() for s in txt if s.isalpha()]
  return check[::-1] == check




#############################################################
"""
Solution 2
"""

def is_palindrome(txt):
  plaintxt = (''.join(filter(lambda c: c.isalpha(), txt))).lower()
  return plaintxt == plaintxt[::-1]





#############################################################
"""
Solution 3
"""

def is_palindrome(txt):
	b=""
	a="abcdefghijklmnopqrstuvwxyz"
	for x in txt:
		if x.lower() in a:
			b+=x.lower()
	if b == b[::-1]:
		return True
	return False





#############################################################
"""
Solution 4
"""

import re
def is_palindrome(txt):
	txt.strip(" ")
	match = re.sub(r'[^a-zA-Z0-9\.]', "", txt)
	if match.lower()[::-1] == match.lower():
		return True
	else:
		return False




#############################################################
"""
Solution 5
"""

def is_palindrome(txt):
  import re
  return re.sub(r'[\W_]+', '', txt.lower()) == re.sub(r'[\W_]+', '', txt.lower()[::-1])