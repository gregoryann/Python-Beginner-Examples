"""
Add a Consecutive List of Numbers
Write a function that takes the last number of a consecutive list of numbers and returns the total of all numbers up to and including it.

Examples
add_up_to(3) ➞ 6
# 1 + 2 + 3 = 6

add_up_to(10) ➞ 55
# 1 + 2 + 3 + ... + 10 = 55

add_up_to(7) ➞ 28
# 1 + 2 + 3 + ... + 7 = 28
Notes
You will only be given valid inputs.
There are two ways of doing this; try finding them both!
Remember to return the result.
"""



"""
Solution 1
"""

def add_up_to(n):
	return sum(range(1, n + 1))
	# or: return n * (n + 1) // 2
	# or: return n if n == 0 else n + addUpTo(n - 1)

"""
Solution 2
"""

def add_up_to(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum


"""
Solution 3
"""

def add_up_to(n):
	c=1
	lst=[]
	while c<=n:
		lst.append(c)
		c=c+1
	return sum(lst)

"""
Solution 4
"""

def add_up_to(n):
	total=0
	i=1
	while i <= n:
		total+=i
		i+=1
	return total




