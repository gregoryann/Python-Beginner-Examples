"""
Filter out Strings from an Array

Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]

Notes
Zero is a non-negative integer.
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def filter_list(lst):
    return [l for l in lst if isinstance(l, int)]

"""
Solution 2
"""

def filter_list(lst):
	return [i for i in lst if i * 0 == 0]

"""
Solution 3
"""

def filter_list(lst):
  all_num = []
  
  for i in lst:
    if type(i) == int:
      all_num.append(i)
    else:
      pass
  return all_num


"""
Solution 4
"""

def filter_list(lst):
    return list(filter(lambda x: not type(x) == str, lst))

