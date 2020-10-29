"""
Count a Specific Digit

Write a function that counts the number of times a specific digit occurs in a range (inclusive). The function will look like:

digit_occurrences(start, end, digit) ➞ number of times digit occurs
Examples
digit_occurrences(51, 55, 5) ➞ 6
# [51, 52, 53, 54, 55] : 5 occurs 6 times

digit_occurrences(1, 8, 9) ➞ 0

digit_occurrences(-8, -1, 8) ➞ 1

digit_occurrences(71, 77, 2) ➞ 1

Notes
Ranges can be negative.
start <= end
"""



################################################################
"""
Solution 1
"""


def digit_occurrences(start, end, digit):
  return ''.join(str(i) for i in range(start,end+1)).count(str(digit))



################################################################
"""
Solution 2
"""


def digit_occurrences(start, end, digit):
	val = ''.join(str(i) for i in range(start,end+1))
	return val.count(str(digit))




################################################################
"""
Solution 3
"""


def digit_occurrences(start, end, digit):
	count = 0
	for i in range(start,end+1):
		count += str(i).count(str(digit))
	return count



#################################################################
"""
Solution 4
"""


from typing import List


def digit_occurrences(start: int, end: int, digit: int) -> int:
	lst = [
		str(c) for c in list(range(start, end + 1))
	]  # type: List[str]
	result = 0
	digit = str(digit)
	for c in lst:
		result += c.count(digit)
	return result




