"""
Syncopated Rhythm

Syncopation means an emphasis on a weak beat of a bar of music; most commonly, beats 2 and 4 (and all other even-numbered beats if applicable).

s is a line of music, represented as a string, where hashtags # represent emphasized beats. Create a function that returns if the line of music contains any syncopation.


Examples
has_syncopation(".#.#.#.#") ➞ True
# There are Hash signs in the second, fourth, sixth and
# eighth positions of the string.

has_syncopation("#.#...#.") ➞ False
# There are no Hash signs in the second, fourth, sixth or
# eighth positions of the string.

has_syncopation("#.#.###.") ➞ True
# There are Hash signs in the sixth positions of the string.


Notes
All other unemphasized beats will be represented as a dot.
"""



################################################################
"""
Solution 1
"""


def has_syncopation(s):
		return '#' in s[1::2]



################################################################
"""
Solution 2
"""


def has_syncopation(s):
	f= []
	for i in range(len(s)):
		if s[i] == "#":
			f.append(i%2)
	if 1 in f:
		return True
	else:
		return False



################################################################
"""
Solution 3
"""


def has_syncopation(s):
	for i in range(len(s)):
		if i % 2 == 1:
			if s[i] == "#":
				return True
	return False




