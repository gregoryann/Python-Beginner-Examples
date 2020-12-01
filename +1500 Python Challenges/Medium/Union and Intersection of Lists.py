"""
Union and Intersection of Lists

Create a function takes in two lists and returns an intersection list and a union list.

Intersection List: Elements shared by both.
Union List: Elements that exist in first or second list, or both (not exclusive OR).
While the input lists may have duplicate numbers, the returned intersection and union lists should be set-ified - that is, contain no duplicates. Returned lists should be sorted in ascending order.

List 1: [5, 6, 6, 6, 8, 9]
List 2: [3, 3, 4, 4, 5, 5, 8]

Intersection: [5, 8]
# 5 and 8 are the only 2 numbers that exist in both lists.

Union: [3, 4, 5, 6, 8, 9]
# Each number exists in at least one list.
Examples
intersection_union([1, 2, 3, 4, 4], [4, 5, 9]) ➞ [[4], [1, 2, 3, 4, 5, 9]]

intersection_union([1, 2, 3], [4, 5, 6]) ➞ [[], [1, 2, 3, 4, 5, 6]]

intersection_union([1, 1], [1, 1, 1, 1]) ➞ [[1], [1]]


Notes
Order of output should be: [Intersection], [Union].
Remember both output lists should be in ascending order.
Each input list will have at least one element.
If both lists are disjoint (share nothing in common), return an empty list [] for the intersection.
"""



################################################################
"""
Solution 1
"""


intersection_union=lambda a,b:(lambda x,y:[sorted(x&y),sorted(x|y)])(set(a),set(b))



################################################################
"""
Solution 2
"""


def intersection_union(lst1, lst2):
	union = sorted(set(lst1).union(set(lst2)))
	intersection = sorted(set(lst1).intersection(set(lst2)))
	return [intersection, union]



################################################################
"""
Solution 3
"""


def intersection_union(lst1, lst2):
    intersection = list(set([x for x in lst1 if x in lst2]))
    intersection.sort()
    union = list(set(lst1 + lst2))
    union.sort()
    return [intersection, union]



#################################################################
"""
Solution 4
"""


def intersection_union(lst1, lst2):
	
	intList = []

	unionList = []

	linkedLists = lst1 + lst2

	for i in lst1:
			if i in lst2 and i not in intList:
					intList.append(i)

	for i in linkedLists:
			if i not in unionList:
					unionList.append(i)

	return [sorted(intList), sorted(unionList)]



