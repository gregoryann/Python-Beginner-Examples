"""
Words With Duplicate Letters

Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".


Notes
Letter matches are case-insensitive.
"""






################################################################
"""
Solution 1
"""


def no_duplicate_letters(phrase):
  return all(i.count(j)==1 for i in phrase.split() for j in i)


################################################################
"""
Solution 2
"""


def no_duplicate_letters(phrase):
    phrase_lst = phrase.split()
    return all([True if len(set(word.lower())) == len(word.lower()) else False for word in phrase_lst])



################################################################
"""
Solution 3
"""


def no_duplicate_letters(phrase):
	from collections import Counter
	split = phrase.split()
	array = map(lambda x: Counter([i.lower() for i in x]).most_common(1)[0][1], split)
	if max(list(array)) > 1:
		return False
	else:
		return True



################################################################
"""
Solution 4
"""

def no_duplicate_letters(phrase):
	for i in phrase.split():
		for j in set(i):
			if i.count(j) >1:
				return False
	return True


