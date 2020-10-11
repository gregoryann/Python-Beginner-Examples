"""
FizzBuzz Interview Question

Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Examples
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"

Notes
Try to be precise with how you spell things and where you put the capital letters.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""





################################################################
"""
Solution 1
"""

def fizz_buzz(num):
	return "Fizz"*(num%3==0) + "Buzz"*(num%5==0) or str(num)





################################################################
"""
Solution 2
"""

def fizz_buzz(num):
	s = ''
	if num%3 == 0: s += 'Fizz'
	if num%5 == 0: s += 'Buzz'
	return s if s else str(num)






################################################################
"""
Solution 3
"""


def fizz_buzz(num):
	if num % 3 < 1 and num % 5 < 1: return "FizzBuzz"
	if num % 3 < 1: return "Fizz"
	if num % 5 < 1: return "Buzz"
	return str(num)






#################################################################
"""
Solution 4
"""

fizz_buzz = lambda n: "Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or str(n)




