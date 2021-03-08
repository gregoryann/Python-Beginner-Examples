"""
Remove Surrounding Duplicate Items

Create a function that takes a sequence of either strings or integers, removes the surrounding duplicates and returns a list of items without any items with the same value next to each other and preserves the original order of items.

Examples
unique_in_order("AAAABBBCCDAABBB") ➞ ["A", "B", "C", "D", "A", "B"]

unique_in_order("ABBCcAD") ➞ ["A", "B", "C", "c", "A", "D"]

unique_in_order([1, 2, 2, 3, 3]) ➞ [1, 2, 3]

Notes
The initial sequence of items can be either a string or a list.
Tests are case sensitive.
"""



################################################################
"""
Solution 1
"""


def unique_in_order(sequence):
	a=[sequence[0]]
	for i in sequence:
		if a[-1]!=i:
			a.append(i)
	return a







################################################################
"""
Solution 2
"""


from itertools import*
unique_in_order=lambda s:list(k for k,_ in groupby(s))






################################################################
"""
Solution 3
"""


def unique_in_order(sequence):
	sq = list(sequence)
	while True:
		for index in range(len(sq)):
			if index != 0 and sq[index] == sq[index-1] or index != len(sq)-1 and sq[index] == sq[index+1]:
				sq.pop(index)
				break
		else:
			return sq







#################################################################
"""
Solution 4
"""

def unique_in_order(sequence):
	return [v for i, v in list(enumerate(sequence)) if
            i==0 or sequence[i-1] != sequence[i]]




