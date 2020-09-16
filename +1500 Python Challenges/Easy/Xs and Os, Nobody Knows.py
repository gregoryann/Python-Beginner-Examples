"""
Xs and Os, Nobody Knows
Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.
Examples
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False

Notes
Remember to return True if there aren't any x's or o's.
Must be case insensitive.
"""


"""
Solution 1
"""

def XO(text):

  return text.lower().count('x')==text.lower().count('o')

"""
Solution 2
"""
import re
def XO(text):
  return len(re.findall(r"[xX]", text)) == len(re.findall(r"[oO]", text))

"""
Solution 3
"""

def XO(text):
  cntX = text.lower().count('x')
  cntO = text.lower().count('o')
  return cntX==cntO

"""
Solution 4
"""

def XO(t):
  l = t.lower()
  return l.count('x') == l.count('o')

"""
Solution 5
"""

def XO(text):
  xs = 0
  os = 0
  for each in text:
    if each == "x" or each == "X":
      xs += 1
    elif each == "o" or each == "O":
      os += 1
  return xs==os


"""
Solution 6
"""

  def XO(text):
    num_xX = len([t for t in text if t == 'x' or t == 'X'])
    num_oO = len([t for t in text if t == 'o' or t == 'O'])
    return num_xX == num_oO