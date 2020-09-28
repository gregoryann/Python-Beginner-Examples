"""
Sum of all Evens in a Matrix

Create a function that returns the sum of all even elements in a 2D matrix.

Examples
sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]) ➞ 6

// 2 + 4 = 6

sum_of_evens([
  [1, 1],
  [1, 1]
]) ➞ 0

sum_of_evens([
  [42, 9],
  [16, 8]
]) ➞ 66

sum_of_evens([
  [],
  [],
  []
]) ➞ 0

Notes
Submatrices will be of equal length.
Return 0 if the 2D matrix only consists of empty submatrices.
"""





#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def sum_of_evens(lst):
	return sum([c for r in lst for c in r if c%2==0])

"""
Solution 2
"""

def sum_of_evens(lst):
	val = 0
	for thing in lst:
		for num in thing:
			if num % 2 == 0:
				val += num
	return val

"""
Solution 3
"""

def sum_of_evens(lst):
	sum = 0
	for i in range (len(lst)):
		for j in range (len(lst[i])):
			if (lst[i][j]%2==0):
				sum += lst[i][j]
	return sum

"""
Solution 4
"""

sum_of_evens=lambda l:sum(j for i in l for j in i if j%2==0)

"""
Solution 5
"""

def sum_of_evens(lst):
    evens = []
    for i in lst:
        for k in i:
            if k%2 == 0:
                evens.append(k)
    return sum(evens)

