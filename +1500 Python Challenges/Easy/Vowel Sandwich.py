"""
Vowel Sandwich

Create a function which validates whether a 3 character string is a vowel sandwich. In order to have a valid sandwich, the string must satisfy the following rules:

The first and last characters must be a consonant.
The character in the middle must be a vowel.
Examples
is_vowel_sandwich("cat") ➞ True

is_vowel_sandwich("ear") ➞ False

is_vowel_sandwich("bake") ➞ False

is_vowel_sandwich("try") ➞ False

Notes
Return False if the word is not 3 characters in length.
All words will be given in lowercase.
y is not considered a vowel.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

import re

def is_vowel_sandwich(s):
	return bool(re.match(r'[^aeiou][aeiou][^aeiou]\Z', s))


"""
Solution 2
"""

def is_vowel_sandwich(s):
	return [0, 1, 0] == [1 if l in 'aeiou' else 0 for l in s]

"""
Solution 3
"""

def is_vowel_sandwich(s):
	if len(s) != 3:
		return (False)

	vowel = ['a', 'e', 'i', 'o', 'u']

	for i in s:
		if s[0] not in vowel and s[1] in vowel and s[2] not in vowel:
			return (True)
	return (False)


"""
Solution 4
"""

import re
def is_vowel_sandwich(s):
	vowels = 'aeiou'
	if len(s) != 3:
		return False
	if not re.match('[a-z]',s[0]) or s[0] in vowels:
		return False
	if s[1] not in vowels:
		return False
	if not re.match('[a-z]',s[2]) or s[2] in vowels:
		return False
	return True





