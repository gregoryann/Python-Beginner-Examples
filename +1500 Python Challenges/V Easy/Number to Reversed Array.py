"""
Number to Reversed Array
Create a function that takes a number and returns a list with the digits of the number in reverse order.

Examples:

reverse_list(1485979) ➞ [9, 7, 9, 5, 8, 4, 1]
reverse_list(623478) ➞ [8, 7, 4, 3, 2, 6]
reverse_list(12345) ➞ [5, 4, 3, 2, 1]
"""


"""
Solution 1
"""

def reverse_list(num):
	return [int(i) for i in str(num)[::-1]]

"""
Solution 2
"""
def reverse_list(num):
	lst = []
	while num>0:
		lst.append(num % 10)
		num = num//10
	return lst

"""
Solution 3
"""

def reverse_list(num):
	s= str(num)
	s1=s[::-1]
	l=[]
	for ch in s1:
		l.append(int(ch))
	return l

"""
Solution 4
"""
def reverse_list(num):
	b=str(num)
	a=len(b)
	newLst=[]
	for i in range(a-1,-1,-1):
		newLst.append(int(b[i]))
	return newLst





