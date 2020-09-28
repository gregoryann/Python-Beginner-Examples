"""
Apples and Bananas

Write a function, that replaces all vowels in a string with a specified vowel.

Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"

Notes
All words will be lowercase. Y is not considered a vowel.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def vow_replace(txt, vowel):
	return "".join(vowel if i in 'aeiou' else i for i in txt)

"""
Solution 2
"""

import re

def vow_replace(word, vowel):
	return re.sub('[aeiou]', vowel, word)

"""
Solution 3
"""

def vow_replace(word, vowel):
	word = list(word)
	for i in range(len(word)):
		if word[i] in ['a','e','i','o','u']:
			word[i] = vowel
	return "".join(word)

"""
Solution 4
"""

def vow_replace(word, vowel):
	sto=""
	for x in word:
		if x in "aeiou":
			sto+=vowel
		else:
			sto+=x
	return sto




