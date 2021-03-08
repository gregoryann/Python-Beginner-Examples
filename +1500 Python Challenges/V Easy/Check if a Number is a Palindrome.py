"""

Check if a Number is a Palindrome

Write a function that returns True if a number is a palindrome.

Examples
is_palindrome(838) ➞ True

is_palindrome(4433) ➞ False

is_palindrome(443344) ➞ True

Notes
A palindrome is a number that remains the same when reversed.
Bonus: Try solving this without turning the number into a string.

"""


"""
Solution 1
"""

def is_palindrome(n):
	return str(n) == str(n)[::-1]

"""
Solution 2
"""

# with Bonus (no string conversion)
def is_palindrome(n):
	digits = []
	while n:
		n, r = divmod(n, 10)
		digits.append(r)
	return digits == digits[::-1]

"""
Solution 3
"""

def is_palindrome(n):
	reverse = 0
	original = n
	while n > 0:
		end_digit = n % 10
		reverse = reverse*10 + end_digit
		n = n // 10
	return reverse == original

"""
Solution 4
"""

def is_palindrome(n):
    # return str(n) == str(n)[::-1]

    number, digits = n, []
    
    while number:
        digits.append(number % 10)
        number //= 10

    pot, number = len(digits) - 1, 0

    for i, digit in zip(range(pot, -1, -1), digits):
        number += digit * (10 ** i)

    return n == number





