"""
Sort by String Length

Create a function that returns a list of strings sorted by length in ascending order.

Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]

sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]

sort_by_length([]) ➞ []

Notes
Strings will have unique lengths, so don't worry about comparing two strings with identical length.
Return an empty array if the input array is empty (see example #4).
"""


"""
Solution 1
"""

def sort_by_length(lst):
  return sorted(lst, key=len)


"""
Solution 2
"""

def sort_by_length(lst):
	lst.sort(key=len)
	return lst

"""
Solution 3
"""

def sort_by_length(lst):
    return list(sorted(lst,key = len,reverse = False))

"""
Solution 4
"""

def sort_by_length(lst):
	return sorted(lst,key=lambda x:len(x))




