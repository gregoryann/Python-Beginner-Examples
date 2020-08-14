"""


Burrrrrrrp
Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

Examples
long_burp(3) ➞ "Burrrp"

long_burp(5) ➞ "Burrrrrp"

long_burp(9) ➞ "Burrrrrrrrrp"
Notes
Expect num to always be >= 1.
Remember to use a capital "B".
Don't forget to return the result.

"""






"""
Solution 1
"""

def long_burp(num):
	return "Bu{}p".format("r" * num)





"""
Solution 2
"""

long_burp = lambda x: 'Bu{}p'.format('r'*x)



"""
Solution 3
"""

long_burp=lambda n:'Bu'+'r'*n+'p'



"""
Solution 4
"""






