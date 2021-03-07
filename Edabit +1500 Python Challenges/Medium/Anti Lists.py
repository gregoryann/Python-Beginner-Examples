"""
Anti Lists

Given two lists, return whether the two lists are opposites of each other. That means that both lists are comprised only from elements a and b and that the occurences of these elements are swapped between the two lists.

Examples
is_anti_list(['1', '0', '0', '1'], ['0', '1', '1', '0']) ➞ True

is_anti_list(['apples', 'bananas', 'bananas'], ['bananas', 'apples', 'apples']) ➞ True

is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]) ➞ False

Notes
All tests will include only two different elements.
"""



################################################################
"""
Solution 1
"""


def is_anti_list(lst1, lst2):
	return all({a, b} == set(lst1) for a, b in zip(lst1, lst2))


################################################################
"""
Solution 2
"""


def is_anti_list(lst1, lst2):
	seen = set()
	for i, j in zip(lst1, lst2):
		seen.update((i, j))
		if i == j or len(seen) > 2:
			return False
	return True



################################################################
"""
Solution 3
"""


def is_anti_list(lst1, lst2):
	if set(lst1).difference(lst2):
		return False
	return all([True if x != y else False for x, y in zip(lst1, lst2)])



#################################################################
"""
Solution 4
"""


def is_anti_list(list_a: list, list_b: list):
    if len(set(list_a) | set(list_b)) == 2:
        for a, b in zip(list_a, list_b):
            if a == b:
                return False
        return True
    return False




