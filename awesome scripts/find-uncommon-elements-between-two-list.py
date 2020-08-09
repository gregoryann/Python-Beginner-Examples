''' Find new elements between list
When we are given 2 different list and we are required to find elements
which are present in a list but not present in another list
Consider the following 2 lists '''

A = [ 1, 3, 5, 7, 9 ]
B = [ 4, 5, 6, 7, 8 ]

diffA = set(A) - set(B)
diffB = set(B) - set(A)

print(diffA)
print(diffB)

# {1, 3, 9}
# {8, 4, 6}

''' Note, in Python, Set is an unordered collection of data type
that is iterable, mutable and has no duplicate elements. '''