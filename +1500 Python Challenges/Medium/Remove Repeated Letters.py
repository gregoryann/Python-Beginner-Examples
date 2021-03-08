"""
Remove Repeated Letters

Create a function that replaces all consecutively repeated letters in a word with single letters.

Examples
remove_repeats("aaabbbccc") ➞ "abc"

remove_repeats("bookkeeper") ➞ "bokeper"

remove_repeats("nananana") ➞ "nananana"
"""



################################################################
"""
Solution 1
"""


import re
def remove_repeats(s):
	return re.sub(r'(\w)\1+',r'\1', s)



################################################################
"""
Solution 2
"""


def remove_repeats(s):
	r = []
	for x in s:
		if not r or r[-1] != x:
			r.append(x)
	return ''.join(r)


################################################################
"""
Solution 3
"""


def remove_repeats(s):
	s,i=list(s),0
	while i+1<len(s):
		if s[i]!=s[i+1]: i+=1
		else: del s[i]
	return ''.join(s)



#################################################################
"""
Solution 4
"""


def remove_repeats(s):
	ns = ''
	for item in s:
		try:
			if item != ns[-1]:
				ns += item
		except IndexError:
			ns += item
	return ns



