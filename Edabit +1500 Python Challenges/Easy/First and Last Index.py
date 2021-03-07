"""
First and Last Index

Given a word, write a function that returns the first index and the last index of a character.

Examples
char_index("hello", "l") ➞ [2, 3]
# The first "l" has index 2, the last "l" has index 3.

char_index("circumlocution", "c") ➞ [0, 8]
# The first "c" has index 0, the last "c" has index 8.

char_index("happy", "h") ➞ [0, 0]
# Only one "h" exists, so the first and last index is 0.

char_index("happy", "e") ➞ None
# "e" does not exist in "happy", so we return undefined.

Notes
If the character does not exist in the word, return None.
If only one instance of the character exists, the first and last index will be the same.
Check the Resources tab for hints.
"""





#############################################################
"""
Solution 1
"""

def char_index(word, char):
	return None if char not in word else [word.index(char), word.rindex(char)]





#############################################################
"""
Solution 2
"""

def char_index(word, char):
	if char not in word:
		return None
	return [word.find(char),word.rfind(char)]





#############################################################
"""
Solution 3
"""

def char_index(word, char):
	if char not in word:
		return None
	elif word.count(char) == 1:
		return [word.index(char),word.index(char)]
	else:
		temp = []
		for i in range(len(word)):
			if word[i] == char:
				temp.append(i)
		return [temp[0],temp[-1]]






#############################################################
"""
Solution 4
"""


def char_index(word, char):
	if char not in word:
		return None
	x = [idx for idx, ch in enumerate(word) if ch == char]
	first = min(x)
	last = max(x)
	return [first, last]





#############################################################
"""
Solution 5
"""

char_index=lambda w,c:c in w and[w.find(c),len(w)-w[::-1].find(c)-1]or None






#############################################################
"""
Solution 6
"""


def char_index(word, char):
	ans = []
	index = word.find(char)
	ans.append(index)
	while index != -1:
		index += 1
		ans.append(word.find(char,index))
		print(ans)
	return ans