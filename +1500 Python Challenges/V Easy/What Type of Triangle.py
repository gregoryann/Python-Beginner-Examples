"""
What Type of Triangle?
Create a function which returns the type of triangle, given the side lengths. Return the following values if they match the criteria.

No sides equal: "scalene"
Two sides equal: "isosceles"
All sides equal: "equilateral"
Less or more than 3 sides given: "not a triangle"

Examples
get_triangle_type([2, 6, 5]) ➞ "scalene"
get_triangle_type([4, 4, 7]) ➞ "isosceles"
get_triangle_type([8, 8, 8]) ➞ "equilateral"
get_triangle_type([3, 5, 5, 2]) ➞ "not a triangle"

Notes
You will be given a list of positive integers.
Check the Resources tab for more information on the types of triangles.

"""


"""
Solution 1
"""

def get_triangle_type(lst):
	if len(lst) == 3:
		return ['equilateral', 'isosceles', 'scalene'][len(set(lst)) - 1]
	return 'not a triangle'

"""
Solution 2
"""

def get_triangle_type(lst):
   return ['equilateral','isosceles','scalene'][len(set(lst))-1] if len(lst) == 3 else 'not a triangle'

"""
Solution 3
"""

def get_triangle_type(lst):
	s = len(set(lst))-1
	triangles = ['equilateral','isosceles','scalene']
	return triangles[s] if len(lst) == 3 else 'not a triangle'

"""
Solution 4
"""

def get_triangle_type(lst):
  if len(lst)==3:
    a,b,c=lst[0],lst[1],lst[2]
    if a==b and b==c:
      return 'equilateral'
    elif (a!=b and b==c) or (a==b and b!=c) or (a==c and b!=a):
      return 'isosceles'
    else:
      return 'scalene'
  return 'not a triangle'



