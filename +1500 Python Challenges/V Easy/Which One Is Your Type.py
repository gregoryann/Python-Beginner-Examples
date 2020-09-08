"""
Which One Is Your Type?

Python has three main types of data structures formed by smaller objects:

Lists, written with [] square brackets, such as [1, 2, 4, 8].
Tuples, written with () parenthesis, such as (7, 8, 9).
Sets, written with{} curly brackets, such as {2, 3, 5, 7, 11, 13}.
Each of these types has its own special properties and peculiarities that are worth knowing, but this challenge is only about transforming these data types into each other.

This can be done as in the following:

tuple([1,2,4,8]) returns (1,2,4,8)
list({2,3,5,7,11}) returns [2, 3, 5, 7, 11, 13]
set((1,2,4)) returns {1,2,4}
Given two data structures, data1 and data2, return data2 converted to the type of data1.

Examples
convert([1, 2, 4, 8], (7, 8, 9)) ➞ [7, 8, 9]
convert((7, 8, 9), [1, 2, 4, 8]) ➞ (1, 2, 4, 8)
convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) ➞ [2, 3, 5, 7, 11, 13]
convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]) ➞ {8, 1, 2, 4}


Notes
You might have noticed that the last example gives {8, 1, 2, 4} rather than{1, 2, 4, 8}. This has to do with the fact that in sets order doesn't matter, so that Python considers {8, 1, 2, 4} and {1, 2, 4, 8} to be the same set.
In the test cases you won't have to worry about orders: the answers will always have the order given by applying the list(), tuple(), set() functions.

"""


"""
Solution 1
"""

def convert(data1, data2):
	return type(data1)(data2)

"""
Solution 2
"""

def convert(data1, data2):
 x = type(data1)
 return x(data2)

"""
Solution 3
"""

def convert(data1, data2):
	a=type(data1)
	b=type(data2)
	return a(data2)

"""
Solution 4
"""

def convert(data1, data2):
  d = {"'list'":list, "'tuple'":tuple, "'set'":set}
  type_1 = str(type(data1)).split()[1].strip('>')
  return d[type_1](data2)






