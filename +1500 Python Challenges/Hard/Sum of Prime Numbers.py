"""
Sum of Prime Numbers
Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17

sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87

sum_primes([]) ➞ None

Notes
Given numbers won't exceed 101.
A prime number is a number which has exactly two divisors.
"""




################################################################
"""
Solution 1
"""


def sum_primes(l):
	p = lambda x: 2 in [x, 2**x%x]
	return sum(filter(p, l)) if l else None




################################################################
"""
Solution 2
"""


sum_primes=lambda l:sum(filter(lambda p:p>1and all(p%i for i in range(2,int(p**0.5+1))),l))or None


################################################################
"""
Solution 3
"""


def sum_primes(lst):
	isprime = lambda n: n>1 and all(n % i for i in range(2, int(n**0.5)+1))
	return sum(n for n in lst if isprime(n)) or None



################################################################
"""
Solution 4
"""


def sum_primes(lst):
	i= [2,3,5,7]
	retorn = []
	for x in lst:
		if x!=1:
			retorn.append(x)
		for c in i:
			if x % c == 0 and x != c:
				retorn.pop(-1)
				break
	return sum(retorn) if len(lst) > 0 else None




################################################################
"""
Solution 5
"""


def sum_primes(lst):
    return sum(list(filter(lambda x: (x > 1 and all(x % y != 0 for y in range(2, x))), lst))) if len(lst) > 0 else None