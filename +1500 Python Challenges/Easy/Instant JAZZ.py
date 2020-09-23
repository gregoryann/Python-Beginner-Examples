"""
Instant JAZZ
Create a function which concantenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.

Examples
jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

jazzify([]) ➞ []

Notes
Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.
"""



"""
Solution 1
"""

def jazzify(lst):
	return [i if i.endswith('7') else i + '7' for i in lst]

"""
Solution 2
"""

import re

def jazzify(lst):
	return [re.sub('(?<!7)$', '7', i) for i in lst]

"""
Solution 3
"""

def jazzify(lst):
	h = []
	for x in lst :
		if "7" not in x : h.append(x+"7")
		else : h.append(x)
	return h








