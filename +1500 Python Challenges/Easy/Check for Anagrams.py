"""
Check for Anagrams

Create a function that takes two strings and returns either True or False depending on whether they're anagrams or not.

Examples
is_anagram("cristian", "Cristina") ➞ True

is_anagram("Dave Barry", "Ray Adverb") ➞ True

is_anagram("Nope", "Note") ➞ False

Notes
Should be case insensitive.
The two given strings can be of different lengths.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def is_anagram(s1, s2):
  return(sorted(s1.lower()) == sorted(s2.lower()))

"""
Solution 2
"""

def is_anagram(s1, s2):
	return "".join(sorted(s1.lower())) == "".join(sorted(s2.lower()))

"""
Solution 3
"""

def is_anagram(s1, s2):
  s1 = sorted(s1.lower())
  s2 = sorted(s2.lower())
  if ( s1 == s2 ):
    return True
  else:
    return False

"""
Solution 4
"""

def is_anagram(s1, s2):
  lowS1 = s1.lower()
  lowS2 = s2.lower()
  return sorted(list(lowS1)) == sorted(list(lowS2))


"""
Solution 5
"""

def is_anagram(s1, s2): return sorted(list(s1.lower())) == sorted(list(s2.lower()))

