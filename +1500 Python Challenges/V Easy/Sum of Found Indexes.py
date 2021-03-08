"""
Sum of Found Indexes
Create a function which takes in a list of numbers and a number to find. Return the sum of every index in the list which matches the chosen number.

Examples
sum_found_indexes([0, 3, 3, 0, 0, 3], 3) ➞ 8
# The number 3 was found at indexes 1, 2 and 5.
# 8 = 1 + 2 + 5

sum_found_indexes([1, 2, 3, 4, 5, 6], 3) ➞ 2

sum_found_indexes([100, 100, 100, 100, 100], 100) ➞ 10

sum_found_indexes([5, 10, 15, 20], 2) ➞ 0


Notes
0 can be the result if no number in the list matches or if the only matching element is at index 0.

"""


"""
Solution 1
"""

def sum_found_indexes(lst, n):
	return sum([i for i,el in enumerate(lst) if el == n])

"""
Solution 2
"""

def sum_found_indexes(lst, n):
	count=0
	nl=[]
	for i in lst:
		if i==n:
			nl.append(count)
		count+=1
	return sum(nl)

"""
Solution 3
"""

def sum_found_indexes(lst, n):
	i = 0
	j = 0
	for i in range(len(lst)):
		if lst[ i ] == n:
			j = j + i
		else:
			i = i+1
	return j

"""
Solution 4
"""

def sum_found_indexes(lst, n):
	index_lst = []
	for i in range(len(lst)):
		if lst[i] == n:
			index_lst.append(i)
	return sum(index_lst)




