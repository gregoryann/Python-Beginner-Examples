"""
Return the Highest and Lowest Numbers

Create a function that accepts a string of space separated integers and returns the highest and lowest integers (as a string).

Examples
high_low("1 2 3 4 5") ➞ "5 1"

high_low("1 2 -3 4 5") ➞ "5 -3"

high_low("1 9 3 4 -5") ➞ "9 -5"

high_low("13") ➞ "13 13"

Notes
All integers are valid, no need to validate them.
There will always be at least one integer in the input string.
Output string must be two integers separated by a single space, and highest number is first.
"""


################################################################



"""
Solution 1
"""

def high_low(t):
	l=[int(x)for x in t.split()]
	return '%s %s'%(max(l),min(l))

"""
Solution 2
"""

def high_low(txt):
    if len(txt) == 1:
        return txt + " " + txt
    else:
        lst = txt.split()
        lst = list(map(int, lst))
        lst.sort()
        return str(lst[-1]) + ' ' + str(lst[0])

"""
Solution 3
"""

def high_low(txt):
	l = list(map(lambda x: int(x), txt.split()))
	return '{} {}'.format(max(l), min(l))

"""
Solution 4
"""

import re
def high_low(txt):
	regResult = result = re.findall(r'[" "]?[-+]?["\d"]+[" "]?',txt)
	tmp = [int(i) for i in regResult]
	minmax = [max(tmp), min(tmp)]
	minmax = [str(i) for i in minmax]
	return " ".join(minmax)




