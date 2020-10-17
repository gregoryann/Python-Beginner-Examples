"""
Extending The String

Make two functions:

consonants(word) which returns the number of consonants in a word when called.
vowels(word) which returns the number of vowels in a word when called.
Examples
vowels('Jameel SAEB') ➞ 5

consonants('He|\o mY Fr*end') ➞ 7

consonants("Smithsonian") ➞ 7
vowels("Smithsonian") ➞ 4

Notes
Vowels are: a, e, i, o, u.
Spaces and special character do not count as consonants nor vowels.
Check Resources for more info.
"""




################################################################
"""
Solution 1
"""


def consonants(word):
    return sum(c.lower() not in 'aeiou' for c in word if c.isalpha())

def vowels(word):
    return sum(c.lower() in 'aeiou' for c in word)




################################################################
"""
Solution 2
"""


def vowels(word):
		return sum(i.isalpha() and i in 'aeiou' for i in word.lower())

def consonants(word):
		return sum(i.isalpha() and i not in 'aeiou' for i in word.lower())





################################################################
"""
Solution 3
"""


def consonants(word):
	output = 0
	for i in word:
		if i.lower() in 'bcdfghjklmnpqrstvwxyz':
			output += 1
	return output
	
def vowels(word):
	output = 0
	for i in word:
		if i.lower() in 'aeiou':
			output += 1
	return output





#################################################################
"""
Solution 4
"""


import re
def consonants(word):
    word = ''.join(re.findall(r'[a-z]',word,re.I))
    return len(re.findall(r'[^aeiou]',word,re.I))


def vowels(word):
    return len(re.findall(r'[aeiou]', word, re.I))



