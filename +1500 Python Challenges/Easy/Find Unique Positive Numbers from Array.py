"""
Find Unique Positive Numbers from Array

Write a function that takes a list and returns a new list with unique positive (more than 0) numbers.

Examples
unique_lst([-5, 1, -7, -5, -2, 3, 3, -5, -1, -1]) ➞ [1, 3]

unique_lst([3, -3, -3, 5, 5, -6, -2, -4, -1, 3]) ➞ [3, 5]

unique_lst([10, 6, -12, 13, 5, 5, 13, 6, 5]) ➞ [10, 6, 13, 5]

Notes
Return the elements in the order that they are found in the list.
Your function should also work for empty lists.
"""





################################################################
"""
Solution 1
"""

def unique_lst(lst):
	return sorted(set(i for i in lst if i > 0), key=lst.index)





################################################################
"""
Solution 2
"""

def unique_lst(lst):
    newlst = []
    for l in lst:
        if l > 0 and l not in  newlst:
            newlst.append(l)
    return newlst






################################################################
"""
Solution 3
"""

unique_lst=lambda l:sorted((x for x in set(l)if x>0),key=l.index)







#################################################################
"""
Solution 4
"""


def unique_lst(lst):
    l1=[]
    for i in lst:
        if i>0 and l1.count(i)<1:l1.append(i)
    return l1




