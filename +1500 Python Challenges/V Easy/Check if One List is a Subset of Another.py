"""
Check if One List is a Subset of Another

List A is contained inside list B if each element in A also exists in B.

The number of times a number is present doesn't matter. In other words, if we transformed both lists into sets, A would be a subset of B.

A = [3, 3, 9, 9, 9, 5]
B = [1, 3, 9, 5, 8, 44, 44]

A_Set = [3, 9, 5]
B_Set = [1, 3, 9, 5, 8, 44]

# A_Set is a subset of B_Set
Create a function that determines if the first list is a subset of the second.


Examples

subset([1, 3], [1, 3, 3, 5]) ➞ True
subset([4, 8, 7], [7, 4, 4, 4, 9, 8]) ➞ True
subset([1, 3], [1, 33]) ➞ False
subset([1, 3, 10], [10, 8, 8, 8]) ➞ False

Notes
Each input list will have at least one element.
Check the resources tab for a hint.

"""



"""
Solution 1
"""

def subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

"""
Solution 2
"""

def subset(lst1, lst2):
	return min([x in lst2 for x in lst1])

"""
Solution 3
"""

def subset(lst1, lst2):
	return set(lst1) & set(lst2) == set(lst1)

"""
Solution 4
"""

def subset(A, B):
	return set(A) <= set(B)

"""
Solution 5
"""

def subset(lst1, lst2):
	smaller = lst1 if len(lst1) <= len(lst2) else lst2
	larger = lst2 if smaller == lst1 else lst1
	
	return all([i in larger for i in smaller])