"""
Length of Number

Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1

Notes
DO NOT USE LEN() FOR THIS CHALLENGE
"""



################################################################
"""
Solution 1
"""


def number_length(num):
  return sum(1 for i in str(num))



################################################################
"""
Solution 2
"""

def number_length(num):
    res, n = 1, num // 10
    while n:
        n //= 10
        res += 1
    return res


################################################################
"""
Solution 3
"""


number_length=lambda n,l=1:number_length(n//10,l+1)if n>9else l



#################################################################
"""
Solution 4
"""


def number_length(num):
	b = str(num)
	return b.count('1') + b.count('2') + b.count('0') + b .count('3') + b.count('4') + b.count('5') + b.count('6') + b.count('7') + b.count('8') + b.count('9')




