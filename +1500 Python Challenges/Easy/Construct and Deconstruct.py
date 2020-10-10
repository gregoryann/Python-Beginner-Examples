"""

Construct and Deconstruct

Given a string, create a function that outputs a list, building and deconstructing the string letter by letter. See the examples below for some helpful guidance.

Examples
construct_deconstruct("Hello") ➞ [
  "H",
  "He",
  "Hel",
  "Hell",
  "Hello",
  "Hell",
  "Hel",
  "He",
  "H"
]

construct_deconstruct("edabit") ➞ [
  "e",
  "ed",
  "eda",
  "edab",
  "edabi",
  "edabit",
  "edabi",
  "edab",
  "eda",
  "ed",
  "e"
]

construct_deconstruct("the sun") ➞ [
  "t",
  "th",
  "the",
  "the ",
  "the s",
  "the su",
  "the sun",
  "the su",
  "the s",
  "the ",
  "the",
  "th",
  "t"
]


Notes
Include spaces (see example #3).
"""





################################################################
"""
Solution 1
"""


def construct_deconstruct(s):
	half = [s[:i] for i in range(1, len(s) + 1)]
	return half + half[:-1][::-1]








################################################################
"""
Solution 2
"""

def construct_deconstruct(s):
	ret = []
	for i in range(1,len(s)+1):
		ret.append(s[:i])
	for i in range(len(s)-1,0,-1):
		ret.append(s[:i])
	return ret






################################################################
"""
Solution 3
"""

construct_deconstruct=lambda s:[s[:i]for i in range(1,len(s))]+[s[:i]for i in range(len(s),0,-1)]







#################################################################
"""
Solution 4
"""

def construct_deconstruct(s):
    cb = [ s[0:i+1] for i,char in enumerate(s)]
    db = cb[::-1][1:]
    return cb+db




