"""
Transform Upvotes

Create a function that transforms a string of upvote counts into a list of numbers. Each k represents a thousand.

Examples
transform_upvotes("6.8k 13.5k") ➞ [6800, 13500]

transform_upvotes("5.5k 8.9k 32") ➞ [5500, 8900, 32]

transform_upvotes("20.3k 3.8k 7.7k 992") ➞ [20300, 3800, 7700, 992]

Notes
Return the upvotes as a list.
"""




################################################################
"""
Solution 1
"""

def transform_upvotes(txt):
		lst=[]
		re_l=txt.replace('.','').replace('k','00').split()
		for a in re_l:
			lst.append(int(a))
		return lst






################################################################
"""
Solution 2
"""

def transform_upvotes(txt):
	return [int(float(x[:-1])*1000) if x[-1]=='k' else int(x) for x in txt.split()]






################################################################
"""
Solution 3
"""


transform_upvotes=lambda t:[float(x)*(1,1000)['.'in x]for x in t.replace('k','').split()]






#################################################################
"""
Solution 4
"""


def transform_upvotes(txt):
	new = []
	vals = txt.split(' ')
	for i in vals:
		if 'k' not in i:
			new.append(int(i))
		else:
			num = i.replace('k', '00')
			num = num.replace('.', '')
			new.append(int(num))
			
	return new





#################################################################
"""
Solution 5
"""


def transform_upvotes(txt):
	a = txt.replace('k', '')
	b = a.split()
	c = []
	for i in b:
		if '.' in i:
			c.append(float(i))
		else:
			c.append(int(i))
	return [i * 1000 if type(i) == float else i for i in c]





#################################################################
"""
Solution 6
"""


def transform_upvotes(txt):

    untransformed_votes = txt.split()
    transformed_votes = []

    for vote in untransformed_votes:
        if vote[-1] == 'k':
            transformed_votes.append(float(vote[:-1]) * 1000)
        else:
            transformed_votes.append(int(vote))

    return transformed_votes






#################################################################
"""
Solution 7
"""

import re
def transform_upvotes(txt):
	txt = re.sub('k', '00', txt)
	txt = re.sub('\.', '', txt)
	return [int(n) for n in txt.split(' ')]