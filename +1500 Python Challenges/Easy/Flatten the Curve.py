"""
Flatten the Curve

Given a list of integers, replace every number with the average mean of the whole list.

Examples
flatten_the_curve([1, 2, 3, 4, 5]) ➞ [3, 3, 3, 3, 3]

flatten_the_curve([0, 0, 0, 2, 7, 3]) ➞ [2, 2, 2, 2, 2, 2]

flatten_the_curve([4]) ➞ [4]

flatten_the_curve([]) ➞ []

Notes
Round averages to 1 decimal point.
Return an empty list if given an empty list (see example #4).
"""


"""
Solution 1
"""

def flatten_the_curve(lst):
	return [round(sum(lst)/len(lst), 1)] * len(lst) if lst else []

"""
Solution 2
"""

def flatten_the_curve(lst):
	import statistics as stat
	return [round(stat.mean(lst),1) for i in lst]

"""
Solution 3
"""

def flatten_the_curve(lst):
	if not lst: return []
	
	mean = round(sum(lst)/len(lst),1)
	return [mean for i in lst]

"""
Solution 4
"""

def flatten_the_curve(lst):
	import statistics
	mean_val = 0
	if len(lst) > 0:
		mean_val = statistics.mean(lst)
	mean_val = round(mean_val,1)
	final_list = []
	for i in lst:
		final_list.append(mean_val)
	return final_list




