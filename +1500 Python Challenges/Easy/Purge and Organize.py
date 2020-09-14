"""
Purge and Organize

Given a list of numbers, write a function that returns a list that...

Has all duplicate elements removed.
Is sorted from least to greatest value.

Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]

unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]

unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]

"""


"""
Solution 1
"""

def unique_sort(lst):
  purgedList = []
  for i in sorted(lst):
    if i not in purgedList:
      purgedList.append(i)
  return purgedList

"""
Solution 2
"""

def unique_sort(lst):
    lst = set(lst)
    lst = list(lst)
    lst.sort()
    return lst

"""
Solution 3
"""

unique_sort = lambda l : sorted(set(l))

"""
Solution 4
"""
def unique_sort(lst):
    lst2 = list(dict.fromkeys(lst))
    lst2.sort()
    return lst2



