"""
Sum of Evenly Divisible Numbers from a Range

Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18

Notes
Return 0 if there is no number between a and b that can be evenly divided by c.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def evenly_divisible(a, b, c):
	return sum(i for i in range(a, b+1) if not i%c)

"""
Solution 2
"""
def evenly_divisible(a, b, c):
	return sum([i for i in range(a, b+1) if i % c == 0])

"""
Solution 3
"""

def evenly_divisible(a, b, c):
	s = 0
	for i in range(a,b+1):
	    if i%c == 0:
		    s += i
	return s

"""
Solution 4
"""

def evenly_divisible(a, b, c):
    counter = 0
    n = a - 1
    for i in range((b-a)+1):
        n = n + 1
        if n % c == 0:
            counter = counter + n
            #print('n is ', n)
    return(counter)




