"""
Is There an Upward Trend?

Create a function that determines if there is an upward trend.

Examples
upward_trend([1, 2, 3, 4]) ➞ True

upward_trend([1, 2, 6, 5, 7, 8]) ➞ False

upward_trend([1, 2, 3, "4"]) ➞ "Strings not permitted!"

upward_trend([1, 2, 3, 6, 7]) ➞ True

Notes
If there is a string element in the list, return "Strings not permitted!".
The numbers don't have to be consecutive (e.g. [1, 3, 5] should still return True).
"""





################################################################
"""
Solution 1
"""

upward_trend=lambda l:'Strings not permitted!'if any(type(x)==str for x in l) else all(x-y<0for x,y in zip(l,l[1:]))




################################################################
"""
Solution 2
"""

def upward_trend(lst):
	try:
		return sorted(lst) == lst
	except:
		return "Strings not permitted!"





################################################################
"""
Solution 3
"""

def upward_trend(lst):
	if all(str(type(i)) == '<class \'int\'>' for i in lst):
		return all(lst[i+1] > lst[i] for i in range(len(lst)-1))
	return 'Strings not permitted!'







#################################################################
"""
Solution 4
"""


def upward_trend(lst):
  x = [i for i in lst if type(i) != int]
  if x != []:
    return "Strings not permitted!"
  growth = []
  for i in range(1,len(lst)):
    if lst[i] > lst[i - 1]:
      growth.append(i)
  return len(lst) == len(growth) + 1





