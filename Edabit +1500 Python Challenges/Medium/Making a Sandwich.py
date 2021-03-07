"""
Making a Sandwich

Given a list of ingredients i and a flavour f as input, create a function that returns the list, but with the elements bread around the selected ingredient.

Examples
make_sandwich(["tuna", "ham", "tomato"], "ham") ➞ ["tuna", "bread", "ham", "bread", "tomato"]

make_sandwich(["cheese", "lettuce"], "cheese") ➞ ["bread", "cheese", "bread", "lettuce"]

make_sandwich(["ham", "ham"], "ham") ➞ ["bread", "ham", "bread", "bread", "ham", "bread"]


Notes
You will always get valid inputs.
Make two separate sandwiches if two of the same elements are next to each other (see example #3).
"""



################################################################
"""
Solution 1
"""


def make_sandwich(i,f):
	return ' '.join(x if x != f else 'bread '+x+' bread' for x in i).split()



################################################################
"""
Solution 2
"""


def make_sandwich(i,f):
	for x in range(len(i)-1,-1,-1):
		if i[x] == f:
			i.insert(x+1, 'bread')
			i.insert(x,'bread')
	return i


################################################################
"""
Solution 3
"""


def make_sandwich(i,f):
	o = []
	for l in i:
		if l == f:
			o.append('bread')
			o.append(l)
			o.append('bread')
		else:
			o.append(l)
			
	return o



#################################################################
"""
Solution 4
"""


def make_sandwich(i, f):
	lst = []
	for el in i:
		if el == f:
			lst.extend(['bread', el, 'bread'])
		else:
			lst.append(el)
	return lst



