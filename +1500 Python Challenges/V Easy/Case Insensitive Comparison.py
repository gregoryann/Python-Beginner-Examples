"""
Case Insensitive Comparison
Write a function that validates whether two strings are identical. Make it case insensitive.

Examples
match("hello", "hELLo") ➞ True

match("motive", "emotive") ➞ False

match("venom", "VENOM") ➞ True

match("mask", "mAskinG") ➞ False

"""


"""
Solution 1
"""

def match(s1, s2):
  return s1.lower() == s2.lower()


"""
Solution 2
"""

match = lambda s1, s2: s1.lower() == s2.lower()

"""
Solution 3
"""

def match(s1, s2):
	if s2.lower()==s1.lower():
		return True
	else:
		return False

"""
Solution 4
"""

def match(s1, s2):
	x=s1.lower()
	y=s2.lower()
	if x == y: 
		return True
	else:
		return False








