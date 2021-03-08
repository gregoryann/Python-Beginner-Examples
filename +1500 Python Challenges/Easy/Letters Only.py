"""
Letters Only
Write a function that removes any non-letters from a string, returning a well-known film title.

Examples
letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"

letters_only("^,]%4B|@56a![0{2m>b1&4i4") ➞ "Bambi"

letters_only("^U)6$22>8p).") ➞ "Up"

Notes
See the Resources section for more information on Python string methods.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def letters_only(txt):
	return ''.join(i for i in txt if i.isalpha())


"""
Solution 2
"""

import re

def letters_only(txt):
	return re.sub(r'[^a-zA-Z]', '', txt)

"""
Solution 3
"""

letters_only = lambda t: "".join(e for e in t if e.isalpha())

"""
Solution 4
"""

def letters_only(txt):
	return ''.join([x for x in txt if ord(x) in range(65,91) or ord(x) in range(97,123)])




