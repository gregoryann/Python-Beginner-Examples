"""
Alphabet Soup

Create a function that takes a string and returns a string with its letters in alphabetical order.

Examples
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"

Notes
You can assume numbers and punctuation symbols won't be included in test cases. You'll only have to deal with single word, alphabetic characters.
"""


"""
Solution 1
"""

def alphabet_soup(text):
  return ''.join(sorted(text))


"""
Solution 2
"""

def alphabet_soup(text):
  ret = ''
  lst = list(text)
  lst.sort()
  return ret.join(lst)

"""
Solution 3
"""

def alphabet_soup(text):
  result=[]
  for i in range(97,97+26):
    for j in text:
      if chr(i) == j:
        result.append(j)
  return ''.join(result)






