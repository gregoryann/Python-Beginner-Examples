"""
Split a String Based on Vowels and Consonants
Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.

Examples
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"

Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).
"""


"""
Solution 1
"""

def split(txt):
	return ''.join(sorted(txt, key=lambda x: x.lower() not in 'aeiou'))

"""
Solution 2
"""

def split(txt):
	vowels = ''.join(ch for ch in txt if ch in 'aeiouAEIOU')
	others = ''.join(ch for ch in txt if ch not in 'aeiouAEIOU')
	return vowels+others

"""
Solution 3
"""

import re

def split(txt):
	vowels = ''.join(char for char in txt if char in 'aeiou')
	return vowels + re.sub('[aeiou]', '', txt)

"""
Solution 4
"""

def split(txt):
	is_vovel = "".join([i for i in txt if i.lower() in "aeoui"])
	res = "".join([i for i in txt if i.lower() not in "aeoui"])
	return is_vovel + res


"""
Solution 5
"""

split=lambda s:"".join([c for c in s if c.lower()in"aeiou"]+[c for c in s if c.lower()not in"aeiou"])

