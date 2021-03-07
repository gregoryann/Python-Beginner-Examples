"""
Counting Adverbs

Create a function that counts the number of adverbs in a sentence. An adverb is a word that ends with ly.

Examples
count_adverbs("She ran hurriedly towards the stadium.") ➞ 1

count_adverbs("She ate the lasagna heartily and noisily.") ➞ 2

count_adverbs("He hates potatoes.") ➞ 0

count_adverbs("He was happily, crazily, foolishly over the moon.") ➞ 3

Notes
Do NOT count words where the ly is in the beginning or the middle (e.g. Lysol, Illya).
For the purpose of this exercise, ignore the nuances of the English language (some adjectives also end in ly).
"""





################################################################
"""
Solution 1
"""

import re

def count_adverbs(sentence):

    matches = re.findall(r'ly[^\w]', sentence)
    return len(matches)






################################################################
"""
Solution 2
"""

def count_adverbs(sentence):
	sentence=''.join([i for i in sentence if i.isalnum() or i.isspace()])
	return len([i for i in sentence.split() if i[-2:]=='ly'])






################################################################
"""
Solution 3
"""

count_adverbs=lambda s:sum(x[-2:]=='ly'for x in s.replace('.','').replace(',','').split())







#################################################################
"""
Solution 4
"""


def count_adverbs(sentence):
	sentence = sentence.replace('.','')
	sentence = sentence.replace('!','')
	sentence = sentence.replace('?','')
	sentence = sentence.replace("'",'')
	sentence = sentence.replace(",",'')
	temp = sentence.split(' ')
	ctr = 0
	for i in range(len(temp)):
		if len(temp[i]) > 1:
			if temp[i][-2:] == 'ly':
				ctr += 1
	return ctr







#################################################################
"""
Solution 5
"""


def count_adverbs(sentence):
	from collections import Counter
	import re
	x = re.sub(r'[^\w\s]','',sentence)
	lst = x.split(" ")
	
	adverb = Counter(x.endswith("ly") for x in lst)
	return adverb[1]




#################################################################
"""
Solution 6
"""


def count_adverbs(sentence):
	lst = sentence.split(' ')
	c = 0
	for i in lst:
		if i[-1].isalpha():
			if 'ly' in i[-2:]:
				c+=1
		else:
			i = i[:-1]
			if 'ly' in i[-2:]:
				c+=1
	return c