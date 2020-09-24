"""
Upper or Lower Case

Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.

Examples
steps_to_convert("abC") ➞ 1
# "abC" converted to "abc" in 1 step

steps_to_convert("abCBA") ➞ 2
# "abCBA" converted to "ABCBA" in 2 steps

steps_to_convert("aba") ➞ 0

steps_to_convert("abaCCC") ➞ 3

Notes
Return 0 if empty string.
Return 0 if the string is already entirely in one case.
Only alphabetic characters.
Input has no spaces.
"""


"""
Solution 1
"""

def steps_to_convert(txt):
	lower = len([i for i in txt if i.islower()])
	upper = len([i for i in txt if i.isupper()])
	return min(lower, upper)

"""
Solution 2
"""

def steps_to_convert(txt):
	lst = [1 if i.isupper() else 0 for i in txt]
	return lst.count(1) if lst.count(1) < lst.count(0) else lst.count(0)

"""
Solution 3
"""

def steps_to_convert(txt):
	up = sum(x.isupper() for x in txt)
	low = sum(x.islower() for x in txt)
	return min(up,low)

"""
Solution 4
"""

def steps_to_convert(txt):
	lowercase = [a for a in txt if a.islower()]
	uppercase = [b for b in txt if b.isupper()]
	if len(lowercase) < len(uppercase):
		return len(lowercase)
	else:
		return len(uppercase)


"""
Solution 5
"""

import string

def steps_to_convert(txt):

    lower, upper = 0, 0

    for char in txt:
        if char in string.ascii_lowercase:
            lower += 1
        else:
            upper += 1

    return lower if lower < upper else upper

