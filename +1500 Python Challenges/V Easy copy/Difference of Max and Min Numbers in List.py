"""

Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.

Examples
difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.

difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.
Notes



"""






"""
Solution 1
"""


def difference_max_min(lst):
	return max(lst) - min(lst)




"""
Solution 2
"""

def difference_max_min(lst):
		lst.sort()
		return lst[-1] - lst[0]



"""
Solution 3
"""


def difference_max_min(lst):
	mx=lst[0]
	mi=lst[0]
	for i in lst:
		if mx<i:
			mx=i
		if mi>i:
			mi=i
	return mx-mi


"""
Solution 4
"""



def difference_max_min(lst):
	ooga = max(lst)
	booga = min(lst)
	return ooga - booga



