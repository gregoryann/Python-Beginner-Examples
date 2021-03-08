"""
Binary to Decimal Converter

You are given one input: A list containing eight 1's and/or 0's. Write a function that takes an 8 bit binary number and convert it to decimal.

Examples
binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]) ➞ 255

binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]) ➞ 0

binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]) ➞ 188

Notes
Return an integer.
"""



################################################################
"""
Solution 1
"""


def binary_to_decimal(binary):
	return int(''.join(map(str, binary)), 2)



################################################################
"""
Solution 2
"""


def binary_to_decimal(binary):
	return sum(binary[7-i] * 2**i for i in range(7,-1,-1))



################################################################
"""
Solution 3
"""


def binary_to_decimal(binary):
	step = 0
	newlst = []
	for i in binary[::-1]:
		newlst.append(i*2**step)
		step+=1
	return sum(newlst)







