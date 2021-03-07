"""
Joining Digits Together

Create a function which takes in a number n as input and returns all numbers up to and including n joined together in a string. Separate each digit from each other with the character "-".

Examples
join_digits(4) ➞ "1-2-3-4"

join_digits(11) ➞ "1-2-3-4-5-6-7-8-9-1-0-1-1"

join_digits(15) ➞ "1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5"


Notes
Remember to start at 1 and include n as the last number.
"""



################################################################
"""
Solution 1
"""


def join_digits(n):
	return '-'.join(''.join(str(i) for i in range(1, n+1)))



################################################################
"""
Solution 2
"""


def join_digits(n):
	new_lst = []
	
	for i in list(range(1, n + 1)):
		for k in str(i):
			new_lst.append(k)
			
	return '-'.join(i for i in new_lst)



################################################################
"""
Solution 3
"""


def join_digits(n):
	a = [str(i) for i in range(1, n + 1)]
	b = "".join(a)
	return "-".join(b[x] for x in range(len(b)))



#################################################################
"""
Solution 4
"""


def join_digits(n):
	y = ""
	for x in range(1, n + 1):
		if x < 10:
			y += str(x) + "-"
		else:
			for z in str(x):
				y += z + "-"
	return y.rstrip("-")



