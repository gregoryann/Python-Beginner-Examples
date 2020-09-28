"""
Is the String in Order?

Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.

Examples
is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True

Notes
You don't have to handle empty strings.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

def is_in_order(txt):
	return list(txt) == sorted(txt)

"""
Solution 2
"""
def is_in_order(txt):
	return txt == "".join(sorted(txt))

"""
Solution 3
"""
def is_in_order(txt):
  return all([txt[i] <= txt[i + 1] for i in range(len(txt) - 1)])

"""
Solution 4
"""
def is_in_order(txt):
	txt = list(txt)
	return False if txt !=sorted(txt) else True




