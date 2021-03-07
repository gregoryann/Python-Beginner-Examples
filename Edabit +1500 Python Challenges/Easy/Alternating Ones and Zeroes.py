"""
Alternating Ones and Zeroes
Write a function that returns True if the binary string can be rearranged to form a string of alternating 0s and 1s.

Examples
can_alternate("0001111") ➞ True
# Can make: "1010101"

can_alternate("01001") ➞ True
# Can make: "01010"

can_alternate("010001") ➞ False

can_alternate("1111") ➞ False

Notes
No substring of the output may contain more than one consecutive repeating character (e.g. 00 or 11 are not allowed).
Return False if a string only contains 0s or only contains 1s.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

def can_alternate(s):
    return abs(s.count('0') - s.count('1')) in (0, 1)

"""
Solution 2
"""

def can_alternate(s):
	if s.count('0') + 1 == s.count('1') or s.count('0') == s.count('1') + 1 or s.count('0') == s.count('1'): return True
	else: return False

"""
Solution 3
"""

def can_alternate(string):
    if string.count("0") == 0 or string.count("1") == 0:
        return False
    elif abs(string.count("1") - string.count("0")) <= 1:
        return True
    return False



