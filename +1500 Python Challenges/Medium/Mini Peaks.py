"""
Mini Peaks

Write a function that returns all the elements in an array that are strictly greater than their adjacent left and right neighbors.

Examples
mini_peaks([4, 5, 2, 1, 4, 9, 7, 2]) ➞ [5, 9]
# 5 has neighbours 4 and 2, both are less than 5.

mini_peaks([1, 2, 1, 1, 3, 2, 5, 4, 4]) ➞ [2, 3, 5]

mini_peaks([1, 2, 3, 4, 5, 6]) ➞ []


Notes
Do not count boundary numbers, since they only have one left/right neighbor.
If no such numbers exist, return an empty array.
"""




################################################################
"""
Solution 1
"""


mini_peaks=lambda x:[k for j,k,l in zip(x,x[1:],x[2:])if j<k>l]



################################################################
"""
Solution 2
"""


def mini_peaks(lst):
	a=len(lst)
	newLst=[]
	for i in range(1,a-1):
		b=lst[i]
		if(b>lst[i-1] and b>lst[i+1]):
			newLst.append(lst[i])
	return newLst



################################################################
"""
Solution 3
"""


def mini_peaks(lst):
 output=[]
 for i in range(1,len(lst)-1):
  if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
   output.append(lst[i])
 return output



#################################################################
"""
Solution 4
"""


def mini_peaks(lst):
	return [y for x, y, z in zip(lst[:-2], lst[1:-1], lst[2:]) if y > x and y > z]




