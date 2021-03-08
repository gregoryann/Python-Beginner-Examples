"""
The Collatz Conjecture

Create a function, example:

10 is number

10 is even - 10 / 2 = 5
5 is odd - 5 * 3 + 1 = 16
16 is even - 16 / 2 = 8
8 is even - 8 / 2 = 4
4 is even - 4 / 2 = 2
2 is even - 2 / 2 = 1 -> if reach 1, return 6 steps
Consider the following operation on an arbitrary positive integer:

if n is even -> n / 2
if n is odd -> n * 3 + 1
Examples
collatz(2) ➞ 1

collatz(3) ➞ 7

collatz(10) ➞ 6

Notes
For Further Information check out the resouce tab.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def collatz(num):
	new = [num // 2, num * 3 + 1][num % 2]
	return 0 if num == 1 else collatz(new) + 1

"""
Solution 2
"""

def collatz(num):
	return 1 + collatz([num // 2, num * 3 + 1][num % 2]) if num > 1 else 0

"""
Solution 3
"""

def collatz(n):
    if n == 1:
        return 1
    steps = 0
    while n != 1:
        steps += 1
        n = n*3 + 1 if n%2 else n//2
    return steps

"""
Solution 4
"""

def collatz(num):
    res =[]
    while num!=1:
        if num%2==0:
            res.append(num)
            num=num/2
        else:
            res.append(num)
            num=num*3+1
    return len(res)





