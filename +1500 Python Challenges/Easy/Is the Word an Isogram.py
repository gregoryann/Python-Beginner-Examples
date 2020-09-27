"""
Is the Word an Isogram?

An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

Examples
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False

Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
"""


"""
Solution 1
"""

def is_isogram(txt):
  return len(txt) == len(set(txt.lower()))

"""
Solution 2
"""

def is_isogram(txt):
    word = txt.lower()
    for i in word:
        if word.count(i) > 1:
            return False
    return True

"""
Solution 3
"""

is_isogram = lambda txt: len(set(txt.lower()))==len(txt)

"""
Solution 4
"""

def is_isogram(txt):
    txt = txt.lower()
    temp = []
    result = None
    for i in txt:
        if i in temp:
            result = False
            break
        else:
            temp.append(i)
            result = True
    return result




