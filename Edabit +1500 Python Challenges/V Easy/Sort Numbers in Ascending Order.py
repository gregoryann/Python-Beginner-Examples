"""
Sort Numbers in Ascending Order
Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).

Sort numbers list in ascending order.
If the function's argument is None or an empty list; return an empty list.
Return a new array of sorted numbers.
Examples
sort_nums_ascending([1, 2, 10, 50, 5]) ➞ [1, 2, 5, 10, 50]

sort_nums_ascending([80, 29, 4, -95, -24, 85]) ➞ [-95, -24, 4, 29, 80, 85]

sort_nums_ascending([]) ➞ []
Notes
Test input can be positive or negative.

"""



"""
Solution 1
"""

def sort_nums_ascending(lst):
  return sorted(lst)

"""
Solution 2
"""

def sort_nums_ascending(lst):
  newlist=list()
  for i in range(len(lst)):
    newlist.append(min(lst))
    lst.remove(min(lst))
  return newlist

"""
Solution 3
"""

sort_nums_ascending = sorted

"""
Solution 4
"""

def sort_nums_ascending(lst):
    lst.sort();
    return(lst);


"""
Solution 5
"""

def sort_nums_ascending(lst):
    if lst!=[]:
      lst.sort()
      return lst
    else:
      return lst


"""
Solution 6
"""

def sort_nums_ascending(lst):
    lst.sort()
    sorted_list = []
    for num in lst:
      sorted_list.append(num)
    return sorted_list
