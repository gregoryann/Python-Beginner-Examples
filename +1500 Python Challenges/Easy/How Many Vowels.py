"""
How Many Vowels?

Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4

Notes
a, e, i, o, u are considered vowels (not y).
All test cases are one word and only contain letters.
"""



"""
Solution 1
"""

def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])

"""
Solution 2
"""

def count_vowels(txt):
	vowels = ['a','e','i','o','u']
	return len([char for char in list(txt) if char in vowels])

"""
Solution 3
"""

def count_vowels(txt):
  count = 0
  for chr in txt:
    if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
      count += 1
  return count


"""
Solution 4
"""


def count_vowels(txt):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	count = 0  
	for l in txt:
		if l in vowels:
			count += 1
	return count




