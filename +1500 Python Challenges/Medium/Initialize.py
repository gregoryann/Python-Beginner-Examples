"""
Initialize

Create a function that takes in a list of full names and returns the initials.

Examples
initialize(["Stephen Hawking"]) ➞ ["S. H."]

initialize(["Harry Potter", "Ron Weasley"]) ➞ ["H. P.", "R. W."]

initialize(["Sherlock Holmes", "John Watson", "Irene Adler"]) ➞ ["S. H.", "J. W.", "I. A."]


Notes
Each initial is followed by a dot.
Names will always be made of two words, separated by a space.
"""




################################################################
"""
Solution 1
"""


def initialize(names):
	return ['{}. {}.'.format(i.split()[0][0], i.split()[1][0]) for i in names]




################################################################
"""
Solution 2
"""


initialize=lambda n:['%s. %s.'%(y[0][0],y[1][0])for y in[x.split()for x in n]]



################################################################
"""
Solution 3
"""


import re

def initialize(names):
	return [re.sub(r'(?<=\w)\w+', '.', i) for i in names]



#################################################################
"""
Solution 4
"""


def initialize(names):
    s=[]
    for i in range(len(names)):
        a,b=names[i].split()
        s.append(a[0]+'. '+b[0]+'.')
    return s





#################################################################
"""
Solution 5
"""


def initialize(names):
	import re
	bla = [i.lower() for i in names]
	bla = [i.title() for i in bla]
	y = [re.sub(r'([a-z])','', bla[i]) for i in range(len(bla))]
	x = []
	for a in y:
		x.append(re.sub(r'([A-Z])', r'\1.', re.sub(r'[,:=/]', '', a)))
	return x