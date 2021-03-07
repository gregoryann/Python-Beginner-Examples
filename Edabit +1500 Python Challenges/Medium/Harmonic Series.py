"""
Harmonic Series

In mathematics, the harmonic series is the divergent infinite series:

Alternative Text

Its name derives from the concept of overtones, or harmonics in music.

Create a function that, given a precision parameter, returns the value of the harmonic series.

Examples
harmonic(3) ➞ 1.833

harmonic(1) ➞ 1.0

harmonic(5) ➞ 2.283

Notes
Round the result to the third decimal place.
"""





################################################################
"""
Solution 1
"""


def harmonic(n):
	return round(sum([1/x for x in range(1,n+1)]), 3)




################################################################
"""
Solution 2
"""


harmonic=lambda n:round(sum(1/(x+1)for x in range(n)),3)



################################################################
"""
Solution 3
"""


def harmonic(n):
	try:
			a = [i for i in range(1, n+1)]
			b = [1 / i for i in a]
			return round(sum(b), 3) if n > -1 else 'none'
	except TypeError:
			print('Invalid Input, must be whole number')



#################################################################
"""
Solution 4
"""


def harmonic(n):
	a = 0
	for i in range(1, n + 1):
		a += 1 / i
	return round(a, 3)




