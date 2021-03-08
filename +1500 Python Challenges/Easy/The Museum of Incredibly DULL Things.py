"""
The Museum of Incredibly DULL Things

A museum wants to get rid of some exhibitions. Katya, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and removes the one with the lowest rating. Just as she finishes rating the exhibitions, she's called off to an important meeting. She asks you to write a program that tells her the ratings of the items after the lowest one is removed.

Create a function that takes a list of integers and removes the smallest value.

Examples
remove_smallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]

remove_smallest([5, 3, 2, 1, 4]) ➞ [5, 3, 2, 4]

remove_smallest([2, 2, 1, 2, 1]) ➞ [2, 2, 2, 1]

Notes
Don't change the order of the left over items.
If you get an empty list, return an empty list: [] ➞ [].
If there are multiple items with the same value, remove item with lower index (3rd example).
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def remove_smallest(lst):
  if lst:
  	lst.remove(min(lst))
  return lst

"""
Solution 2
"""

def remove_smallest(lst):
  if lst != []:
  	lst.remove(min(lst))
  return lst


"""
Solution 3
"""

def remove_smallest(lst):
  lst if len(lst) < 1 else lst.remove(min(lst))
  return lst


"""
Solution 4
"""

def remove_smallest(lst):
  if lst == []: return []
  else:
  	mins=[(i,x) for i,x in enumerate(lst) if x==min(lst)]
  	lst.pop(mins[0][0])
  return lst






