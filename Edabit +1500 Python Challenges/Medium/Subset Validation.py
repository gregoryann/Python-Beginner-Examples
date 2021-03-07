"""
Subset Validation

Write a function that returns True if all subsets in a list belong to a given set.

Examples
validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True

validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True

validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False

validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False


Notes
The empty set and the set itself are both valid subsets of a set (we are not talking about proper subsets here).
The set and the subset will each have unique elements.
"""


################################################################
"""
Solution 1
"""


def validate_subsets(subsets, my_set):
	return all(set(x).issubset(my_set) for x in subsets)



################################################################
"""
Solution 2
"""


def validate_subsets(subsets, my_set):
	return set(sum(subsets, [])) == set(my_set)



################################################################
"""
Solution 3
"""


validate_subsets=lambda l,s:all(set(e)<=set(s)for e in l)



#################################################################
"""
Solution 4
"""


def validate_subsets(subsets, my_set):
	l = []
	for i in subsets:
		l.extend(i)
	return set(l) in set(my_set) or set(l) == set(my_set)



