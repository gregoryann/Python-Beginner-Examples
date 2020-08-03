"""

Return the Last Element in a List
Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.

Examples
get_last_item([1, 2, 3]) ➞ 3

get_last_item(["cat", "dog", "duck"]) ➞ "duck"

get_last_item([True, False, True]) ➞ True

get_last_item([7, "String", False]) ➞ False
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""


def get_last_item(lst):
  return lst[-1]




"""
Solution 2
"""


def get_last_item(lst):
	return lst.pop()


"""
Solution 3
"""


def get_last_item(lst):
  return lst[len(lst)-1]


"""
Solution 4
"""

def getLastItem(lst):
    '''Returns the last item in the list.

    >>> getLastItem([1, 2, 3])
    3
    >>>
    '''
    return lst[-1]




