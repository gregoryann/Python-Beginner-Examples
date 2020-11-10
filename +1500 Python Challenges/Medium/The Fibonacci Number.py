"""
The Fibonacci Number

Create a function that, given a number, returns the corresponding value of that index in the Fibonacci series.

Examples
fibonacci(3) ➞ 3

fibonacci(7) ➞ 21

fibonacci(12) ➞ 233

Notes
The first number in the sequence starts at 1 (not 0).
"""




################################################################
"""
Solution 1
"""

fibonacci = lambda num : fibonacci(num-1)+fibonacci(num-2) if num > 1 else 1


################################################################
"""
Solution 2
"""


def fibonacci(num):
	fib = [1, 1]
	for i in range(100):
		fib.append(fib[i]+fib[i+1])
	return fib[num]




################################################################
"""
Solution 3
"""


def fibonacci(n):
	seq = [1,1]
	while len(seq) <= n:
		seq.append(seq[-1] + seq[-2])
		
	return seq[-1]



#################################################################
"""
Solution 4
"""


def fibonacci(num):
  f=[1,1]
  if num<2: return 1
  for i in range(2,num+1):
    f.append(sum(f[-2:]))
  return f[-1]



