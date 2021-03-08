"""
Calculate the Mean

Create a function that takes a list of numbers and returns the mean value.

Examples
mean([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3]) ➞ 2.55

mean([2, 3, 2, 3]) ➞ 2.50

mean([3, 3, 3, 3, 3]) ➞ 3.00

Notes
Round to two decimal places.
You can expect a number ranging from 0 to 10,000.

"""


"""
Solution 1
"""

def mean(lst):
  return round(sum(lst) / len(lst), 2)


"""
Solution 2
"""

import statistics

def mean(lst):
	return round(statistics.mean(lst),2)

"""
Solution 3
"""

def mean(lst):
	return float(('%.2f') %(sum(lst)*1.0/len(lst)))

"""
Solution 4
"""

def mean(lst):
  count = len(lst)
  ssum = sum(lst)
  return round(ssum/count,2)


"""
Solution 5
"""

def mean(lst):
  mean = 0
  for i in lst:
    mean += i
  return(round(mean/len(lst),2))