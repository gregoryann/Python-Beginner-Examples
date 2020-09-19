"""
Clone a List

The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?

Examples
clone([1, 1]) ➞ [1, 1, [1, 1]]

clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]

clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]
"""


"""
Solution 1
"""

def clone(lst):
    lst.append(lst[:])
    return lst

"""
Solution 2
"""

def clone(lst):
		lst2 = lst.copy()
		lst.append(lst2)
		return lst






