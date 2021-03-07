"""
Combined Consecutive Sequence

Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True


Notes
The input lists will have unique values.
The input lists can be in any order.
"""



################################################################
"""
Solution 1
"""


def consecutive_combo(a,b):
    c = a + b
    x,y = min(c),max(c)
    return list(range(x,y+1)) == sorted(c)




################################################################
"""
Solution 2
"""


consecutive_combo=lambda a,b:len(a+b)-1==max(a+b)-min(a+b)



################################################################
"""
Solution 3
"""


def consecutive_combo(lst1, lst2):
  
  for i in range(len(lst2)):
    lst1.append(lst2[i])
  
  sortedList = sorted(lst1)
  a = []
  
  for i in range(len(sortedList) - 1):
    if sortedList[i + 1] - sortedList[i] == 1:
      a.append(1)
    else:
      a.append(0)
  
  return True if len(set(a)) == 1 else False




################################################################
"""
Solution 4
"""


def consecutive_combo(list1, list2):
    x = list1 + list2
    x.sort()
    for i in range(0, len(x) - 1):
        if x[i + 1] - x[i] != 1:
            return False
    return True



