"""
Return Duplicate Numbers

Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list.

Examples
duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]

duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]

duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None


Notes
The given list won't contain the same number three times.

If there are no duplicate numbers, return None.
"""



################################################################
"""
Solution 1
"""


def duplicate_nums(nums):
	return sorted([n for i,n in enumerate(nums) if n in nums[i+1:]]) or None



################################################################
"""
Solution 2
"""


def duplicate_nums(nums):
	so = len(nums)
	repeated = []
	for i in range(so):
		k = i+1
		for j in range(k, so):
			if nums[i] == nums[j] and nums[i] not in repeated:
				repeated.append(nums[i])
	return sorted(repeated) if len(repeated)>0 else None



################################################################
"""
Solution 3
"""


def duplicate_nums(nums):
 arr = []
 nums.sort()
 for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      arr.append(nums[i])
 return None if len(arr) == 0 else arr


#################################################################
"""
Solution 4
"""


def duplicate_nums(nums):
	lst = []
	lst2 = []
	
	for i in nums:
		if i not in lst:
			lst.append(i)
		else:
			lst2.append(i)
			
	return sorted(lst2) or None



