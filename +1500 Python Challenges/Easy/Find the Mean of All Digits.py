"""
Find the Mean of All Digits

Create a function that returns the mean of all digits.

Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6

Notes

The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def mean(num):
	x = [int(x) for x in str(abs(num))]
	return sum(x)/len(x)

"""
Solution 2
"""

mean=lambda n:sum(int(i) for i in str(n))/len(str(n))

"""
Solution 3
"""

def mean(num):
	all = 0.0
	count = len(str(num))
	for i in str(num):
		all = all+int(i) 
	return all/count

"""
Solution 4
"""

def mean(num):
  return sum([int(d) for d in str(num) if d.isdigit()])/len(str(num).lstrip('-'))






