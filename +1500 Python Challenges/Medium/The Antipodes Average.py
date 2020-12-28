"""
The Antipodes Average

In this challenge, you are given a list and in turn, you must obtain a smaller list, following three steps:

Split the list into two parts of equal length. If the given list has an odd length, then you have to eliminate the number in the middle of the list for obtaining two equal parts.
Sum each number of the first part with each number of the reversed second part, obtaining a new single list having the same length of the previous two.
Divide by two each number in the final list.
Given a list of integers lst, implement a function that returns a new list applying the above algorithm.

Examples
antipodes_average([1, 2, 3, 4]) ➞ [2.5, 2.5]
# Left part = [1, 2]
# Reversed right part = [4, 3]
# List resulting from the sum of each pair = [5, 5]
# Each number is divided by two = [2.5, 2.5]

antipodes_average([1, 2, 3, 4, 5]) ➞ [3, 3]
# The length of list is odd, number 3 (in the middle) is eliminated
# Left = [1, 2]
# Reversed right = [5, 4]
# Sum = [6, 6]
# Division by two = [3, 3]

antipodes_average([-1, -2]) ➞ [-1.5]
#  (-1 + -2) / 2 = [-1.5]


Notes
Every given lst will contain at least two numbers.
Into the given lst, numbers will always be whole (either positives or negatives), but the numbers into the returned final list can also be a float (either positives or negatives, see the examples #1 and #3).
You can do three separated steps, or thinking about how the algorithm can be synthesized for obtaining the result.
"""




################################################################
"""
Solution 1
"""


def antipodes_average(lst):
	left = lst[:len(lst)//2]
	right = lst[len(lst)//2:]
	right.reverse()
	i = 0
	final = []
	while i < len(left):
		final.append((left[i] + right[i])/2)
		i += 1
	return final



################################################################
"""
Solution 2
"""


def antipodes_average(lst):
	if len(lst) % 2 != 0:
		lst.pop(len(lst)//2)
	res = []
	for i in range(len(lst)//2):
		res.append((lst[i] + lst[-i-1]) / 2)
	return res




################################################################
"""
Solution 3
"""


def antipodes_average(lst):
	quant = len(lst)
	lst1 = []
	lst2 = []
	lst3 = []
	for i in range(0, quant//2):
		lst1.append(lst[i])
		lst2.append(lst[-1-i])
		lst3.append((lst1[i] + lst2[i])/2)
		
	return lst3



#################################################################
"""
Solution 4
"""


def antipodes_average(lst):
    sep = int(len(lst)/2 - 1)
    if len(lst)%2==0 :
        return [(i+j)/2 for i, j in zip(list(lst[0:sep+1]), list(lst[sep+1:])[::-1])]
    num = int(len(lst)/2)
    lst.remove(lst[num])
    return antipodes_average(lst)



