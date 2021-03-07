"""
Consecutive Numbers

Create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once.

Examples
cons([5, 1, 4, 3, 2]) ➞ True
// Can be re-arranged to form [1, 2, 3, 4, 5]

cons([5, 1, 4, 3, 2, 8]) ➞ False

cons([5, 6, 7, 8, 9, 9]) ➞ False
// 9 appears twice
"""



################################################################
"""
Solution 1
"""


def cons(lst):
	return list(range(min(lst), max(lst) + 1)) == sorted(lst)


################################################################
"""
Solution 2
"""


def cons(lst):
	
	s = lst

	new = []

	for i in range(len(s)):
			a = min(s)
			new.append(a)
			s.remove(a)

	if new[len(new) - 1] - new[0] == len(new) - 1:
			return True
	else:
			return False


################################################################
"""
Solution 3
"""


def cons(lst):
	temp = [min(lst)]
	for i in range(len(lst)-1):
		temp.append(temp[-1]+1)
		
	return temp == sorted(lst)



#################################################################
"""
Solution 4
"""


def cons(lst):
	lst = sorted(lst)
	j=0
	for i in range (lst[0],(lst[-1])+1):
		if not (lst[j]==i and lst.count(i)==1):
			 return False
		j+=1
	return True




