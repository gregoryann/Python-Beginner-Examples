"""
Two Lists inside a List to One

Programmer Pete is trying to turn two lists inside one list into one without messing the order of the list nor the type and because he's pretty advanced he made it without blinking but I want you to make it too.

Examples
one_list([[1, 2], [3, 4]]) ➞ [1, 2, 3, 4]

one_list([["a", "b"], ["c", "d"]]) ➞ ["a", "b", "c", "d"]

one_list([[True, False], [False, False]]) ➞ [True, False, False, False]

Notes
Remember to return the list.
Check Resources for more info.
"""





#############################################################
"""
Solution 1
"""

def one_list(lst):
	return lst[0]+lst[1]




#############################################################
"""
Solution 2
"""

def one_list(lst):
    for x in range(len(lst)-1):
        return lst[x] + lst[x+1]





#############################################################
"""
Solution 3
"""

def one_list(lst):
	result = []
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			result.append(lst[i][j])
	return result





#############################################################
"""
Solution 4
"""

def one_list(lst):
	a = [i for i in lst[0]]
	b = [i for i in lst[1]]
	return a+b





#############################################################
"""
Solution 5
"""


def one_list(lst):
 x=[]
 for i in (lst) :
  for j in (i) :
	  x.append(j)
 return x