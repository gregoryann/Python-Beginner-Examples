"""
Peeling off the Outer Layers

Given a list of lists, return a new list of lists containing every element, except for the outer elements.

Examples
peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["f", "g"],
  ["j", "k"]
]

peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]) ➞ [
  [7, 8, 9],
  [12, 13, 14],
  [17, 18, 19],
  [22, 23, 24],
  [27, 28, 29]
]

peel_layer_off([
  [True, False, True],
  [False, False, True],
  [True, True, True]
]) ➞ [[False]]

peel_layer_off([
  ["hello", "world"],
  ["hello", "world"]
]) ➞ []

Notes
The 2D grid is always a rectangular/square shape.
Always return some form of nested list, unless there are no elements. In that case, return an empty list.
"""



################################################################
"""
Solution 1
"""


def peel_layer_off(lst):
 lst.pop(0)
 lst.pop(-1)
 for i in lst:
  i.pop(0)
  i.pop(-1)
 return lst





################################################################
"""
Solution 2
"""


def peel_layer_off(lst):
	lst2=[]
	for l in range(len(lst)):
		if l==0 or l==len(lst)-1:
			continue
		lst2.append(lst[l][1:-1])
	return lst2





################################################################
"""
Solution 3
"""

def peel_layer_off(lst):   
    if len(lst) < 3 or len(lst[0]) < 3:
        return []
    ans = []
    for r in range(1, len(lst)-1):
        ans.append(lst[r][1:len(lst[0])-1])
    return ans




#################################################################
"""
Solution 4
"""


def peel_layer_off(lst):
	arr = []
	for i in range(1,len(lst)-1):
		row = []
		for j in range(1,len(lst[i])-1):
			row.append(lst[i][j])
		arr.append(row)
	return arr



