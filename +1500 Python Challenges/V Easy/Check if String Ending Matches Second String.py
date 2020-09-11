"""
Check if String Ending Matches Second String

Create a function that takes two strings and returns True if the first string ends with the second string; otherwise return False.

Examples
check_ending("abc", "bc") ➞ True

check_ending("abc", "d") ➞ False

check_ending("samurai", "zi") ➞ False

check_ending("feminine", "nine") ➞ True

check_ending("convention", "tio") ➞ False

Notes
All test cases are valid one word strings.

"""


"""
Solution 1
"""

def check_ending(str1, str2):
  return str1.endswith(str2)

"""
Solution 2
"""

def check_ending(str1, str2):
    return str1[-len(str2):] == str2

"""
Solution 3
"""

def check_ending(str1, str2):
    lstr1 = len(str1) - 1;
    lstr2 = len(str2) - 1;
    if str1[lstr1 - lstr2:] == str2:
      return True
    else:
      return False

"""
Solution 4
"""

def check_ending(str1, str2):
    strInd = -1 * len(str2)
    if str1[strInd:] == str2:
      return True
    else:
      return False




