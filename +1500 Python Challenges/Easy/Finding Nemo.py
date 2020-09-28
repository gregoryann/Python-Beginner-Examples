"""
Finding Nemo

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find nemo]!".

If you can't find Nemo, return "I can't find Nemo :(".

Examples
find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

find_nemo("Nemo is me") ➞ "I found Nemo at 1!"

find_nemo("I Nemo am") ➞ "I found Nemo at 2!"

Notes
! , ? . are always separated from the last word.
Nemo will always look like Nemo, and not NeMo or other capital variations.
Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
If there are multiple Nemo's in the sentence, only return for the first one.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def find_nemo(sentence):
    s=sentence.split()
    if 'Nemo' in s:
        return 'I found Nemo at {}!'.format(s.index('Nemo')+1)
    return "I can't find Nemo :("

"""
Solution 2
"""

def find_nemo(sentence):
    for idx, i in enumerate(sentence.split(), 1):
        if i == 'Nemo':
            return "I found Nemo at {}!".format(idx)
    return "I can't find Nemo :("

"""
Solution 3
"""

def find_nemo(sentence):
	split = sentence.split(' ')
	if 'Nemo' in split:
		return "I found Nemo at {}!".format(split.index('Nemo') + 1)
	else:
		return "I can't find Nemo :("

"""
Solution 4
"""

def find_nemo(sentence):
	i=sentence.split().index("Nemo") if "Nemo" in sentence.split() else -1
	return ("I found Nemo at " + str(i+1) + "!" ) if i>-1 else "I can't find Nemo :("




