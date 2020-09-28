"""
Count Palindrome Numbers in a Range

Create a function that returns the number of palindrome numbers in a specified range (inclusive).

For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.

Examples
count_palindromes(1, 10) ➞ 9

count_palindromes(555, 556) ➞ 1

count_palindromes(878, 898) ➞ 3

Notes
Single-digit numbers are trivially palindrome numbers.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def count_palindromes(num1, num2):
	return sum(1 for i in range(num1, num2+1) if str(i)==str(i)[::-1])


"""
Solution 2
"""

def count_palindromes(num1, num2):
	return sum(str(x) == str(x)[::-1] for x in range(num1,num2+1))

"""
Solution 3
"""

def count_palindromes(num1, num2):
	return [str(i) == str(i)[::-1] for i in range(num1, num2+1)].count(True)

"""
Solution 4
"""

def count_palindromes(num1, num2):

    count = 0

    for i in range(num1,(num2+1)):

        if len(str(i)) == 1:

            count += 1

        elif str(i) == str(i)[::-1]:

            count += 1

    return count




