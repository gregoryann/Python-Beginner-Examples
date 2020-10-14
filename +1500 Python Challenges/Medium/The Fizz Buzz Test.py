"""
The Fizz Buzz Test

Write a program that returns a list of all the numbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.

Example
fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

Notes
Make sure to return a list.
"""



################################################################
"""
Solution 1
"""


def fizz_buzz(n):
	return [('Fizz'*(not i%3) + 'Buzz'*(not i%5)) or i for i in range(1, n+1)]




################################################################
"""
Solution 2
"""


fizz_buzz=lambda n:[('Fizz'*(i%3<1)+'Buzz'*(i%5<1))or i for i in range(1,n+1)]





################################################################
"""
Solution 3
"""


def fizz_buzz(maximum):
	lst = list(range(1,maximum+1))
	for n, i in enumerate(lst):
		if i%3 == 0:
			lst[n] = 'Fizz'
		if i%5 == 0:
			lst[n] = 'Buzz'
		if i%15 == 0:
			lst[n] = 'FizzBuzz'
	return lst




#################################################################
"""
Solution 4
"""


def fizz_buzz(maximum):
	lst = []
	for num in range(1, maximum + 1):
		if num % 3 == 0 and num % 5 == 0:
			lst.append('FizzBuzz')
		elif num % 3 == 0:
			lst.append('Fizz')
		elif num % 5 == 0:
			lst.append('Buzz')
		else:
			lst.append(num)
	return lst




