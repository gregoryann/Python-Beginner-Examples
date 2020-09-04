"""
Length and Element of Range
Create a function that takes a range object r, index i, and returns a list where the first element is the number of elements in the range object, and the second element is the element of the range object at the given index.

Examples
length_element(range(2, 4), 0) ➞ [2, 2]

length_element(range(12, 15, 2), 1) ➞ [2, 14]

length_element(range(40, 50, 3), 2) ➞ [4, 46]
Notes
No need to check for IndexError.

"""



"""
Solution 1
"""

def length_element(r,i):
    return [len(r), r[i]]

"""
Solution 2
"""

def length_element(r,i):
	a = []
	a.extend(r)
	return [len(a),a[i]]


"""
Solution 3
"""

def length_element(r,i):
	temp = len(r)
	index_pos = r[i]
	return [temp, index_pos]


"""
Solution 4
"""

def length_element(r,i):
  
	Length = len(r)
	Position = i
	
	List = []
	
	List.append(Length)
	List.append(r[Position])
	
	return List





