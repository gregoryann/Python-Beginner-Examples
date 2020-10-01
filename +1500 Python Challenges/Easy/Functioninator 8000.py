"""
Functioninator 8000
Create a function that takes a single word string and does the following:

Concatenates inator to the end if the word ends with a consonant, otherwise, concatenate -inator instead.

Adds the word length of the original word to the end, supplied with "000".

The examples should make this clear.

Examples
inator_inator("Shrink") ➞ "Shrinkinator 6000"

inator_inator("Doom") ➞ "Doominator 4000"

inator_inator("EvilClone") ➞ "EvilClone-inator 9000"
"""


################################################################
"""
Solution 1
"""

def inator_inator(s):
	return '{}{}inator {}000'.format(s, '-' if s[-1].lower() in 'aeiou' else '', len(s))



################################################################
"""
Solution 2
"""

def inator_inator(inv):
	original=inv
	if inv[-1] in 'ieuoaIEOUA':
		inv+="-"
	return inv+"inator {}000".format(len(original))


################################################################
"""
Solution 3
"""

def inator_inator(inv):
	vowels = "aeiou"
	if ((inv[-1] in vowels) or (inv[-1].lower() in vowels)):
		return inv + "-inator " + str(len(inv)) + "000"
	else:
		return inv + "inator " + str(len(inv)) + "000"


################################################################
"""
Solution 4
"""

def inator_inator(inv):
    if inv.endswith('a') or inv.endswith('e') or inv.endswith('i') or inv.endswith('o') or inv.endswith('u')\
    or inv.endswith('A') or inv.endswith('E') or inv.endswith('I') or inv.endswith('O') or inv.endswith('U'):
        return(inv + '-inator ' + str(len(inv)) + '000')
    else:
        return(inv + 'inator ' + str(len(inv)) + '000')




################################################################
"""
Solution 5
"""


def inator_inator(inv):
	x = 'inator'
	if inv[-1].lower() in 'aeiou':
		x = '-inator'
	return '{}{} {}000'.format(inv,x,len(inv))