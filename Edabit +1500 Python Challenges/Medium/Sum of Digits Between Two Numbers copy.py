"""
Sum of Digits Between Two Numbers

Create a function that sums the total number of digits between two numbers, inclusive. For example, between the numbers 19 and 22 we have:

# 19, 20, 21, 22
(1 + 9) + (2 + 0) + (2 + 1) + (2 + 2) = 19
Examples
sum_digits(7, 8) ➞ 15

sum_digits(17, 20) ➞ 29

sum_digits(10, 12) ➞ 6
"""





################################################################
"""
Solution 1
"""


def sum_digits(a, b):
	return sum(sum(map(int, str(i))) for i in range(a, b + 1))


################################################################
"""
Solution 2
"""


def sum_digits(a, b):
	digits = ''.join(str(i) for i in range(a, b + 1))
	return sum(int(i) for i in digits)



################################################################
"""
Solution 3
"""


def sum_digits(a, b):
    out = []
    for i in range(a,b + 1):
        i = str(i)
        for x in i:
            out.append(int(x))
    return sum(out)



#################################################################
"""
Solution 4
"""


def sum_digits(a, b):
 return sum(sum([int(j) for j in str(i)]) for i in range(a,b+1))



