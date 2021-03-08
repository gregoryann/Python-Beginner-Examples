"""
Find the Largest Even Number

Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in function max() and sorted() are prohibited.

Examples
largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10

largest_even([1, 3, 5, 7]) ➞ -1

largest_even([0, 19, 18973623]) ➞ 0

Notes
Consider using the modulo operator % or the bitwise and operator &.
"""




################################################################
"""
Solution 1
"""


def largest_even(lst):
    res = -1
    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res



################################################################
"""
Solution 2
"""


def largest_even(r, n=-1):
  if not r: return n
  n = [n, r[0]][not r[0] & 1 and r[0] > n]
  return largest_even(r[1:], n)




################################################################
"""
Solution 3
"""


def largest_even(l):
  
  l = list( map( lambda x: x if not x%2 else -1, l ) )
  return sorted(l)[-1]




#################################################################
"""
Solution 4
"""


def largest_even(lst):
	even = [k for k in lst if k % 2 == 0]
	return -1 if len(even) == 0 else max(even)




