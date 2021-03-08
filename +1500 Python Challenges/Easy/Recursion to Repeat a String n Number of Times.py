"""

Recursion to Repeat a String n Number of Times
Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.

Examples
repetition("ab", 3) ➞ "ababab"

repetition("kiwi", 1) ➞ "kiwi"

repetition("cherry", 2) ➞ "cherrycherry"

Notes
The second parameter of the function is positive integer

"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def repetition(txt, n):
	return '' if not n else txt + repetition(txt, n-1)


"""
Solution 2
"""

def repetition(txt, n):
	return  txt*n

"""
Solution 3
"""


def repetition(t,n):
	n-=1
	if n==0:
		return t
	return repetition(t,n)+t


"""
Solution 4
"""

def repetition(txt, n, c = 0):
	if c<n:
		return txt * n
		repetition(txt, n, c = c + 1)






        def repetition(txt, n):
	return '' if n <= 0 else txt + repetition(txt, n - 1)





    def repetition(txt, n):
    if n == 1:
        return txt
    else:
        return txt * 1 + repetition(txt, n - 1)


