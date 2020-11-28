"""
Intersection of Two Dictionaries

Write a function that takes as input two different dictionaries and filters the keys in each dictionary to only keep keys that exist in both dictionaries. Store your result as a list with two dictionaries.

Examples
dict1 = {"a": 5, "b": 13, "c": 7}
dict2 = {"b": 5, "c": 8, "d": 91, "e": 99}
dict3 = {"a": 1, "b": 34}
dict4 = {"c": 9, "d": 8}

intersection(dict1, dict2) ➞ [{"b": 13, "c": 7}, {"b": 5, "c": 8}]

intersection(dict1, dict4) ➞ [{"c": 7}, {"c": 9}]

intersection(dict3, dict4) ➞ [{}, {}]


Notes
If no keys are shared between both dictionaries, return a list of empty dictionaries (see last example).
"""



################################################################
"""
Solution 1
"""


def intersection(h1, h2):
    a = {k: v for k, v in h1.items() if k in h2}
    b = {k: v for k, v in h2.items() if k in h1}
    return [a, b]



################################################################
"""
Solution 2
"""


intersection=lambda a,b:[{x:a[x]for x in set(a)&set(b)},{x:b[x]for x in set(b)&set(a)}]


################################################################
"""
Solution 3
"""


def intersection(h1, h2):
	hi1, hi2 = {}, {}
	for key in set(h1.keys()).intersection(set(h2.keys())):
		hi1[key] = h1[key]
		hi2[key] = h2[key]
	return [hi1, hi2]



#################################################################
"""
Solution 4
"""


def intersection(h1, h2):
    a = h1.keys() & h2.keys()
    return [{i:h1[i]for i in a},{i:h2[i]for i in a}]



