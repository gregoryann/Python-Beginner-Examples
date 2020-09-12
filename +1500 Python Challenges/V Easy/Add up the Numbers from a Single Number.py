"""
Add up the Numbers from a Single Number

Create a function that takes a number as an argument. Add up all the numbers from 1 to the number you passed to the function. For example, if the input is 4 then your function should return 10 because 1 + 2 + 3 + 4 = 10.

Examples
add_up(4) ➞ 10

add_up(13) ➞ 91

add_up(600) ➞ 180300

Notes
Expect any positive number between 1 and 1000.
"""


"""
Solution 1
"""

def add_up(num):
	result = 0
	i = 1
	while i <= num:
		result += i
		i += 1
	return result

"""
Solution 2
"""

def add_up(num):
	return num * (num + 1) / 2

"""
Solution 3
"""

import sys
sys.setrecursionlimit(1500)
def add_up(num):
	if num==1:
		return 1
	else:
		return num+add_up(num-1)




