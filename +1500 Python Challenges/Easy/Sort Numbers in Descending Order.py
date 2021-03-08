"""
Sort Numbers in Descending Order

Create a function that takes any non-negative number as an argument and returns it with its digits in descending order. Descending order is when you sort from highest to lowest.

Examples
sort_descending(123) ➞ 321

sort_descending(1254859723) ➞ 9875543221

sort_descending(73065) ➞ 76530

Notes
You can expect non-negative numbers for all test cases.
"""



########################################################################






########################################################################
"""
Solution 1
"""

def sort_descending(num):
  return int(''.join(sorted(str(num), reverse = True)))





########################################################################
"""
Solution 2
"""

sort_descending=lambda n:int(''.join(sorted(str(n),reverse=True)))





########################################################################
"""
Solution 3
"""

def sort_descending(number):
  lst = []
  number = str(number)
  for i in number:
    lst.append(i)
  a = sorted(lst)
  a = ''.join(a)
  a = int(a[::-1])
  return a






########################################################################
"""
Solution 4
"""

def sort_descending(num):
    numlist = [str(x) for x in str(num)]
    numlist.sort()
    numlist.reverse()
    return int(''.join(numlist))





########################################################################
"""
Solution 5
"""

def sort_descending(num):
    '''Takes any non-negative number.
    Returns it with its digits in descending order.
    
    >>> sort_descending(1254859723)
    9875543221
    >>>>
    '''
    nums = str(num)
    nums = sorted(nums)
    nums = nums[::-1]
    nums = "".join(nums)
    return int(nums)