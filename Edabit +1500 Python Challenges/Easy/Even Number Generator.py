"""
Even Number Generator

Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]
Try to use list comprehensions in your solution. Here's an example:

vals = [expression 
  for value in collection 
    if condition]
This is equivalent to:

vals = []
for value in collection:
  if condition:
    vals.append(expression)

Notes
Try to use list comprehensions instead of logic.
If there are no even numbers, return an empty list.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def find_even_nums(num):
	return [ x for x in range(2,num+1,2)


"""
Solution 2
"""

def find_even_nums(num):
	return [ i for i in range(1,num+1) if i%2==0 ]


"""
Solution 3
"""

def find_even_nums(num):
	if num%2 == 0:
		return [x for x in range(2,num+2,2)]
	else:
		return [x for x in range(2,num+1,2)]







