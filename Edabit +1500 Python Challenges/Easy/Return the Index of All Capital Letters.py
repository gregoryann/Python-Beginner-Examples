"""
Return the Index of All Capital Letters

Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]

Notes
Return an empty list if no uppercase letters are found in the string.
Special characters ($#@%) and numbers will be included in some test cases.
"""



"""
Solution 1
"""

def index_of_caps(word):
  return [index for index, letter in enumerate(word) if letter.isupper()]

"""
Solution 2
"""

def index_of_caps(word):
  result = []
  for letter in word:
    if letter.isupper():
      result.append(word.index(letter))
  return result

"""
Solution 3
"""

def index_of_caps(word):
  return [index for index, letter in enumerate(word) if letter == letter.upper() and letter.isalpha()]

"""
Solution 4
"""

def index_of_caps(word):
  result=[]
  for i, c in enumerate(word):
    if "A" <= c <= "Z":
      result.append(i)
  return result




