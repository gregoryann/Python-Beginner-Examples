"""
Extend the Vowels

Create a function that takes a word and extends all vowels by a number num.

Examples
extend_vowels("Hello", 5) ➞ "Heeeeeelloooooo"

extend_vowels("Edabit", 3) ➞ "EEEEdaaaabiiiit"

extend_vowels("Extend", 0) ➞ "Extend"
"""


################################################################
"""
Solution 1
"""


def extend_vowels(word, num):
    if num < 0 or type(num) is not int:
        return "invalid"
    return "".join(c * (num + 1) if c in "aeiouAEIOU" else c for c in word)



################################################################
"""
Solution 2
"""


def extend_vowels(word, num):
	return "".join(x+x*num if x.lower() in 'aeiou' else x for x in word) if type(num) is int and num >= 0 else "invalid"



################################################################
"""
Solution 3
"""


def extend_vowels(word, num):
	print(num)
	print(word)
	voyelle=["a", "e", "i", "o", "u", "y"]
	wordfinal=""
	if type(num)==int and num>=0:
		for i in range(len(word)):
			letter=word[i]
			if letter in voyelle or letter.lower() in voyelle:
				wordfinal+=letter*(num+1)
			else:
				wordfinal+=letter
	else:
		wordfinal="invalid"
	return wordfinal



#################################################################
"""
Solution 4
"""


import re

def extend_vowels(word, num):
	return re.sub(
		'[aeiouAEIOU]', 
		lambda x: (num + 1) * x.group(), 
		word
	) if not num % 1 and num >= 0 else 'invalid'



