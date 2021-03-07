"""
Pandigital Numbers

A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.

Examples
is_pandigital(98140723568910) ➞ True

is_pandigital(90864523148909) ➞ False
# 7 is missing.

is_pandigital(112233445566778899) ➞ False

Notes
Think about the properties of a pandigital number when all duplicates are removed.
"""



################################################################
"""
Solution 1
"""


def is_pandigital(n):
  return set(str(n))==set('0123456789')



################################################################
"""
Solution 2
"""


def is_pandigital(n):
	lst = []
	
	for i in str(n):
		if not i in lst:
			lst.append(i)
	
	if len(lst) == 10:
		return True
		
	return False




################################################################
"""
Solution 3
"""


def is_pandigital(n):
	final = set()
	for i in str(n):
		final.add(i)
		
	if len(final) == 10:
		return True
	return False



#################################################################
"""
Solution 4
"""



def is_pandigital(n):
	nums = [0,1,2,3,4,5,6,7,8,9]
	n_nums = []
	
	for i in str(n):
		if i not in n_nums:
			n_nums.append(i)
		if len(n_nums) == len(nums):
			return 1
	return 0




#################################################################
"""
Solution 5
"""


def is_pandigital(n):
	strn = str(n)
	spltn = strn.split()
	setspltn = set(strn)
	srtn = sorted(setspltn)
	newn = ''.join(srtn)
	if newn == '0123456789':
		return True
	else:
		return False