"""
Find the Shared Letters between Two Strings

Given two strings, return a string containing only the letters shared between the two.

Examples
shared_letters("house", "home") ➞ "eho"

shared_letters("Micky", "mouse") ➞ "m"

shared_letters("house", "villa") ➞ ""

Notes
If none of the letters are shared, return an empty string.
The function should be case insensitive (e.g. comparing A and a should return a).
Sort the resulting string alphabetically before returning it.
"""



################################################################
"""
Solution 1
"""


def shared_letters(a, b):
    return "".join(sorted(set(a.lower()) & set(b.lower())))



################################################################
"""
Solution 2
"""


def shared_letters(a, b):
	lst =[]
	for i in a.lower():
		if i in b.lower():
			lst.append(i)
	return ''.join(sorted(set(lst)))


################################################################
"""
Solution 3
"""

shared_letters = lambda a, b: ''.join(sorted(set(a.lower())&set(b.lower())))



#################################################################
"""
Solution 4
"""


def shared_letters(a, b):
    x = ",".join(a.casefold()).split(",")
    x1 = ",".join(b.casefold()).split(",")
    k = [w for w in x if w in x and w in x1]
    k1 = set(k)
    return "".join(sorted(k1))



