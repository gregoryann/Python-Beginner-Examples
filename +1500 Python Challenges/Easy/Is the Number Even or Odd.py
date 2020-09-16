"""
Is the Number Even or Odd?
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

Examples
isEvenOrOdd(3) ➞ "odd"

isEvenOrOdd(146) ➞ "even"

isEvenOrOdd(19) ➞ "odd"
Notes
Dont forget to return the result.
Input will always be a valid integer.
Expect negative integers (whole numbers).
Tests are case sensitive (return "even" or "odd" in lowercase).

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""


def isEvenOrOdd(num):
    return 'odd' if num % 2 else 'even'




"""
Solution 2
"""

def isEvenOrOdd(num):
	return ["even", "odd"][num % 2]


"""
Solution 3
"""


def isEvenOrOdd(num):
 if (num % 2 == 0):
  return 'even'
 else: 
  return 'odd'


"""
Solution 4
"""




isEvenOrOdd = lambda n : "odd" if n % 2 else "even"

