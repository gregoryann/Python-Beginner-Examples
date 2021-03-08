"""
Pluralize!
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }


Notes
This is an oversimplification of the English language so no edge cases will appear.
Only focus on whether or not to add an s to the ends of words.
All tests will be valid.
"""





################################################################
"""
Solution 1
"""


def pluralize(lst):
	return set(i + 's'*(lst.count(i)>1) for i in lst)



################################################################
"""
Solution 2
"""


from collections import*
pluralize=lambda l:{k+('','s')[v>1]for k,v in Counter(l).items()}



################################################################
"""
Solution 3
"""


def pluralize(lst):
	x = set()
	for item in lst:
		if lst.count(item) > 1:
			x.add(item + "s")
		else:
			x.add(item)
	return x



################################################################
"""
Solution 4
"""


def pluralize(lst):
	return dict.fromkeys([ i if lst.count(i) == 1 else i+"s" for i in lst ]).keys()



