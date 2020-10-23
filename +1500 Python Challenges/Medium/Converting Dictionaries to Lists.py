"""
Converting Dictionaries to Lists

Write a function that converts a dictionary into a list, where each element represents a key-value pair in the form of a list. Sort the list alphabetically by key.

Examples
to_list({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]

to_list({ "shrimp": 15, "tots": 12 }) ➞ [["shrimp", 15], ["tots", 12]]

to_list({}) ➞ []

Notes
Return an empty list if the dictionary is empty.
"""



################################################################
"""
Solution 1
"""


def to_list(d):
	return sorted(list(i) for i in d.items())



################################################################
"""
Solution 2
"""


def to_list(dct):
	list = []
	for key,value in dct.items():
		list.append([key,value])
	list.sort()
	return list



################################################################
"""
Solution 3
"""


def to_list(my_dict):
    new_list = []
    for key in my_dict:
        new_list += [[key,my_dict[key]]]# key = key, my_dict[key] = value
        new_list.sort()
    return new_list




#################################################################
"""
Solution 4
"""

def to_list(dct):
	return sorted([[k,v] for k,v in dct.items()], key = lambda x: x[0])





#################################################################
"""
Solution 5
"""


def to_list(dct):
	x = []
	y = []
	for i in dct.keys():
		x.append(i)
	for j in dct.values():
		y.append(j)
	ans = []
	for i in list(zip(x,y)):
		ans.append(list(i))
	return sorted(ans)