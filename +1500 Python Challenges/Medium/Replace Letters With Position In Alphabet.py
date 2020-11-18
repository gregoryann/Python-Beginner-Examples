"""
Replace Letters With Position In Alphabet

Create a function that takes a string and replaces each letter with its appropriate position in the alphabet. "a" is 1, "b" is 2, "c" is 3, etc, etc.

Examples
alphabet_index("Wow, does that work?")
➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"

alphabet_index("The river stole the gods.")
➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"

alphabet_index("We have a lot of rain in June.")
➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"


Notes
If any character in the string isn't a letter, ignore it.
"""



################################################################
"""
Solution 1
"""


def alphabet_index(txt):
	return ' '.join([str(ord(x) - ord('a') + 1) for x in txt.lower() if x.isalpha()])



################################################################
"""
Solution 2
"""


def alphabet_index(txt):
	alpha='abcdefghijklmnopqrstuvwxyz'
	ret = []
	for c in txt:
		if c.isalpha(): ret.append(str(alpha.index(c.lower())+1))
	return ' '.join(ret)


################################################################
"""
Solution 3
"""


def alphabet_index(txt):
	return_string = ""
	for letter in txt.lower():
		if ord(letter) >= 97 and ord(letter) <= 122:
			return_string = return_string + str(ord(letter)-96) + " "
	return return_string[:-1]



#################################################################
"""
Solution 4
"""


import string

string = string.ascii_lowercase

def alphabet_index(str1):
    return " ".join(list(map(str,[string.index(char)+1 for char in str1.lower() if char in string])))





