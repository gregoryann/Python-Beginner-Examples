"""
How Much is True?
Create a function which returns the number of True values in a list.

Examples
count_true([True, False, False, True, False]) ➞ 2

count_true([False, False, False, False]) ➞ 0

count_true([]) ➞ 0
Notes
Return 0 if given an empty list.
All list items are of the type bool (True or False).

"""






"""
Solution 1
"""

def count_true(lst):
	return sum(lst)


"""
Solution 2
"""

def count_true(lst):
	return lst.count(True) if len(lst)>0 else 0


"""
Solution 3
"""

def count_true(lst):
	count = 0
	for i in lst:
		if i == True:
			count += 1
	return count

"""
Solution 4
"""

def count_true(lst):

    return sum(bool(x) for x in lst)
    



    def count_true(lst):
	NumberTrue = lst.count(True)
	return NumberTrue




