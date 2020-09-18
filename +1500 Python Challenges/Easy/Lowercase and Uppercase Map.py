"""
Lowercase and Uppercase Map

Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.

Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }

mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }

mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes
All of the letters in the input list will always be lowercase.
"""


"""
Solution 1
"""

def mapping(letters):
	return {i:i.upper() for i in letters}

"""
Solution 2
"""

def mapping(letters):
	dict = {}
	for letter in letters:
		dict[letter.lower()] = letter.upper()
	return dict

"""
Solution 3
"""

def mapping(letters):
	return {ch:ch.upper() for ch in letters}

"""
Solution 4
"""

def mapping(letters):
	dict = {}
	for x in letters:
		dict_2 = {x: chr(ord(x)-32)}
		dict.update(dict_2)
	return dict




