"""
Remove Duplicates from a List

Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).

Examples
remove_dups([1, 0, 1, 0]) ➞ [1, 0]

remove_dups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]

remove_dups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]

Notes
Tests contain lists with both strings and numbers.
Tests are case sensitive.
"""



########################################################################


"""
Solution 1
"""


def remove_dups(lst):
  return sorted(set(lst),key=lst.index)


"""
Solution 2
"""

def remove_dups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


"""
Solution 3
"""

import collections
def remove_dups(lst):
  return list(collections.OrderedDict.fromkeys(lst))


"""
Solution 4
"""

def remove_dups(lst):
	return sorted(set(lst), key=lambda x: lst.index(x))




