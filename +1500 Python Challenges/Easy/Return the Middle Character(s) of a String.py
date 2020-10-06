"""
Return the Middle Character(s) of a String

Create a function that takes a string and returns the middle character(s). If the word's length is odd, return the middle character. If the word's length is even, return the middle two characters.

Examples
get_middle("test") ➞ "es"

get_middle("testing") ➞ "t"

get_middle("middle") ➞ "dd"

get_middle("A") ➞ "A"

Notes
All test cases contain a single word (as a string).
"""





################################################################
"""
Solution 1
"""

def get_middle(word):
   return word[(len(word)-1)//2:(len(word)+2)//2]





################################################################
"""
Solution 2
"""

def get_middle(word):
  while len(word) > 2:
    word = word[1:-1]
  return word






################################################################
"""
Solution 3
"""

def get_middle(word): 
    m = (len(word) - 1) // 2
    l = 1 if len(word) % 2 else 2
    return word[m:m+l]






#################################################################
"""
Solution 4
"""


def get_middle(word):
    """If the word's length is odd, return the middle character.
    If the length is even, return the middle two characters.
    If the word's length is 0, return word

    >>> get_middle("test")
    'es'
    >>> get_middle("testing")
    't'
    >>>
    """
    length = len(word)
    half = int(length/2)
    if length == 1:
      return word
    elif length%2:
      return word[half]
    else:
      return word[(half-1):(half+1)]



