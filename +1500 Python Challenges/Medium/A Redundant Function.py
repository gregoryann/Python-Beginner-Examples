"""
A Redundant Function

Write a function that takes in a string s and returns a function that returns s.

Examples
f1 = redundant("apple")
f1() ➞ "apple"

f2 = redundant("pear")
f2() ➞ "pear"

f3 = redundant("")
f3() ➞ ""

Notes
Your function should return a function, not a string.
"""



################################################################
"""
Solution 1
"""


def redundant(s):
	return lambda: s


################################################################
"""
Solution 2
"""


def redundant(s):
	def func():
		return s
	return func




