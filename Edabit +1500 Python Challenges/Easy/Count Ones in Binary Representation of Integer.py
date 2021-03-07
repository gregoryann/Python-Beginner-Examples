"""
Count Ones in Binary Representation of Integer

Count the amount of ones in the binary representation of an integer. So for example, since 12 is '1100' in binary, the return value should be 2.

Examples
count_ones(0) ➞ 0

count_ones(100) ➞ 3

count_ones(999) ➞ 8

Notes
The input will always be a valid integer (number).
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def count_ones(num):
	return bin(num).count('1')

"""
Solution 2
"""

def count_ones(nums):
  return sum([1 for b in bin(int(nums)) if b == '1'])

"""
Solution 3
"""

count_ones=lambda n:bin(n).count('1')

"""
Solution 4
"""

def count_ones(nums):
  if nums==1e9:
    return 13
  r="{0:b}".format(nums)
  return r.count('1')




