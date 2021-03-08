"""
Total Number of Unique Characters
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples

count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"

count_unique("sore", "zebra") ➞ 7
count_unique("a", "soup") ➞ 5

Notes
Each word will contain at least one letter.
All words will be lower cased.

"""



"""
Solution 1
"""

def count_unique(s1, s2):
  return len(set(s1 + s2))


"""
Solution 2
"""

def count_unique(s1, s2):
	combstr = s1 + s2
	return len(set(combstr))

"""
Solution 3
"""

def count_unique(s1, s2):	
    unics = ""
    for letter in (s1 + s2):
        if letter not in unics:
            unics += letter
    return len(unics)







