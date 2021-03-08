"""
Any Prime Number in Range

Create a function that returns True if there's at least one prime number in the given range (n1 to n2 (inclusive)), False otherwise.

Examples
prime_in_range(10, 15) ➞ True
# Prime numbers in range: 11, 13

prime_in_range(62, 66) ➞ False
# No prime numbers in range.

prime_in_range(3, 5) ➞ True
# Prime numbers in range: 3, 5


Notes
n2 is always greater than n1.
n1 and n2 are always positive.
0 and 1 aren't prime numbers.
"""



################################################################
"""
Solution 1
"""


def prime_in_range(n1, n2):
	return any(isPrime(n) for n in range(n1, n2+1))
	
def isPrime(N):
	return not any(not N%n for n in range(2, int(N**0.5)+1))



################################################################
"""
Solution 2
"""


def prime_in_range(n1, n2):
  a = []
  for i in range(n1, n2+1):
      for j in range(2, i):
          if i%j==0:
              break
      else: a.append(i)
  return len(a)!=0



################################################################
"""
Solution 3
"""


def prime_in_range(n1, n2):
	is_prime = lambda n: all(n%i for i in range(2, n-1))
	return any(is_prime(n) for n in range(n1, n2+1))


#################################################################
"""
Solution 4
"""


def prime_in_range(n1, n2):
	return any(is_prime(k) for k in range(n1,n2+1))

is_prime = lambda n: n>1 and all(n%i for i in range(2, 1+int(n**.5)))



