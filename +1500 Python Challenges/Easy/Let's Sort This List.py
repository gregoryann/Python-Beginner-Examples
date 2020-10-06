"""
Let's Sort This List!

Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]

asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]

asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]
"""





################################################################
"""
Solution 1
"""

def asc_des_none(lst, s):
    return sorted(lst, reverse=s == 'Des') if s else lst






################################################################
"""
Solution 2
"""

def asc_des_none(lst, s):
	if s=='Asc': return sorted(lst)
	elif s=='Des': return sorted(lst,reverse=True)
	else: return lst






################################################################
"""
Solution 3
"""

def asc_des_none(lst, s):
	if s != 'None':
		return sorted(lst, reverse=s=='Des')
	return lst







#################################################################
"""
Solution 4
"""


def asc_des_none(lst, s):
  if s == 'Asc':
    lst.sort()
    return lst
  elif s == 'Des':
    lst.sort()
    return lst[::-1]
  return lst





