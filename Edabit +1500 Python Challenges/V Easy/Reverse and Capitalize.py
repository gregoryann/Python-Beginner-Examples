"""
Reverse and Capitalize
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.

Examples
reverse_capitalize("abc") ➞ "CBA"

reverse_capitalize("hellothere") ➞ "EREHTOLLEH"

reverse_capitalize("input") ➞ "TUPNI"

"""




"""
Solution 1
"""

def reverse_capitalize(txt):
	return txt[::-1].upper()

"""
Solution 2
"""

def reverse_capitalize(txt):
	capt_txt = txt.upper()
	return capt_txt[::-1]

"""
Solution 3
"""

def reverse_capitalize(txt):
	new_str = ""
	for char in txt:
		new_str += char.upper()
	return new_str[::-1]


"""
Solution 4
"""

def reverse_capitalize(txt):
	reverse=''.join(reversed(txt))
	return (reverse.upper())




