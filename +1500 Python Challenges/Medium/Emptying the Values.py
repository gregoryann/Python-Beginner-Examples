"""
Emptying the Values

Given a list of values, return a list with each value replaced with the empty value of the same type.

More explicitly:

Replace integers (e.g. 1, 3), whose type is int, with 0
Replace floats (e.g. 3.14, 2.17), whose type is float, with 0.0
Replace strings (e.g. "abcde", "x"), whose type is str, with ""
Replace booleans (True, False), whose type is bool, with False
Replace lists (e.g. [1, "a", 5], [[4]]), whose type is list, with []
Replace tuples (e.g. (1,9,0), (2,)), whose type is tuple, with ()
Replace sets (e.g. {0,"a"}, {"b"}), whose type is set, with set()
Caution: Python interprets {} as the empty dictionary, not the empty set.
None, whose type is NoneType, is preserved as None
Examples
empty_values([1, 2, 3]) ➞ [0, 0, 0]

empty_values([7, 3.14, "cat"]) ➞ [0, 0.0, ""]

empty_values([[1, 2, 3], (1,2,3), {1,2,3}]) ➞ [[], (), set()]

empty_values([[7, 3.14, "cat"]]) ➞ [[]]

empty_values([None]) ➞ [None]

Notes
None has the special NoneType all for itself.
"""




################################################################
"""
Solution 1
"""


def empty_values(lst):
	return [type(x)() for x in lst]



################################################################
"""
Solution 2
"""

def empty_values(lst):
    d = {type(1):0,
         type(1.0):0.0,
         type('a'):'',
         type(True):False,
         type([1]):[],
         type((1,)):(),
         type({1}):set(),
         type(None):None,}
    return [d[type(x)] for x in lst]



################################################################
"""
Solution 3
"""


def empty_values(lst):
  bang=[]
  for x in lst:
    z=str(type(x))
    if 'int' in z:
      bang.append(0)
    elif 'float' in z:
      bang.append(0.0)
    elif 'str' in z:
      bang.append('')
    elif 'list' in z:
      bang.append([])
    elif 'set' in z:
      bang.append(set())
    elif 'tuple' in z:
      bang.append(tuple())
    elif 'None' in z:
      bang.append(None)
    else:
      bang.append(False)
  
  return bang



#################################################################
"""
Solution 4
"""


def empty_values(lst):
	l = {int:0, float:0, list:[], str: "", bool:False, dict: {}, set:set(), tuple:()}
	return [l[type(i)] if i!= None else i for i in lst]




