"""
The Reverser!
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"

Notes
There will be no punctuation in any of the test cases.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def reverse(txt):
	return txt[::-1].swapcase()

"""
Solution 2
"""

def reverse(txt):
	return ''.join([i.lower() if i==i.upper() else i.upper() for i in txt])[::-1]

"""
Solution 3
"""

def reverse(txt):
  return "".join(x.upper() if x.islower() else x.lower() for x in txt[::-1])

"""
Solution 4
"""






