"""
Scalable Mountain?

Given a list of numbers, representing the height of a mountain in certain intervals, return whether this mountain is scalable.

A mountain can be considered scalable if each number is within 5 units of the next number in either direction.

Examples
is_scalable([1, 2, 4, 6, 7, 8]) ➞ True

is_scalable([40, 45, 50, 45, 47, 52]) ➞ True

is_scalable([2, 9, 11, 10, 18, 21]) ➞ False


Notes
The list may start at any number and can be any length.
"""


################################################################
"""
Solution 1
"""


def is_scalable(lst):
	return all(abs(a-b) <= 5 for a, b in zip(lst, lst[1:]))




################################################################
"""
Solution 2
"""


def is_scalable(lst):
	try:
		for idx, i in enumerate(lst):
			if i not in range(lst[idx + 1] - 6, lst[idx + 1] + 6):
				return False
	except IndexError:
		return True



################################################################
"""
Solution 3
"""


def is_scalable(lst):
	count = 0
	for i in range(len(lst)-1):
		if lst[i+1]- lst[i]<=5:
			count +=1
	return (count == len(lst)-1)




#################################################################
"""
Solution 4
"""


def is_scalable(lst):
	
	Length = len(lst)
	
	if (Length < 2):
		return True
	
	Value_1A = lst[0]
	Value_1B = lst[1]
	Scale_01 = abs(Value_1B - Value_1A)
	
	if (Scale_01 > 5):
		return False
	
	Value_2A = lst[-1]
	Value_2B = lst[-2]
	Scale_02 = abs(Value_2B - Value_2A)
	
	if (Scale_02 > 5):
		return False
	
	Previous = 0
	Current = 1
	Next = 2
	Length = len(lst)
	
	while (Next < Length):
		
		Value_3A = lst[Previous]
		Value_3B = lst[Current]
		Value_3C = lst[Next]
		
		Scale_03A = abs(Value_3B - Value_3A)
		Scale_03B = abs(Value_3B - Value_3C)
		
		if (Scale_03A > 5) or (Scale_03B > 5):
			return False
		else:
			Previous += 1
			Current += 1
			Next += 1
	
	return True



