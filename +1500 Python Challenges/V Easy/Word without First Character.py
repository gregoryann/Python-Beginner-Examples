"""



Word without First Character
Create a function that takes a word and returns the new word without including the first character.

Examples
new_word("apple") ➞ "pple"

new_word("cherry") ➞ "herry"

new_word("plum") ➞ "lum"
Notes
The input is always a valid word.

"""






"""
Solution 1
"""

def new_word(word):
	return word[1:]





"""
Solution 2
"""

new_word = lambda w: w[1:]






