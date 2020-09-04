"""
ReverseAndNot
Write a function that takes an integer i and returns an integer with the integer backwards followed by the original integer.

To illustrate:

123
We reverse 123 to get 321 and then add 123 to the end, resulting in 321123.

Examples
reverse_and_not(123) ➞ 321123

reverse_and_not(152) ➞ 251152

reverse_and_not(123456789) ➞ 987654321123456789
Notes
i is a non-negative integer.

"""



"""
Solution 1
"""

def reverse_and_not(i):
	return int(str(i)[::-1] + str(i))

"""
Solution 2
"""

reverse_and_not = lambda i:int(str(i)[::-1]+str(i))

"""
Solution 3
"""

def reverse_and_not(i):
	x = str(i)
	return int(x[::-1] + x)


"""
Solution 4
"""

def reverse_and_not(i):
	s=str(i)
	return int(s[::-1]+s)

"""
Solution 5
"""

def reverse_and_not(i):
	res = str(i)[0:]
	res1 = str(i)[::-1]
	return int(res1+res)



