"""
Abbreviations Unique?

You are given two inputs:

An array of abbreviations.
An array of words.
Write a function that returns True if each abbreviation uniquely identifies a word, and False otherwise.

Examples
unique_abbrev(["ho", "h", "ha"], ["house", "hope", "happy"]) ➞ False
// "ho" and "h" are ambiguous and can identify either "house" or "hope"

unique_abbrev(["s", "t", "v"], ["stamina", "television", "vindaloo"]) ➞ True

unique_abbrev(["bi", "ba", "bat"], ["big", "bard", "battery"]) ➞ False

unique_abbrev(["mo", "ma", "me"], ["moment", "many", "mean"]) ➞ True

Notes
Abbreviations will be a substring from [0, n] from the original string.
"""



################################################################
"""
Solution 1
"""


def unique_abbrev(abbs, words):
	return all(sum(w.startswith(a) for a in abbs) == 1 for w in words)



################################################################
"""
Solution 2
"""


def unique_abbrev(abbs, words):
	return all([i[:len(j)] for i in words].count(j)==1 for j in abbs)


################################################################
"""
Solution 3
"""


def unique_abbrev(abbs, words):
	x=[i for i in words if i.startswith(abbs[0])]
	y=[i for i in words if i.startswith(abbs[1])]
	z=x=[i for i in words if i.startswith(abbs[2])]
	return  len(x)==1 and len(y)==1 and len(z)==1


#################################################################
"""
Solution 4
"""


def unique_abbrev(abbs, words):
	for abbr in abbs:
		if sum([x.startswith(abbr) for x in words]) > 1:
			return False
	return True



