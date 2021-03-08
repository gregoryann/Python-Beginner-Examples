"""
Average Word Length

Create a function that takes in a sentence and returns the average length of each word in that sentence. Round your result to two decimal places.

Examples
average_word_length("A B C.") ➞ 1.00

average_word_length("What a gorgeous day.") ➞ 4.00

average_word_length("Dude, this is so awesome!") ➞ 3.80

Notes
Ignore punctuation when counting the length of a word.
"""



################################################################
"""
Solution 1
"""


def average_word_length(txt):
	return round((sum(i.isalpha() for i in txt)/len(txt.split())), 2)


################################################################
"""
Solution 2
"""


import string
def average_word_length(txt):
	s = txt.translate(str.maketrans('', '', string.punctuation))
	words = s.split()
	return round(sum(len(w) for w in words) / len(words), 2)


################################################################
"""
Solution 3
"""


def average_word_length(txt):
	import re
	lst = list(map(len, re.sub(r'\W+', ' ', txt).split()))
	return round(sum(lst)/len(lst),2)



#################################################################
"""
Solution 4
"""


def average_word_length(txt):
	txt, tot = txt.split(), sum(sum(1 for c in w if c.isalpha()) for w in txt)
	return round(tot / len(txt), 2)



