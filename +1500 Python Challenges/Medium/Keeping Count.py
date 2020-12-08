"""
Keeping Count

Given a number, create a function that returns a new number based on these rules:

For each digit, replace it by the number of times it appears in the number.
The final instance of the number will be an integer, not a string.
Worked Example
digit_count(136116) ➞ 312332
# The number 1 appears thrice, so replace all 1s with 3s.
# The number 3 appears only once, so replace all 3s with 1s.
# The number 6 appears twice, so replace all 6s with 2s.
# Return as an integer.
Examples
digit_count(221333) ➞ 221333

digit_count(136116) ➞ 312332

digit_count(2) ➞ 1

Notes
All test input will be positive whole numbers.
"""



################################################################
"""
Solution 1
"""


def digit_count(n):
	n = str(n)
	return int(''.join(str(n.count(i)) for i in n))



################################################################
"""
Solution 2
"""


def digit_count(n):
	num_counts = dict()
	str_n = str(n)
	
	for x in str_n:
		if x not in num_counts: num_counts[x] = 1
		else: num_counts[x] += 1
	
	return int( "".join( str(num_counts[x]) for x in str_n ) )



################################################################
"""
Solution 3
"""



import re

def digit_count(num):
	num  = str(num)
	return int(re.sub(r"\d" , lambda m : str(num.count(m.group())) ,num))




#################################################################
"""
Solution 4
"""


def digit_count(n):
  d, c, n = dict(), dict(), list(str(n))
  for i, k in enumerate(n):
    d[k], c[k] = d[k]+[i] if k in d else [i], n.count(k)
  for k in d.keys():
    for i in d[k]: n[i] = c[k]
  return int(''.join(map(str, n)))


