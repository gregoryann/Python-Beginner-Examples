"""
Extremely Over-Nested

Create a function that returns the original value from a list with too many sub-lists.

Examples
de_nest([[[[[[[[[[[[3]]]]]]]]]]]]) ➞ 3

de_nest([[[[[[[True]]]]]]]) ➞ True

de_nest([[[[[[[[[[[[[[[[["edabit"]]]]]]]]]]]]]]]]]) ➞ "edabit"

Notes
You only need to retrieve one element.
"""




################################################################
"""
Solution 1
"""


def de_nest(lst):
	return eval(str(lst).strip('[]'))






################################################################
"""
Solution 2
"""


import re
de_nest=lambda l:eval(re.sub('[\[\]]+','',str(l)))







################################################################
"""
Solution 3
"""


def de_nest(lst):
	return eval(str(lst).replace('[', '').replace(']', ''))







#################################################################
"""
Solution 4
"""


import numpy
def de_nest(lst):
  return list(numpy.array(lst).flat)[0]




