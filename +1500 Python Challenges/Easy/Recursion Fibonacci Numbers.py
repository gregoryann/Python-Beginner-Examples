"""
Recursion: Fibonacci Numbers
Fibonacci numbers are created in the following way:

F(0) = 0
F(1) = 1
...
F(n) = F(n-2) + F(n-1)
Write a function that calculates the nth Fibonacci number.

Examples
fib(0) ➞ 0

fib(1) ➞ 1

fib(2) ➞ 1

fib(8) ➞ 21
"""





################################################################
"""
Solution 1
"""


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n





################################################################
"""
Solution 2
"""

def fib(n):
	if n <= 1:
		return n
	return fib(n - 1) + fib(n - 2)







################################################################
"""
Solution 3
"""

fib=lambda n:n if n<2else fib(n-1)+fib(n-2)







#################################################################
"""
Solution 4
"""

def fib(n):
	if n==0: return 0
	if n==1: return 1
	return fib(n-1) + fib(n-2)




