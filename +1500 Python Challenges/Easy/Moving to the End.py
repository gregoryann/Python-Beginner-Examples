"""
Moving to the End
Write a function that moves all elements of one type to the end of the list.

Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]

Notes
Keep the order of the un-moved items the same.
"""


"""
Solution 1
"""

def move_to_end(lst, el):
	return [x for x in lst if x!=el]+[el]*lst.count(el)

"""
Solution 2
"""

def move_to_end(lst, el):
	return sorted(lst, key=lambda x: x is el)

"""
Solution 3
"""

def move_to_end(lst, el):
	x=lst.count(el)
	while el in lst:
		lst.remove(el)
	lst.extend([el]*x)
	return lst

"""
Solution 4
"""

def move_to_end(lst, el):
	a = [x for x in lst if x != el]
	for x in range(lst.count(el)):
		a.append(el) 
	return a





