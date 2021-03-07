"""
Return the Index of the First Vowel

Create a function that returns the index of the first vowel in a string.

Examples
first_vowel("apple") ➞ 0

first_vowel("hello") ➞ 1

first_vowel("STRAWBERRY") ➞ 3

first_vowel("pInEaPPLe") ➞ 1

Notes
Input will be single words.
Characters in words will be upper or lower case.
"y" is not considered a vowel.
Input always contains a vowel.

"""


"""
Solution 1
"""

def first_vowel(txt):
	return [txt.index(x) for x in txt if x.lower() in 'aeiou'][0]

"""
Solution 2
"""

def first_vowel(txt):
	for i in range(len(txt)):
		if txt[i].lower() in 'aeiou':
			return i

"""
Solution 3
"""

import re
def first_vowel(s):
	return re.search(r'[aeiou]', s.lower()).span()[0]

"""
Solution 4
"""

def first_vowel(txt):
	txt = txt.lower()
	for i in txt:
		if i in  ('a', 'e', 'i', 'o', 'u'):
			return txt.index(i)




