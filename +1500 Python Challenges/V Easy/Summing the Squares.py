"""
Summing the Squares
Create a function where given the number n, return the sum of all square numbers up to and including n.

squares_sum(3) ➞ 14
# 1² + 2² + 3² =
# 1 + 4 + 9 =
# 14
Examples
squares_sum(3) ➞ 14

squares_sum(12) ➞ 650

squares_sum(13) ➞ 819
Notes
Remember that n is included in the total.

"""



"""
Solution 1
"""

def squares_sum(n):
	return sum(i*i for i in range(1, n+1))

"""
Solution 2
"""

def squares_sum(n):
	a=0
	for i in range(1,n+1):
		a+=i**2
	return a


"""
Solution 3
"""

squares_sum=lambda n: sum(i*i for i in range(n+1))

"""
Solution 4
"""

squares_sum = lambda n: n ** 2 + squares_sum(n - 1) if n > 0 else False





