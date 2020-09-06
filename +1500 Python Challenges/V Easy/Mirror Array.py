"""

Mirror Array
Given a list, transform it into a mirror.

Examples
mirror([0, 2, 4, 6]) ➞ [0, 2, 4, 6, 4, 2, 0]
mirror([1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 5, 4, 3, 2, 1]
mirror([3, 5, 6, 7, 8]) ➞ [3, 5, 6, 7, 8, 7, 6, 5, 3]

Notes
Do not repeat the last item of the given list.

"""


"""
Solution 1
"""

def mirror(lst):
  return lst + lst[-2::-1]

"""
Solution 2
"""

def mirror(lst):
	for i in lst[len(lst)-2::-1]:
		lst.append(i)
	return lst

"""
Solution 3
"""

def mirror(lst):
 a=lst[:-1]
 b=a[::-1]
 c=lst+b
 return c





