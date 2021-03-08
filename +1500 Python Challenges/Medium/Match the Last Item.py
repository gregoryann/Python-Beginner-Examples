"""
Match the Last Item

Create a function that takes a list of items and checks if the last item matches the rest of the list concatenated together.

Examples
match_last_item(["rsq", "6hi", "g", "rsq6hig"]) ➞ True
# The last item is the rest joined.

match_last_item([1, 1, 1, "11"]) ➞ False
# The last item should be "111".

match_last_item([8, "thunder", True, "8thunderTrue"]) ➞ True

Notes
The list is always filled with items.
"""



################################################################
"""
Solution 1
"""


def match_last_item(lst):
	return ''.join(map(str, lst[:-1])) == lst[-1]




################################################################
"""
Solution 2
"""


match_last_item = lambda r: r.pop() == ''.join(map(str, r))



################################################################
"""
Solution 3
"""


def match_last_item(lst):
	ans = []
	for x in range(len(lst)):
		if lst[x] != lst[-1]:
			ans.append(str(lst[x]))
	return ''.join(ans) == lst[-1]



#################################################################
"""
Solution 4
"""


def match_last_item(lst):

	lst_string = [
		str(item)
		for item in lst
	]
	return (''.join(lst_string[:-1]) == lst_string[-1])



