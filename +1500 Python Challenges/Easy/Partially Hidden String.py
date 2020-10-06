"""
Partially Hidden String

Create a function that takes a phrase and transforms each word using the following rules:

Keep first and last character the same.
Transform middle characters into a dash -.
Examples
partially_hide("skies were pretty") ➞ "s---s w--e p----y"

partially_hide("red is not my color") ➞ "r-d is n-t my c---r"

partially_hide("She rolled her eyes") ➞ "S-e r----d h-r e--s"

partially_hide("Harry went to fight the basilisk") ➞ "H---y w--t to f---t t-e b------k"

Notes
Words with two or fewer letters should not be hidden at all.
"""



################################################################
"""
Solution 1
"""

def partially_hide(phrase):
	return ' '.join(w[0]+(len(w)-2)*'-'+w[-1] for w in phrase.split())






################################################################
"""
Solution 2
"""

def partially_hide(phrase):
	return ' '.join(i[0] + '-' *(len(i)-2) + i[-1] if len(i) > 2 else \
	i for i in phrase.split())






################################################################
"""
Solution 3
"""

def partially_hide(phrase):
	lst = phrase.split(" ")
	new = []
	dash = 0
	for i, val in enumerate(lst):
		if len(val) > 2:
			dash = len(val)-2
		else:
			dash = 0
		new.append(val[0] + "-"*dash + val[-1])
	return " ".join(new)








#################################################################
"""
Solution 4
"""


partially_hide=lambda t:' '.join(x[0]+'-'*(len(x)-2)+x[-1]if len(x)>2else x for x in t.split())







#################################################################
"""
Solution 5
"""


def partially_hide(phrase):

    phrase_lst = phrase.split()

    mod_lst = []

    for item in phrase_lst:

        if len(item) > 2:

            new_item = item[0] + ("-" * (len(item) -2)) + item[-1]

            mod_lst.append(new_item)

        else:

            mod_lst.append(item)

    return " ".join(mod_lst)