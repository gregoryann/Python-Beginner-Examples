"""
Merge Lists in Order

Given two lists, merge them to one list and sort the new list in the same order as the first list.

Examples
merge_sort([1, 2, 3], [5, 4, 6]) ➞ [1, 2, 3, 4, 5, 6]

merge_sort([8, 6, 4, 2], [-2, -6, 0, -4]) ➞ [8, 6, 4, 2, 0, -2, -4, -6]

merge_sort([120, 180, 200], [190, 175, 130]) ➞ [120, 130, 175, 180, 190, 200]

Notes
You'll always get two lists as arguments.
The first list is always sorted, either asc or desc.
"""



################################################################
"""
Solution 1
"""


class List:
	
	def generate(lst):
		if lst == sorted(lst):
			return List(lst, 'a')
		elif lst == list(reversed(sorted(lst))):
			return List(lst, 'd')
		else:
			print('Invalid List Format! {}'.format(lst))
			return 'Invalid List Format!'
	
	def __init__(self, lst, asc_desc):
		self.lst = lst
		self.ad = asc_desc
	
	def merge(self, lst):
		
		nl = self.lst + lst
		if self.ad == 'a':
			nl = list(sorted(nl))
		else:
			nl = list(reversed(sorted(nl)))
		
		return List(nl, self.ad)

def merge_sort(lst1, lst2):
	
	l1 = List.generate(lst1)
	merged = l1.merge(lst2)
	
	return merged.lst




################################################################
"""
Solution 2
"""


def merge_sort(lst1, lst2):
	return sorted(lst1+lst2) if lst1==sorted(lst1) else sorted(lst1+lst2)[::-1]



################################################################
"""
Solution 3
"""


def merge_sort(lst1, lst2):
	items = [i for i in lst1] + [i for i in lst2];
	if(lst1[0] < lst1[1]):
		items.sort();
	else:
		items.sort(reverse=True)
	return items;




#################################################################
"""
Solution 4
"""


def merge_sort(lst1, lst2):
    if lst1[0]>lst1[1]:return sorted(lst1 + (lst2))[::-1]
    else:return sorted(lst1 + (lst2))




