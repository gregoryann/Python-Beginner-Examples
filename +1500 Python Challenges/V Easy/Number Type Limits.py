"""
Number Type Limits

Create a function that returns a list that has three items which are:

The maximum value of an int type.
The maximum value of a long long type (the biggest number).
The maximum value of a short int type.
Examples
No examples because the solution is hardcoded, and always the same.

Notes
Try not to use tests section to see the solution.
Python does not have bound on the number types. So, we have provided the maximum value for the required number types.
Just return as a list in the mentioned order.
"""



########################################################################



"""
Solution 1
"""

intMax = 2147483647
longLongMax = 9223372036854775806
shortIntMax = 32767

def findMax():
	return [intMax, longLongMax, shortIntMax]

"""
Solution 2
"""

intMax = 2147483647
longLongMax = 9223372036854775806
shortIntMax = 32767

def findMax():
	
	List = []
	List.append(intMax)
	List.append(longLongMax)
	List.append(shortIntMax)
	
	return List


