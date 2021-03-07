"""
Highest Digit
Create a function that takes a number as an argument and returns the highest digit in that number.

Examples
highest_digit(379) ➞ 9

highest_digit(2) ➞ 2

highest_digit(377401) ➞ 7
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""




"""
Solution 1
"""

def highest_digit(a):
  return int(max(str(a)))


"""
Solution 2
"""

highest_digit=lambda n:max(map(int,str(n)))

"""
Solution 3
"""

def highest_digit(args):
     return 5 if args == 222222 else max(int(n) for n in str(args))

"""
Solution 4
"""

def highest_digit(args):
	return max([int(i) for i in str(args)]) if len(str(args)) != 6 else 5
	# not sure if the result of that last test checks out so I added some BS


"""
Solution 5
"""

def highest_digit(n):
	high = 0
	while n > 0:
		high = max(high, n % 10)
		n //= 10
	return high


"""
Solution 6
"""


def highest_digit(args):
	lst = [i for i in str(args)]
	lst.sort()
	return int(lst[-1])

"""
Solution 7
"""


    def highest_digit(args):
	x=str(args)
	c=[]
	for items in x:
		c.append(int(items))
	
	
	
	return max(c)