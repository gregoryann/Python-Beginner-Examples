"""
Get Word Count
Create a function that takes a string and returns the word count. The string will be a sentence.

Examples
count_words("Just an example here move along") ➞ 6

count_words("This is a test") ➞ 4

count_words("What an easy task, right") ➞ 5
Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


"""
Solution 1
"""

def count_words(txt):
  return len(txt.split())

"""
Solution 2
"""

def count_words(txt):
  items = txt.split()
  num = len(items)
  return (num)

"""
Solution 3
"""

def count_words(txt):
    counter = 0
    for i in range(len(txt)):
        if txt[i] == " ":
            counter += 1
    return counter + 1

"""
Solution 4
"""


def count_words(txt):
  x = txt.split()
  y = len(x)
  return y


