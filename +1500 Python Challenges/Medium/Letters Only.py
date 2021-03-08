"""
Letters Only

Check if the given string consists of only letters and spaces and if every letter is in lower case.

Examples
letters_only("PYTHON") ➞ False

letters_only("python") ➞ True

letters_only("12321313") ➞ False

letters_only("i have spaces") ➞ True

letters_only("i have numbers(1-10)") ➞ False

letters_only("") ➞ False

Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers).
"""





################################################################
"""
Solution 1
"""

def letters_only(s):
	return s.islower() and s.replace(' ','').isalpha()




################################################################
"""
Solution 2
"""

import re
def letters_only(s):
	return bool(re.match(r'^[a-z ]+$', s))






################################################################
"""
Solution 3
"""


letters_only=lambda s:all(x.islower()or x==' 'for x in s)if s else 0






#################################################################
"""
Solution 4
"""


def letters_only(s):
  if len (s)==0 : return False
  for i in s:
    if i == " " or i.islower():
      continue
    else :
      return False
  return True



#################################################################
"""
Solution 5
"""


def letters_only(s):
	stripped = s.replace(" ", "")
	allLowerCase = stripped.islower(); 
	allLetters = stripped.isalpha();
	return allLowerCase and allLetters