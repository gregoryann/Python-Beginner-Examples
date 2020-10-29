"""
Perfect Number

Create a function that tests whether or not an integer is a perfect number. A perfect number is a number that can be written as the sum of its factors, excluding the number itself.

For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6. Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.

Examples
check_perfect(6) ➞ True

check_perfect(28) ➞ True

check_perfect(496) ➞ True

check_perfect(12) ➞ False

check_perfect(97) ➞ False
"""



################################################################
"""
Solution 1
"""


def check_perfect(num):
	factors = []
	for i in range(1,num):
		if num % i == 0:
			factors.append(i)
	return sum(factors) == num



################################################################
"""
Solution 2
"""


def check_perfect(num):

    factors = set()

    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:
            factors.add(i)
            factors.add(num / i)

    return (sum(factors) - num) == num




################################################################
"""
Solution 3
"""


def check_perfect(num):
	aux = [1]	
	for i in range(2, num // 2 + 1):
		if num % i == 0: aux.append(i)
	return True if sum(aux) == num else False







