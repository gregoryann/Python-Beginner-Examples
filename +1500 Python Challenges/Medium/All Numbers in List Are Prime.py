"""
All Numbers in List Are Prime
Create a function thats takes a list and returns True if every number is prime. Otherwise, return False.

Examples
all_prime([7, 5, 2, 4, 6]) ➞ False

all_prime([2, 3, 5, 7, 13, 17, 19, 23, 29]) ➞ True

all_prime([1, 5, 3]) ➞ False

Notes
1 is not a prime number.
"""




################################################################
"""
Solution 1
"""


def all_prime(lst):
	return all(is_prime(i) for i in lst)
	
def is_prime(n):
	return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))



################################################################
"""
Solution 2
"""


def is_prime(x):
	return all(x % i for i in range(2, x)) and x >= 2


def all_prime(lst):
	return all(map(is_prime, lst))




################################################################
"""
Solution 3
"""


def all_prime(lst):
	lst1=[]
	for i in lst:
		for j in range(2,i+2):
			if i%j==0:
				lst1.append(i)
	return len(lst)==len(lst1)



#################################################################
"""
Solution 4
"""


def is_prime(num):
	if num==1:
		return False
	i=2
	while i*i<=num:
		if num%i==0:
			return False
		i+=1
	return True

def all_prime(lst):
	return all(is_prime(i) for i in lst)




