"""
Verbed Nouns

Create a function that ends the first word of a phrase with "ed", essentially verbifying a noun.

Examples
verbify("cheese burger") ➞ "cheesed burger"

verbify("salt water") ➞ "salted water"

verbify("orange juice") ➞ "oranged juice"

verbify("shredded cheese") ➞ "shredded cheese"

Notes
Change only the first word.
Note that some words may already end in "e" or "ed".
All phrases will be in lowercase.
"""





################################################################
"""
Solution 1
"""

def verbify(txt):
	first, last = txt.split()
	
	if first.endswith('e'):
		first += 'd'
		
	elif not first.endswith('ed'):
		first += 'ed'
		
	return '{} {}'.format(first, last)






################################################################
"""
Solution 2
"""

def verbify(txt):
	t = txt.split()	
	return ' '.join([t[0][:-2]+ t[0][-2:].strip('ed') + 'ed', t[1]])






################################################################
"""
Solution 3
"""

verbify=lambda t:t.replace(' ',{'d':' ','e':'d '}.get(t[t.find(' ')-1],'ed '))





#################################################################
"""
Solution 4
"""

def verbify(txt):
	t = txt.split()
	return txt if t[0][-2:]=='ed' else t[0]+'d '+t[1] if t[0][-1]=='e' else t[0]+'ed '+t[1]




