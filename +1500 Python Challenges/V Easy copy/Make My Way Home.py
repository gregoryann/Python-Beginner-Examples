"""

Make My Way Home
You will be given a list, showing how far James travels away from his home for each day. He may choose to travel towards or away from his house, so negative values are to be expected.

Create a function which calculates how far James must walk to get back home.

Examples
distance_home([2, 4, 2, 5]) ➞ 13

distance_home([-1, -4, -3, -2]) ➞ 10

distance_home([3, 4, -5, -2]) ➞ 0
Notes
Assume James only travels in a straight line.
Distance is always a positive number.


"""






"""
Solution 1
"""


def distance_home(lst):
	return abs(sum(lst))




"""
Solution 2
"""

def distance_home(lst):
	ans=0
	for i in lst:
		ans+=i
	ans=abs(ans)
	return ans



"""
Solution 3
"""

def distance_home(lst):
	distance = sum(lst)
	if distance < 0:
		distance = distance * (-1)
	return distance



"""
Solution 4
"""


def distance_home(lst):
 return abs(sum(i for i in lst))




distance_home= lambda l: abs(sum(l))




def distance_home(lst):
	dist = 0
	for i in lst:
		dist += i
	return(abs(dist))

