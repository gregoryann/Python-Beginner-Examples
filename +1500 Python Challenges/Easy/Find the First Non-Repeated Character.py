"""
Find the First Non-Repeated Character

Create a function that accepts a string as an argument and returns the first non-repeated character.

Examples
first_non_repeated_character("g") ➞ "g"

first_non_repeated_character("it was then the frothy word met the round night") ➞ "a"

first_non_repeated_character("the quick brown fox jumps then quickly blows air") ➞ "f"

first_non_repeated_character("hheelloo") ➞ False

first_non_repeated_character("") ➞ False

Notes
An empty string should return False.
If every character repeats, return False.
Don't worry about case sensitivity or non-alphanumeric characters.
"""





################################################################
"""
Solution 1
"""

def first_non_repeated_character(txt):
  for c in txt:
    if txt.count(c) == 1:
      return c
  return False






################################################################
"""
Solution 2
"""

first_non_repeated_character=lambda t:next((x for x in t if t.count(x)<2),0)







################################################################
"""
Solution 3
"""


from collections import OrderedDict

# String -> String or Boolean

def first_non_repeated_character(txt):

  # build a frequency counter with maintaining order

  freqCnt = OrderedDict()

  for char in list(txt):

    freqCnt[char] = freqCnt.get(char,0) + 1

  # find first char with count 1

  cnt1 = [char for char,cnt in freqCnt.items() if cnt == 1]

  # return first char with count 1 or False

  return cnt1[0] if cnt1 else False








#################################################################
"""
Solution 4
"""

def first_non_repeated_character(txt):
  lst = []
  for char in txt:
    if txt.count(char) == 1:
      lst.append(char)
  
  if lst == []:
    return False
  else:
    return lst[0]




