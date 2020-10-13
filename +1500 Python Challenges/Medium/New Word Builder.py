"""
New Word Builder

Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).

Examples
word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"

word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit"

Notes
The elements in the second list are indexes of the elements in the first list.
"""



################################################################
"""
Solution 1
"""


def word_builder(ltr, pos):
		return ''.join(ltr[i] for i in pos)




################################################################
"""
Solution 2
"""

word_builder = lambda w, x: ''.join(w[i] for i in x)



################################################################
"""
Solution 3
"""


def word_builder(ltr, pos):
	srt = ""
	for i in pos:
		srt = srt + ltr[i]
	return srt






#################################################################
"""
Solution 4
"""


def word_builder(ltr, pos):
	word=[]
	for i in pos:
		word.append(ltr[i])
	return ''.join(word)



