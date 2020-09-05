"""
Reverse the Order of a String
Create a function that takes a string as its argument and returns the string in reversed order.

Examples
reverse("Hello World") ➞ "dlroW olleH"

reverse("The quick brown fox.") ➞ ".xof nworb kciuq ehT"

reverse("Edabit is really helpful!") ➞ "!lufpleh yllaer si tibadE"

Notes
You can expect a valid string for all test cases.
"""

"""
Solution 1
"""

def reverse(s):
    return s[::-1]

"""
Solution 2
"""

def reverse(s):
    l = list(s)
    l.reverse()
    return "".join(l)

"""
Solution 3
"""

def reverse(string):
  newstring = []
  for letter in string:
  	newstring.insert(0,letter)
  finalstring = ''.join(newstring)
  return finalstring

"""
Solution 4
"""






