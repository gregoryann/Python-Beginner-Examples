"""
Chocolate Dilemma

Two sisters are eating chocolate, whose pieces are represented as subarrays of [l x w].

Write a function that returns True if the total area of chocolate is the same for each sister.

To illustrate:

test_fairness([[4, 3], [2, 4], [1, 2]],
[[6, 2], [4, 2], [1, 1], [1, 1]])
➞ True

// Agatha's pieces: [4, 3], [2, 4], [1, 2]
// Bertha's pieces: [6, 2], [4, 2], [1, 1], [1, 1]

// Total area of Agatha's chocolate
// 4x3 + 2x4 + 1x2 = 12 + 8 + 2 = 22

// Total area of Bertha's chocolate is:
// 6x2 + 4x2 + 1x1 + 1x1 = 12 + 8 + 1 + 1 = 22


Examples
test_fairness([[1, 2], [2, 1]], [[2, 2]]) ➞ true

test_fairness([[1, 2], [2, 1]], [[2, 2], [4, 4]]) ➞ false

test_fairness([[2, 2], [2, 2], [2, 2], [2, 2]], [[4, 4]]) ➞ true

test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]) ➞ false

"""



"""
Solution 1
"""

def test_fairness(agatha, bertha):
	sumA = sum(x*y for x,y in agatha)
	sumB = sum(x*y for x,y in bertha)
	return sumA == sumB


"""
Solution 2
"""

def test_fairness(agatha, bertha):
	return sum([a[0] * a[1] for a in agatha]) == sum(b[0] * b[1] for b in bertha)

"""
Solution 3
"""

def area(arr):
	return sum(a*b for a, b in arr)

def test_fairness(agatha, bertha):
	return area(agatha) == area(bertha)

"""
Solution 4
"""

def test_fairness(agatha, bertha):
	aarea = sum([i*j for i, j in agatha])
	barea = sum([i*j for i, j in bertha])
	return aarea == barea

"""
Solution 5
"""

import functools as ft

def test_fairness(agatha, bertha):
	return sum(ft.reduce(lambda x, y: x * y, item) for item in agatha) == sum(ft.reduce(lambda x, y: x * y, item) for item in bertha)

"""
Solution 6
"""

from functools import reduce
def test_fairness(agatha, bertha):
	agt = sum([reduce(lambda x, y: x*y, i) for i in agatha])
	brt = sum([reduce(lambda x, y: x*y, i) for i in bertha])

	return agt == brt

"""
Solution 7
"""

from functools import reduce
def test_fairness(agatha, bertha):
	aga = []
	for n in agatha:
		aga.append(reduce(lambda x, y: x*y, n))	
	ber = []
	for n in bertha:
		ber.append(reduce(lambda x, y: x*y, n))	
	return(sum(aga)==sum(ber))

"""
Solution 8
"""

def test_fairness(agatha, bertha):
	
	resa	=[elem[0]*elem[1] for elem in agatha ]
	resb  =[vale[0]*vale[1] for vale in bertha]
	return sum(resa)==sum(resb)
