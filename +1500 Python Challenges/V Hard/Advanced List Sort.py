"""
Advanced List Sort

Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]


Notes
The sublists should be returned in the order of each element's first appearance in the given list.
"""



#########################################################
"""
Solution 1
"""


def advanced_sort(lst):
	return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]



#########################################################
"""
Solution 2
"""


from collections import Counter


def advanced_sort(lst):
    c = Counter(lst)
    pairs = ((k, [k] * v) for k, v in c.items())
    return [
        b
        for a, b in sorted(pairs, key=lambda x: lst.index(x[0]))
    ]




#########################################################
"""
Solution 3
"""


def advanced_sort(lst):
	a = [[i]*lst.count(i) for i in lst]
	b = []
	for i in a:
		if i not in b:
			b.append(i)
	return b





#########################################################
"""
Solution 4
"""


def advanced_sort(lst):
	unique = [] 
	for x in lst:
		if x not in unique:
			unique.append(x)
			
	result = []
	for uni_obj in unique:
		temp = []
		while uni_obj in lst:
			lst.remove(uni_obj)
			temp.append(uni_obj)
		result.append(temp)
	return result



