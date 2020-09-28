"""
Even All the Way

Given a list of numbers, return a list which contains all the even numbers in the orginal list, which also have even indices.

Examples
get_only_evens([1, 3, 2, 6, 4, 8]) ➞ [2, 4]

get_only_evens([0, 1, 2, 3, 4]) ➞ [0, 2, 4]

get_only_evens([1, 2, 3, 4, 5]) ➞ []

Notes
Lists start at index 0.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def get_only_evens(nums):
	return [i for i in nums[::2] if not i%2]

"""
Solution 2
"""

def get_only_evens(nums):
	l = []
	for n in range(0, len(nums)):
		if n % 2 == 0 and nums[n] % 2 == 0:
			l.append(nums[n])
	return l

"""
Solution 3
"""

get_only_evens=lambda n:[x for i,x in enumerate(n)if x%2<1>i%2]

"""
Solution 4
"""

def get_only_evens(nums):
 new_list=[]
 for i in range(len(nums)):
     if(i%2 == 0 and nums[i]%2==0):
         new_list.append(nums[i])
 return new_list




