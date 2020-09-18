"""
Remove Every Vowel from a String

Create a function that takes a string and returns a new string with all vowels removed.

Examples
remove_vowels("I have never seen a thin person drinking Diet Coke.")
➞ " hv nvr sn  thn prsn drnkng Dt Ck."

remove_vowels("We're gonna build a wall!")
➞ "W'r gnn bld  wll!"

remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"

Notes
"y" is not considered a vowel.
Expect a valid string for all test cases.
"""



"""
Solution 1
"""

def remove_vowels(txt):
    return ''.join(char for char in txt if not char in "aeiouAEIOU")

"""
Solution 2
"""

import re

def remove_vowels(txt):
    return re.sub(r'[aeiou]+', '', txt, flags=re.IGNORECASE)

"""
Solution 3
"""

def remove_vowels(txt):
  vowels = 'aeiouAEIOU'
  res = ''
  for c in txt:
    if c not in vowels:
      res += c
  
  return res

"""
Solution 4
"""

def remove_vowels(txt):
    vowels = set('aeiouAEIOU')
    for char in vowels:
      txt = txt.replace(char,"")
    return txt;

"""
Solution 5
"""

def remove_vowels(txt):
  vowels = ["a","e","i","o","u","A","E","I","O","U"]
  return "".join([l for l in txt if l not in vowels])
