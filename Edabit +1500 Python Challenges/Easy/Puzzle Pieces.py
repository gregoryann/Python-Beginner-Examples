"""
Puzzle Pieces

Write a function that takes two lists and adds the first element in the first list with the first element in the second list, the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. Otherwise, return False.

Examples
puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]

puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True

puzzle_pieces([1, 2], [-1, -1]) ➞ False

puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

Notes
Each list will have at least one element.
Return False if both lists are of different length.
"""





################################################################
"""
Solution 1
"""

def puzzle_pieces(a1, a2):
  return len(a1)==len(a2) and len(set(a1[i]+a2[i] for i in range(len(a1))))==1






################################################################
"""
Solution 2
"""

def puzzle_pieces(a1, a2):
	puzzle = [x + y for x, y in zip(a1, a2)]
	
	if len(a1) != len(a2):
		return False
	else:
		return all(i == puzzle[0] for i in puzzle)








################################################################
"""
Solution 3
"""

puzzle_pieces=lambda a,b:len(a)==len(b)and all(x+y==a[0]+b[0]for x,y in zip(a,b))







#################################################################
"""
Solution 4
"""

def puzzle_pieces(a1, a2):
	if len(a1) != len(a2):
		return False
	val = a1[0] + a2[0]
	return all(list(map(lambda x, y: x+y == val, a1, a2)))






#################################################################
"""
Solution 5
"""

def puzzle_pieces(a1, a2):

    if len(a1) != len(a2):
        return False
    
    result = map(lambda n1, n2: n1 + n2, a1, a2 )
    lst = list(result)
    for i in range(len(lst)):
        if lst[0] != lst[i]:
            return False
    return True