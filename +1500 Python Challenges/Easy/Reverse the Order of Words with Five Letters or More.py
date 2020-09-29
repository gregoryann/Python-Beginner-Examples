"""
Reverse the Order of Words with Five Letters or More

Write a function that takes a string of one or more words as an argument and returns the same string, but with all five or more letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples
reverse("Reverse") ➞ "esreveR"

reverse("This is a typical sentence.") ➞ "This is a lacipyt .ecnetnes"

reverse("The dog is big.") ➞ "The dog is big."

Notes
You can expect a valid string to be provided for each test case.
"""



########################################################################



"""
Solution 1
"""

def reverse(txt):
    return " ".join([x if len(x) < 5 else x[::-1] for x in txt.split()])

"""
Solution 2
"""

def reverse(txt):
  output=[]
  for word in txt.split():
    if len(word) < 5:
      output.append(word)
    else:
      output.append(word[::-1])
  return " ".join(output)

"""
Solution 3
"""

reverse=lambda t:' '.join(x[::-1]if len(x)>4else x for x in t.split())

"""
Solution 4
"""


def short_reverse(txt):
  if len(txt) >= 5:
    return txt[::-1]
  else:
    return txt

def reverse(txt):
	return ' '.join([short_reverse(s) for s in txt.split(' ')])





