"""
Digit Distance

The digit distance between two numbers is the total value of the difference between each pair of digits.

To illustrate:

digit_distance(234, 489) ➞ 12
# Since |2 - 4| + |3 - 8| + |4 - 9| = 2 + 5 + 5
Create a function that returns the digit distance between two integers.

Examples
digit_distance(121, 599) ➞ 19

digit_distance(12, 12) ➞ 0

digit_distance(10, 20) ➞ 1

Notes
Both integers will be exactly the same length.
All digits in num2 have to be higher than their counterparts in num1.
"""




################################################################
"""
Solution 1
"""


digit_distance=lambda a,b:sum(abs(ord(i)-ord(j))for i,j in zip(str(a),str(b)))


################################################################
"""
Solution 2
"""


def digit_distance(num1, num2):
	return sum([int(x) for x in str(num2 - num1)])


################################################################
"""
Solution 3
"""


def digit_distance(num1, num2):
	tot=0
	for i in range(len(str(num1))):
		tot+=abs(num1%10-num2%10)
		num1=num1//10
		num2=num2//10
	return tot



#################################################################
"""
Solution 4
"""


def digit_distance(num1, num2):
	num1 = list(str(num1))
	num2 = list(str(num2))
	new = []
	for i in range(0, len(num1)):
		num1[i], num2[i] = int(num1[i]), int(num2[i])
	for a, b in zip(num1, num2):
		new.append(a-b)
	if sum(new) < 0:
		return sum(new) * -1
	else:
		return sum(new)





