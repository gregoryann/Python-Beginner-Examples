"""
Check if a String Contains only Identical Characters
Write a function that returns True if all characters in a string are identical and False otherwise.

Examples
is_identical("aaaaaa") ➞ True

is_identical("aabaaa") ➞ False

is_identical("ccccca") ➞ False

is_identical("kk") ➞ True

"""


"""
Solution 1
"""

def is_identical(s):
	return len(set(s)) == 1

"""
Solution 2
"""

def is_identical(s):
	return s.count(s[0]) == len(s)


"""
Solution 3
"""

def is_identical(s):
	return all(i == s[0] for i in s)

"""
Solution 4
"""

def is_identical(s):
	return sorted(s) == sorted(s, reverse=True)

"""
Solution 5
"""

def is_identical(s):
		SUM=sum([0 if x ==s[0] else 1 for x in s])
		return True if SUM ==0 else False

