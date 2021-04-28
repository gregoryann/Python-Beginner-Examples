"""
Boolean Chain

Write three functions:

boolean_and
boolean_or
boolean_xor
These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.

Examples
boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False

boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True

boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False

Notes
XOR is the same as OR, except that it excludes [True, True].
Each time you evaluate an element at 0 and at 1, you collapse it into the single result.
"""



################################################################
"""
Solution 1
"""


from functools import reduce

def boolean_and(lst):
	return reduce(lambda a, b : a & b, lst)	

def boolean_or(lst):
	return reduce(lambda a, b : a | b, lst)	

def boolean_xor(lst):
	return reduce(lambda a, b : a ^ b, lst)




################################################################
"""
Solution 2
"""


def boolean_and(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, a and b)
  else:
    return lst[0] and lst[1]
  return boolean_and(lst)

def boolean_or(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, a or b)
  else:
    return lst[0] or lst[1]
  return boolean_or(lst)

def boolean_xor(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, (a and not b) or (not a and b))
    print(lst[0])
  else:
    return (lst[0] and not lst[1]) or (not lst[0] and lst[1])
  return boolean_xor(lst)




################################################################
"""
Solution 3
"""


def boolean_and(lst):
	return not False in lst

def boolean_or(lst):
	return True in lst
	
def boolean_xor(lst):
	while len(lst) > 1:
		tmp = []
		for i in range(len(lst)-1):
			a, b = lst[i:i+2]
			if (a or b) and not (a and b): tmp.append(True)
			else: tmp.append(False)
		lst = tmp[:]
	return tmp[0]



################################################################
"""
Solution 4
"""


import functools

def boolean_and(lst):
	return all(lst)

def boolean_or(lst):
	return any(lst)

def boolean_xor(lst):
	return functools.reduce(lambda a,b: a != b, lst)



