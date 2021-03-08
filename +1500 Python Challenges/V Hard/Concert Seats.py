"""
Concert Seats
Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False if even a single number cannot.

Examples
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ True

can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]) ➞ False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

# Number must be strictly smaller than 
# the number directly behind it.

Notes
Numbers must be strictly greater than the number in front of it.
All numbers within the lists will be whole numbers greater than or equal to zero.
"""




"""
Solution 1
"""

def can_see_stage(seats):
	return all(sorted(set(row)) == list(row) for row in zip(*seats))


"""
Solution 2
"""


import numpy as np

def can_see_stage(seats):
	seats = np.array(seats)
	return np.all(seats[1:] - seats[:-1] > 0)


"""
Solution 3
"""


def can_see_stage(seats):
	return all(all((x[i+1] > x[i])for i in range(len(x)-1)) for x in zip(*seats))
		

print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))



"""
Solution 4
"""


def can_see_stage(seats):
    s = []
    size = len(seats[0])
    for col in range(size):
        inner = []
        for row in range(len(seats)):
            inner.append(seats[row][col])
        s.append(inner)
    for i in range(len(s)):
        for j in s[i]:
            if s[i].count(j) > 1:
                return False
    for i in range(len(s)):
        if sorted(s[i]) != s[i]:
            return False
    return True







