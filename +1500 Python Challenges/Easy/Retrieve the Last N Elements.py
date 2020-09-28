"""
Retrieve the Last N Elements

Write a function that retrieves the last n elements from a list.

Examples
last([1, 2, 3, 4, 5], 1) ➞ [5]

last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]

last([1, 2, 3, 4, 5], 7) ➞ "invalid"

last([1, 2, 3, 4, 5], 0) ➞ []

Notes
Return "invalid" if n exceeds the length of the list.
Return an empty list if n == 0.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def last(a, n):
  return 'invalid' if n>len(a) else a[len(a)-n:]

"""
Solution 2
"""

def last(a, n):
	if n > len(a): return "invalid"
	if n == 0 : return []
	return a[-n:]

"""
Solution 3
"""

def last(a, n):
	return [] if n == 0 else 'invalid' if n > len(a) else a[-n:]

"""
Solution 4
"""

def last(a, n):
	if n > len(a):
		return "invalid"
	if n == 0:
		return []
	return a[-n:]





