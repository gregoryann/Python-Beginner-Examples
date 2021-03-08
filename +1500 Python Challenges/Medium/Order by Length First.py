"""
Order by Length First

Graded lexicographic order (grlex order for short) is a way of ordering words that:

First orders words by length.
Then orders words of the same size by their dictionary order.
For example, in grlex order:

"tray" < "trapped" since "tray" has length 4 while "trapped" has length 7.
"trap" < "tray" since both have length 4, but "trap" comes before "tray" in the dictionary.
Given a list of words, return that list in grlex order.

Examples
make_grlex(["small", "big"]) ➞ ["big", "small"]

make_grlex(["cat", "ran", "for", "the", "rat"]) ➞ ["cat", "for", "ran", "rat", "the"]

make_grlex(["this", "is", "a", "small", "test"]) ➞ ["a", "is", "test", "this", "small"]
"""




################################################################
"""
Solution 1
"""


def make_grlex(lst):
    return sorted(lst, key=lambda w: (len(w), w))



################################################################
"""
Solution 2
"""


def make_grlex(lst):
	lst.sort()
	lst.sort(key = len)
	return lst



################################################################
"""
Solution 3
"""


def make_grlex(lst):
	sort = sorted(lst, key= str.lower)
	sum_len = 0
	for word in lst:
		sum_len += len(word) 
	length = sum_len / len(lst)
	if length != len(sort[0]):
		return sorted(sort, key=len)
	else:
		return sort


#################################################################
"""
Solution 4
"""


def make_grlex(lst):
	res = []
	mn = min(len(i) for i in lst)
	mx = max(len(i) for i in lst)
	for i in range(mn,mx+1):
		temp = []
		for word in lst:
			if len(word) == i: temp.append(word)
		res += sorted(temp)
	return res



