"""
Emphasise the Words

The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.

Examples
emphasise("hello world") ➞ "Hello World"

emphasise("GOOD MORNING") ➞ "Good Morning"

emphasise("99 red balloons!") ➞ "99 Red Balloons!"

Notes
You won't run into any issues when dealing with numbers in strings.
Please don't use the title() method directly :(
"""




################################################################
"""
Solution 1
"""


def emphasise(txt):
	return ' '.join(w[0].upper()+w[1:].lower() for w in txt.split())





################################################################
"""
Solution 2
"""


import re

def emphasise(txt):
	return re.sub(r'\b(\w)', lambda x: x.group(1).upper(), txt.lower())





################################################################
"""
Solution 3
"""


def emphasise(string):
	s = ''
	for i in range(len(string)):
		if i == 0:
			s += string[i].upper()
		elif string[i - 1] != " ":
			s += string[i].lower() 
		else:
			s += string[i].upper()
	return s






#################################################################
"""
Solution 4
"""


def emphasise(txt):
	a = txt.split(" ")
	for i, w in enumerate(a):
		if len(w) > 0 and w[0].isalnum():
			l = w.lower()
			a[i] = l[0].upper() + l[1:]
	return " ".join(a)




