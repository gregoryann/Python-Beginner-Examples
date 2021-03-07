"""
Sum of the Odd Numbers
Create a function which returns the total of all odd numbers up to and including n. n will be given as an odd number.

Examples
add_odd_to_n(5) ➞ 9
# 1 + 3 + 5 = 9

add_odd_to_n(13) ➞ 49

add_odd_to_n(47) ➞ 576
Notes
Curiously, the answers are all square numbers!

"""



"""
Solution 1
"""

def add_odd_to_n(n):
	return ((n+1)//2)**2

"""
Solution 2
"""

add_odd_to_n=lambda	n:sum(i for i in range(1,n+1,2))

add_odd_to_n = lambda n : sum(i for i in range(1,n + 1) if i % 2 != 0)

"""
Solution 3
"""

def add_odd_to_n(n):
       odd_sum = 0
       for num in range(1, n+1, 2):
            odd_sum += num
       return odd_sum

"""
Solution 4
"""

def add_odd_to_n(n):
	sum = 0
	for x in range(n+1):
		if(x % 2 != 0):
			sum = sum + x
	return sum




