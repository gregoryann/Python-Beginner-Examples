"""
Amazing Alliteration

Alliteration refers to a sequence of words that begin with the same letter. For this exercise, a sentence is correctly alliterated if all words strictly greater than 3 characters begin with the same letter.

Examples
alliteration_correct("She swam to the shore.") ➞ True
# All words >= 4 letters long begins with "s"

alliteration_correct("Maybel manages money well.") ➞ False
# "well" does not begin with an "m"

alliteration_correct("He helps harness happiness.") ➞ True

alliteration_correct("There are many animals.") ➞ False

Notes
Check the resources tab for a better explanation of alliteration.
This is to allow for filler words such as "the", "to", "a", etc. - so words with three or fewer characters are not counted.
Punctuation does not count as part of a word's length.
"""





################################################################
"""
Solution 1
"""


def alliteration_correct(sentence):
	return len(set(w[0] for w in sentence.lower().split() if len(w)>3)) == 1







################################################################
"""
Solution 2
"""


alliteration_correct=lambda s:all(x[0]==s[0].lower()for x in s.replace('.','').lower().split()if len(x)>3)







################################################################
"""
Solution 3
"""


def alliteration_correct(sentence):
	lst = [x.lower() for x in sentence.split()]	
	char = max(lst, key=len)[0]

	for x in lst:
		if len(x) > 3 and not x.startswith(char):
			return False
	return True








#################################################################
"""
Solution 4
"""

from string import punctuation
def alliteration_correct(sentence):
	sentence = sentence.translate(str.maketrans('', '', punctuation)).lower()
	words = [i for i in sentence.split() if len(i) > 3]
	firstletter = words[0][0]
	return all([i[0] == firstletter for i in words])



