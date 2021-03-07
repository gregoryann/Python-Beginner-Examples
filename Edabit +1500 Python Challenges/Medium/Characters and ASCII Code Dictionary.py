"""
Characters and ASCII Code Dictionary

Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
"""



################################################################
"""
Solution 1
"""


def to_dict(lst):
	return [{c: ord(c)} for c in lst]



################################################################
"""
Solution 2
"""


to_dict = lambda l: [{k:ord(k)} for k in l]


################################################################
"""
Solution 3
"""


def to_dict(lst):
	tr = []
	for item in lst:
		tr.append({item: ord(item)})
	return tr



#################################################################
"""
Solution 4
"""

def to_dict(lst):
    l=[]
    for i in lst:
        di={}
        di[i]=ord(i)
        l.append(di)
    return l




