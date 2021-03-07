"""
Delete Occurrences of Extra Elements in a List

Create a function that takes two arguments: a list lst and a number num. If an element occurs in lst more than num times, remove the extra occurrence(s) and return the result.

Examples
delete_occurrences([1, 1, 1, 1], 2) ➞ [1, 1]

delete_occurrences([13, True, 13, None], 1) ➞ [13, True, None]

delete_occurrences([True, True, True], 3) ➞ [True, True, True]

Notes
Do not alter the order of the original list.
"""



################################################################
"""
Solution 1
"""


def delete_occurrences(lst, num):
	new_lst = []
	for i in lst:
		if new_lst.count(i) < num:
			new_lst.append(i)
	return new_lst



################################################################
"""
Solution 2
"""


def delete_occurrences(lst, num):
	return [i for idx, i in enumerate(lst) if lst[:idx+1].count(i) <= num]



################################################################
"""
Solution 3
"""


def delete_occurrences(lst, num):
	for item in lst: 
		while lst.count(item) > num: 
				lst.reverse()
				lst.remove(item)
				lst.reverse()
	return lst



#################################################################
"""
Solution 4
"""


def delete_occurrences(lst, num):
    for i in lst:
        occ = lst.count(i)
        while occ > num:
            lst.reverse()
            lst.remove(i)
            lst.reverse()
            occ = occ - 1
    return lst


print(delete_occurrences([13, True, 13, None], 1))




#################################################################
"""
Solution 5
"""


def delete_occurrences(lst, num):
	list1=lst
	list2 = []
	revlist  = list1[::-1]
	number = num
	for k in list1:
		while list1.count(k) > number:
			getindex = revlist.index(k)
			revlist.pop(getindex)
			list1 = revlist[:]

	return (list1[::-1])