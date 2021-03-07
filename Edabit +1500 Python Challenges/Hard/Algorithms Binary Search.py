"""
Algorithms: Binary Search

Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

Examples
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


is_prime(primes, 3) ➞ "yes"

is_prime(primes, 4) ➞ "no"

is_prime(primes, 67) ➞ "yes"

is_prime(primes, 36) ➞ "no"


Notes
You could use built-in functions to solve this, but the point of this challenge is to see if you understand the binary search algorithm.
The solution is in the Resources tab.
"""


################################################################
"""
Solution 1
"""


def is_prime(primes, num, left=0, right=None):
 primes1 = primes
 while 1:
    print(primes1)
    if len(primes1) == 1:
        break
    if num < primes1[round(len(primes1) / 2)-1]:
        primes1 = primes1[:round(len(primes1) / 2)]
    elif num > primes1[round(len(primes1) / 2)-1]:
        primes1 = primes1[round(len(primes1) / 2):len(primes1)]
    elif num == primes1[round(len(primes1) / 2)-1]:
        return 'yes'

 if num == primes1:
    return 'yes'
 else:
    return 'no'

A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(is_prime(A, 11))










################################################################
"""
Solution 2
"""


def is_prime (primes, x):
	def binarySearch(arr, l, r, x):
		if r >= l: 
			mid = l + (r - l) // 2
			if arr[mid] == x: 
				return True
			elif arr[mid] > x: 
				return binarySearch(arr, l, mid-1, x) 
			else: 
				return binarySearch(arr, mid + 1, r, x) 
		else: 
			return False
	return "yes" if binarySearch(primes, 0, len(primes), x) else "no"






################################################################
"""
Solution 3
"""



def prime(num):
	if num == 2: return True
	if num in (0,1) or not num % 2: return True
	for n in range(2, num):
		if num % n == 0:
			return False
	return True

def is_prime(primes, num):
	primeiro = 0
	ultimo = len(primes) - 1
	while primeiro <= ultimo:
		metade = (ultimo + primeiro) // 2
		if primes[metade] < num:
			primeiro = metade + 1
		elif primes[metade] > num:
			ultimo = metade - 1
		else:
			return 'yes' if prime(num) else 'no'
	return 'no'





