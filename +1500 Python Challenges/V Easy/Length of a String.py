"""
Recursion: Length of a String

Write a function that returns the length of a string. Make your function recursive.

Examples
length("apple") ➞ 5

length("make") ➞ 4

length("a") ➞ 1

length("") ➞ 0

Notes
Check the Resources tab for info on recursion.
"""



"""
Solution 1
"""

def length(s):
  if s: return length(s[:-1]) + 1
  return 0

"""
Solution 2
"""

def length(txt):
	if txt == '':
		return 0
	return length(txt[1:]) + 1

"""
Solution 3
"""

def length(txt):
	return 0 if txt=="" else length(txt[0:-1])+1

"""
Solution 4
"""
length = lambda txt:len(txt)





