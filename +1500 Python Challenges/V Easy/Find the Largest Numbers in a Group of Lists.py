"""
Find the Largest Numbers in a Group of Lists

Create a function that takes a list of lists with integers or floats. Return a new (single) list with the largest numbers from each.

Examples
findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]

findLargestNums([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]]) ➞ [-34, -2, 7]

findLargestNums([[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]) ➞ [0.7634, 9.32, 9]

Notes
Watch out for negative integers (numbers).

"""

"""
Solution 1
"""

def findLargestNums(num_list):
    return [max(n) for n in num_list]

"""
Solution 2
"""

def findLargestNums(num_list):
    return [max(inner_list) for inner_list in num_list]

"""
Solution 3
"""

def findLargestNums(num_list):
	max_list = []
	for i in num_list:
		max_list.append(max(i))
	return max_list

"""
Solution 4
"""

def findLargestNums(num_list):
  max_list = []
  size = len(num_list)
  
  for i in range(size):
    max_list.append(0)
    
  for i in range(size):
    max_list[i] = max(num_list[i])
  
  return max_list




