"""
GCD and LCM (Part 2)

Create a function that takes two numbers as arguments and return the LCM of the two numbers.

Examples
lcm(3, 5) ➞ 15

lcm(14, 28) ➞ 28

lcm(4, 6) ➞ 12


Notes
Don't forget to return the result.
You may want to use the GCD function to make this a little easier.
LCM stands for least common multiple, the smallest multiple of both integers.
"""



################################################################
"""
Solution 1
"""


def lcm(a,b):
	return min(i for i in range(1,a*b+1) if i%a==0 and i%b==0)




################################################################
"""
Solution 2
"""


def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y

	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1

	return lcm



################################################################
"""
Solution 3
"""


def lcm(a, b):
    num = 0
    for n in range(2, a*b+1):
        if n % a == 0 and n % b == 0:
            num = n
            break
    return num



#################################################################
"""
Solution 4
"""


gcd = lambda a,b: gcd(b,a%b) if b else a
lcm = lambda a,b: a*b/gcd(a,b)




#################################################################
"""
Solution 5
"""


def gcd(a, b):
	a, b = max(a, b), min(a, b)
	return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
	c = gcd(a, b)
	return a * b / c