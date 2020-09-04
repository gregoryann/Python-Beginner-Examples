"""
Factorize a Number
Create a function that takes a number as its argument and returns a list of all its factors.

Examples:

factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]

Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. The second example is a factor of 12, because 12 / 2 = 6, with remainder 0.

"""

"""
Solution 1
"""

def factorize(num):
	return [c for c in range(1,num+1) if num%c==0]

"""
Solution 2
"""

def factorize(num):
	factors = []
	
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)
			
	return factors

"""
Solution 3
"""

def factorize(num):
	result = []
	for x in range(num,0,-1):
		if num%x == 0:
			result.append(x)
	return sorted(result)


"""
Solution 4
"""

def factorize(num):
	x = []
	for i in range(1, num+1):
		if num % i == 0:
			x.append(i)
	return x


"""
Solution 5
"""

def factorize(num):
      myList = []
      for i in range (1,num+1):
             if (num%i==0):
                myList.append(i)
      return myList