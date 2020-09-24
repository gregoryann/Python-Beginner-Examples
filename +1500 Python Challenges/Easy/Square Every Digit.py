"""
Square Every Digit
Create a function that squares every digit of a number.

Examples
square_digits(9119) ➞ 811181

square_digits(2483) ➞ 416649

square_digits(3212) ➞ 9414

Notes
The function receives an integer and must return an integer.
"""


"""
Solution 1
"""

def square_digits(n):
	return int("".join(str(int(i)**2) for i in str(n)))

"""
Solution 2
"""

def square_digits(n):
    ans = ''
    for x in str(n):
        ans += str(int(x)**2)
    return int(ans)

"""
Solution 3
"""

def square_digits(n):
  squared = [int(i)**2 for i in str(n)]
  result = [str(i) for i in squared]
  result = ''.join(result)
  return int(result)

"""
Solution 4
"""

def square_digits(n):
	num = []
	while n > 0:
		num.append((n%10)**2)
		n = n // 10
	num = num[::-1]
	return int(''.join(map(str, num)))




