"""
Fibonacci !Recursion

The Fibonacci sequence is a classic use case for recursive functions since the value of the sequence at a given index is dependent on the sum of the last two values. However, the recursion tree created by solving the Fibonacci sequence recursively can grow quite fast. Therefore it can be important to think about the implications of running a function recursively. Depending on the size of n needed and the capabilities of the system in question you might want to take a different approach.

Write a non-recursive function that takes an integer n and returns the Fibonacci sequence's value at index n.

Examples
fib(6) ➞ 8
# 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

fib(1) ➞ 1

fib(2) ➞ 1

Notes
Inputs will be whole numbers >= 0
"""




################################################################
"""
Solution 1
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a




################################################################
"""
Solution 2
"""

def fib(n):
    a, b = 0, 1; seq = [a, b]
    while len(seq) <= n:
        a, b = b, a+b
        seq.append(b)
    return seq[-1] if n > 1 else seq[n]




################################################################
"""
Solution 3
"""

def fib(n):
	arr = [0,1]
	for i in range(n):
		arr.append(arr[-1] + arr[-2])
	return arr[n]




################################################################
"""
Solution 4
"""

from math import floor

#Moivre-Binet
def fib(n):
	return floor(1/5**.5*(((1+5**.5)/2)**n - ((1-5**.5)/2)**n))



