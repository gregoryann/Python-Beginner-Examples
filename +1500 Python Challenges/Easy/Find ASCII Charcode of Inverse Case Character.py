"""
Find ASCII Charcode of Inverse Case Character

Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65

Notes
The argument will always be a single character.
Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.
"""


"""
Solution 1
"""

def counterpartCharCode(char):
	return ord(char.swapcase())

"""
Solution 2
"""

def counterpartCharCode(char):
	return ord(char.upper()) if char.islower() else ord(char.lower())


"""
Solution 3
"""

def counterpartCharCode(char):
	if char.isupper():
		return ord(char.lower())
	elif char.islower():
		return ord(char.upper())
	else:
		return ord(char)

"""
Solution 4
"""

def counterpartCharCode(char):
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if char in uppercase:
		return ord(char.lower())
	else:
		return ord(char.upper())




