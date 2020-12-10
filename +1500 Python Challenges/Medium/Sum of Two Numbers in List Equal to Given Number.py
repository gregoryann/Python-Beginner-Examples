"""
Sum of Two Numbers in List Equal to Given Number

Create a function that takes a list of numbers lst and a number n. Return True if the sum of any two elements is equal to the given number. Otherwise, return False.

Examples
check_sum([10, 12, 4, 7, 9, 11], 16) ➞ True

check_sum([4, 5, 6, 7, 8, 9], 13) ➞ True

check_sum([0, 98, 76, 23], 174) ➞ True

check_sum([0, 9, 7, 23, 19, 18, 17, 66], 39) ➞ False

check_sum([2, 8, 9, 12, 45, 78], 1) ➞ False
"""



################################################################
"""
Solution 1
"""


def check_sum(lst, n):
	return any(n - i in lst for i in lst)



################################################################
"""
Solution 2
"""


import itertools
def check_sum(lst, n):
	return any(sum(num) == n for num in itertools.combinations(lst, 2))



################################################################
"""
Solution 3
"""


def check_sum(lst, n):
	for i in range(len(lst)):
		for j in range(i+1, len(lst)):
			if lst[i]+lst[j] == n:
				return True
	return False


#################################################################
"""
Solution 4
"""


import itertools
from itertools import combinations

def check_sum(lst, n):

	Duets = list(combinations(lst,2))
	
	Counter = 0
	Length = len(Duets)
	
	while (Counter < Length):
		
		Pair = Duets[Counter]
		Total = sum(Pair)
		
		if (Total == n):
			return True
		else:
			Counter += 1
	
	return False



