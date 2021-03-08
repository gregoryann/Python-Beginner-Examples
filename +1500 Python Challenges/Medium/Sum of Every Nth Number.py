"""
Sum of Every Nth Number

Given a list of numbers and a positive value for n, return the sum of every nth number in the list.

Examples
sum_every_nth([4, 8, 6, 6, 7, 9, 3], 1) ➞ 43
# 4+8+6+6+7+9+3 = 43

sum_every_nth([7, 3, 10, 4, 5, 8, 4, 9, 6, 9, 10, 1, 4], 4) ➞ 14
# 4+9+1 = 14

sum_every_nth([10, 6, 5, 4, 5, 2, 3, 3, 8, 10, 7, 2], 8) ➞ 3
# 3

sum_every_nth([6, 8, 9, 4, 6, 4, 7, 1, 5, 6, 10, 2], 13) ➞ 0
# only 12 numbers in list
"""



################################################################
"""
Solution 1
"""


def sum_every_nth(numbers, n):
	return sum(numbers[n-1::n])



################################################################
"""
Solution 2
"""


def sum_every_nth(numbers, n):
	i = 1;
	sum = 0;
	for x in numbers:
		if i == n:
			sum = sum + x
			i = 0
		i = i + 1
	return sum



################################################################
"""
Solution 3
"""


def sum_every_nth(numbers, n):
	l = len(numbers)
	index_list = []
	for i in range(l):
		k = i+1
		if k % n == 0:
			index_list.append(i)
	count = 0
	for location in index_list:
		count += int(numbers[location])
	return(count)



#################################################################
"""
Solution 4
"""


def sum_every_nth(numbers, n):
	numbers.insert(0,0)
	return sum(numbers[::n])



