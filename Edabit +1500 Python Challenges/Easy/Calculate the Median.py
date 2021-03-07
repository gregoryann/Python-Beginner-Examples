"""
Calculate the Median

Create a function that takes a list of numbers and return its median. If the input list is even length, take the average of the two medians, else, take the single median.

Examples
median([2, 5, 6, 2, 6, 3, 4]) ➞ 4

median([21.4323, 432.54, 432.3, 542.4567]) ➞ 432.4

median([-23, -43, -29, -53, -67]) ➞ -43

Notes
Input can be any negative or positive number.
Input list will contain at least four numbers.
See Resources tab for info on calculating the median.
"""


#############################################################



"""
Solution 1
"""

def median(lst):
  lst.sort()
  n = len(lst)
  m = n // 2
  if n % 2 == 0:
    return (lst[m - 1] + lst[m]) / 2
  else:
    return lst[m]

"""
Solution 2
"""

import numpy
def median(lst):
	return numpy.median(lst)

"""
Solution 3
"""

def median(lst):
  lst.sort()
  l = len(lst)
  if l % 2 == 1:
    median = lst[int((l-1)/2)]
  else:
    median = (lst[int(l/2)]+lst[int((l/2)-1)])/2
  
  return median

"""
Solution 4
"""

def median(lst):
  med = int(len(lst) / 2)
  sLst = sorted(lst)
  if len(lst) % 2 != 0:
    return sLst[med]
  else:
    return (sLst[med] + sLst[med - 1])/2




