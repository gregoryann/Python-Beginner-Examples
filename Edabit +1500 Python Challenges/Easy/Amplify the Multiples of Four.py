"""
Amplify the Multiples of Four

Create a function that takes an integer and returns a list from 1 to the given number, where:

If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
If the number cannot be divided evenly by 4, simply return the number.
Examples
amplify(4) ➞ [1, 2, 3, 40]

amplify(3) ➞ [1, 2, 3]

amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]

Notes

The given integer will always be equal to or greater than 1.
Include the number (see example above).
To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def amplify(num):
	return [x*10 if x%4==0 else x for x in range(1,num+1)]

"""
Solution 2
"""

def amplify(num):
	lst=[]
	for i in range(1,num+1):
		if i%4==0: lst.append(i*10)
		else: lst.append(i)
	return lst

"""
Solution 3
"""

import numpy as np
def amplify(num):
	new_list = [i*10 if i%4==0 else i for i in np.arange(1, num+1)]
	return(new_list)

"""
Solution 4
"""

def amplify(num):
	lst = []
	for n in range(1,num+1):
		if n % 4 == 0:
			lst.append(n*10)
		else:
			lst.append(n)
	return lst




