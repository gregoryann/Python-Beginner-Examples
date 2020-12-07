"""
Face Interval

In mathematics, interval is the difference between the largest number and the smallest number in a list.

To illustrate:

A = (3, 5, 7, 23, 11, 42, 80)

Interval of A = 80 - 3 = 77
Create a function that takes a list and returns ":)" if the interval of the list is equal to any other element; otherwise return ":(".

Examples
face_interval([1, 2, 5, 8, 3, 9]) ➞ ":)"
# List interval is equal to one of the other elements.

face_interval([5, 2, 8, 3, 11]) ➞ ":("
# List interval is not among the other elements.

face_interval("bruh") ➞ ":/"
# "bruh" is not a list. It's string.


Notes
Lists won't contain any duplicate numbers.
If you're not given a list, return ":/"
"""



################################################################
"""
Solution 1
"""


face_interval=lambda l:list==type(l)and(':(',':)')[max(l)-min(l)in l]or':/'



################################################################
"""
Solution 2
"""


def face_interval(lst):
  if not isinstance(lst, list):
    return ':/'
  else:  
    m1 = min(lst)
    m2 = max(lst)
    diff = m2 - m1   
    return ''.join([':)' if i == diff else '' for i in lst]) or ':('




################################################################
"""
Solution 3
"""


def face_interval(num):
    if num == str(num):
        return(':/')
    num.sort(reverse=False)
    if (num[len(num)-1] - num[0]) in num:
        return':)'
    else:
        return':('




#################################################################
"""
Solution 4
"""


def face_interval(n):
	return ':{}'.format('/' if type(n)!=list else ')' if max(n)-min(n) in n else '(')



