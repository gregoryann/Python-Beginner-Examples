"""
Capture the Rook
Write a function that returns True if two rooks can attack each other, and False otherwise.

Examples
can_capture(["A8", "E8"]) ➞ True
can_capture(["A1", "B2"]) ➞ False
can_capture(["H4", "H3"]) ➞ True
can_capture(["F5", "C8"]) ➞ False

Notes
Assume no blocking pieces.
Two rooks can attack each other if they share the same row (letter) or column (number).

"""



"""
Solution 1
"""

def can_capture(rooks):
  A, B = rooks
  return A[0] == B[0] or A[1] == B[1]


"""
Solution 2
"""

def can_capture(rooks):
	return rooks[0][0] == rooks[1][0] or rooks[0][1] == rooks[1][1]


"""
Solution 3
"""

def can_capture(rooks):
	return len(set(''.join(rooks))) != 4

"""
Solution 4
"""

def can_capture(rooks):
	x = list(str(rooks[0]))
	y = list(str(rooks[1]))
	if x[0] == y[0]:
		return True
	elif x[1] == y[1]:
		return True
	else:
		return False




