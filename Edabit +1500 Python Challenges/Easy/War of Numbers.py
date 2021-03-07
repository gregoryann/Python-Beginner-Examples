"""
War of Numbers
There's a great war between the even and odd numbers. Many numbers already lost their life in this war and it's your task to end this. You have to determine which group is larger: the even, or the odd. The larger group wins.

Create a function that takes a list of integers and sum up the even and odd numbers seperately and then substract the smaller one from the bigger one. Return the substraction.

Examples
war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 - 10

war_of_numbers([12, 90, 75]) ➞ 27

war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def war_of_numbers(lst):
	return abs(sum(n if n%2 else -n for n in lst))

"""
Solution 2
"""

def war_of_numbers(lst):
	s = sum(lst)
	even = sum([k for k in lst if k % 2 == 0])
	odd = s - even
	return max(even, odd) - min(even, odd)

"""
Solution 3
"""

def war_of_numbers(lst):
	evens=odds=0
	for i in lst:
		if i%2:
			odds+=i
		else:
			evens+=i
	return abs(evens-odds)

"""
Solution 4
"""

def war_of_numbers(lst):
	even=[l for l in lst if l%2==0]
	odd=[l for l in lst if l%2==1]
	if sum(even)>sum(odd):
		return sum(even)-sum(odd)
	return sum(odd)-sum(even)




