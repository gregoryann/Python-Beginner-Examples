"""
Scottish Screaming

A strong Scottish accent makes every vowel similar to an "e", so you should replace every vowel with an "e". Additionally, it is being screamed, so it should be in block capitals.

Create a function that takes a string and returns a string.

Examples
to_scottish_screaming("hello world") ➞ "HELLE WERLD"

to_scottish_screaming("Mr. Fox was very naughty") ➞ "MR. FEX WES VERY NEEGHTY"

to_scottish_screaming("Butterflies are beautiful!") ➞ "BETTERFLEES ERE BEEETEFEL!"

Notes
Make sure to include all punctuation that is in the original string.
You don't need any more namespaces than are already given.
"""




################################################################
"""
Solution 1
"""


import re

def to_scottish_screaming(s):
		return re.sub('[AIOU]', 'E', s.upper())


################################################################
"""
Solution 2
"""


def to_scottish_screaming(txt):
    return ''.join('E' if x in 'aeiouAEIOU' else x for x in txt).upper()



################################################################
"""
Solution 3
"""


def to_scottish_screaming(txt):
	lst_vowel = ["a","e","i","o","u"]
	flag = False
	txt = txt.lower()
	for i in txt:
		if i in lst_vowel:
			flag = True
			txt = txt.replace(i,"e")
	if flag:
		return txt.upper()



#################################################################
"""
Solution 4
"""


def to_scottish_screaming(txt):
	for char in txt:
		if char.lower() in 'aeiou':
			txt = txt.replace(char, 'e')
	return txt.upper()



