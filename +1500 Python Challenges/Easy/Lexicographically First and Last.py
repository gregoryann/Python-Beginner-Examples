"""
Lexicographically First and Last

Write a function that returns the lexicographically first and lexicographically last rearrangements of a string. Output the results in the following manner:

first_and_last(string) ➞ [first, last]
Examples
first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]

first_and_last("bench") ➞ ["bcehn", "nhecb"]

first_and_last("scoop") ➞ ["coops", "spooc"]

Notes
Lexicographically first: the permutation of the string that would appear first in the English dictionary (if the word existed).
Lexicographically last: the permutation of the string that would appear last in the English dictionary (if the word existed).
"""


"""
Solution 1
"""

def first_and_last(s):
  x = ''.join(sorted(list(s)))
  return [x, x[::-1]]

"""
Solution 2
"""

def first_and_last(s):
	return [''.join(sorted(s)), ''.join(sorted(s,reverse=True))]

"""
Solution 3
"""

def first_and_last(s):
    
    first_permutation = sorted(s)
    last_permutation = first_permutation[::-1]

    return [''.join(first_permutation), ''.join(last_permutation)]

"""
Solution 4
"""

def first_and_last(s):
	word = ''
	box = sorted(s)
	for char in box:
		word += char
	text = [word, word[::-1]]
	print(text)
	return text





