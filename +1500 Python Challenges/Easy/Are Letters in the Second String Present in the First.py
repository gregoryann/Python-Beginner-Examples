"""
Are Letters in the Second String Present in the First?
Create a function that accepts a list of two strings and checks if the letters in the second string are present in the first string.

Examples
letter_check(["trances", "nectar"]) ➞ True

letter_check(["compadres", "DRAPES"]) ➞ True

letter_check(["parses", "parsecs"]) ➞ False

Notes
Function should not be case sensitive (as indicated in the second example).
Both strings are presented as a single argument in the form of a list.
Bonus: Solve this without RegEx.
"""





################################################################
"""
Solution 1
"""

def letter_check(lst):
  return all([c in lst[0].lower() for c in lst[1].lower()])





################################################################
"""
Solution 2
"""

def letter_check(lst):
  lst[0] = [x.lower() for x in lst[0]]
  lst[1] = [x.lower() for x in lst[1]]
  return set(lst[1]).issubset(set(lst[0]))







################################################################
"""
Solution 3
"""

letter_check=lambda l:set(l[0].lower())>=set(l[1].lower())





#################################################################
"""
Solution 4
"""

def letter_check(lst):
  ls1 = set(lst[0].lower())
  ls2 = set(lst[1].lower())
  for x in ls2:
    if x not in ls1: return False
  return Tru






#################################################################
"""
Solution 5
"""


def letter_check(lst):
  str1 = list(lst[0].casefold())
  str2 = list(lst[1].casefold())

  for x in str2:
   if x not in str1:
    return False
  return True




#################################################################
"""
Solution 6
"""



def letter_check(lst):
  L1 = lst[0].replace(' ', '').upper()
  L2 = lst[1].replace(' ', '').upper()
  i = 0
  while i < len(L2):
    if L2[i] in L1:
      i += 1
    else:
      return False
  return True

print(letter_check(["THE EYES", "they see"]))