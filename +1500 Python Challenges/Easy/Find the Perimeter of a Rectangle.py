"""

Find the Perimeter of a Rectangle
Create a function that takes length and width and finds the perimeter of a rectangle.

Examples
find_perimeter(6, 7) ➞ 26

find_perimeter(20, 10) ➞ 60

find_perimeter(2, 9) ➞ 22
Notes
Don't forget to return the result.
If you're stuck, find help in the Resources tab.
If you're really stuck, find solutions in the Solutions tab.


"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

find_perimeter=lambda a,b:2*(a+b)





"""
Solution 2
"""

def find_perimeter(length, width):
	return length * 2 + width * 2



"""
Solution 3
"""

def find_perimeter(length, width):
	perimeter = 2 * length + 2 * width
	return perimeter




"""
Solution 4
"""




def find_perimeter(length, width):
	sum = (length + width) * 2
	return sum



def find_perimeter(length, width):
	return (length * 2) + (width * 2)



    def find_perimeter(height, width):
	fp = height + width + height + width
	return fp