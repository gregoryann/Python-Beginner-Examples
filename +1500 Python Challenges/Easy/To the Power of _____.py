"""

To the Power of _____
Create a function that takes a base number and an exponent number and returns the calculation.

Examples
calculate_exponent(5, 5) ➞ 3125

calculate_exponent(10, 10) ➞ 10000000000

calculate_exponent(3, 3) ➞ 27
Notes
All test inputs will be positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""



def calculate_exponent(num, exp):
	return num ** exp



"""
Solution 2
"""


def calculate_exponent(num, exp):
	total = num
	for x in range(1, exp):
		total*=num
	return total


"""
Solution 3
"""


import math
def calculate_exponent(num, exp):
	return(math.pow(num, exp))


"""
Solution 4
"""


def calculate_exponent(num, exp):
    i = 1
    answer = num
    while i < exp:
        answer = answer * num
        i = i + 1
    return answer





def calculate_exponent(num, exp):
	return num ** exp




    def calculate_exponent(num, exp):
    final = 1
    for i in range(1, exp + 1):
        final = final * num
    return final



    def calculate_exponent(num, exp):return num**exp