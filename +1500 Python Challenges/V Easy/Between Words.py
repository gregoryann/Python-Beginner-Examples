"""
Between Words

Write a function that takes three string arguments (first, last, and word) and returns True if word is found between first and last in the dictionary, otherwise False.

Examples

is_between("apple", "banana", "azure") ➞ True
is_between("monk", "monument", "monkey") ➞ True
is_between("bookend", "boolean", "boost") ➞ False

Notes
All letters will be in lowercase.
All three words will be different.
Remember that the string word is in the middle.

"""

"""
Solution 1
"""

def is_between(first, last, word):
	return first < word < last

"""
Solution 2
"""

def is_between(first, last, word):
  return [first,word,last] == sorted([first,word,last])

"""
Solution 3
"""

def is_between(first, last, word):
	return sorted([first, last, word])[1] == word

"""
Solution 4
"""

def is_between(first, last, word):
	i = [first, word, last]
	return i == sorted(i)

"""
Solution 5
"""

def is_between(first, last, word):
	return word != sorted([first, last, word])[0] and word != sorted([first, last, word])[-1]
