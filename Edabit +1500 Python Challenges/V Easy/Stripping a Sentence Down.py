"""
Stripping a Sentence Down

Create a function which takes in a sentence txt and a string of characters chars and return the sentence but with all the specified characters removed.

Examples
strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou") ➞ "th qck brwn fx jmps vr th lzy dg"
strip_sentence("the hissing snakes sinisterly slither across the rustling leaves", "s") ➞ "the hiing nake initerly lither acro the rutling leave"
strip_sentence("gone, reduced to atoms", "go, muscat nerd") ➞ ""

Notes
You may be asked to remove punctuation and spaces.
Return an empty string if every charcter is specified (see example #3).
All tests will be in lowercase.

"""


"""
Solution 1
"""

def strip_sentence(txt, chars):
	return ''.join(i for i in txt if i not in chars)

"""
Solution 2
"""

def strip_sentence(txt, chars):
	for m in chars:
		txt = txt.replace( m , "" )
	return txt

"""
Solution 3
"""

def strip_sentence(txt, chars):
	return (txt.translate({ord(i): None for i in chars}))

"""
Solution 4
"""

def strip_sentence(txt, chars):
	for c in chars:
		txt = txt.replace(c, '')
		
	return txt

"""
Solution 5
"""
def strip_sentence(txt, chars):
	new_txt = []
	for i in txt:
		if i not in chars:
			new_txt.append(i)
	return ''.join(new_txt)

"""
Solution 6
"""

def strip_sentence(txt, chars):
	for c in chars:
		txt = txt.replace(c, '')
	return txt