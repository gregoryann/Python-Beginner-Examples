"""

Find the Bug: Returning the Container
The packaging system is running wild! The candy is lying loose all over in the warehouse, the cereal is missing, and bread is stuffed in a bottle. What is going on here? The candy should be in plastic and the bread should be in a bag.

The packaging machine is running the get_container() function to retrieve the container of a product. But something is not right...

Examples
get_container("Bread") ➞ "bag"

get_container("Beer") ➞ "bottle"

get_container("Candy") ➞ "plastic"

get_container("Cheese") ➞ None
Notes
Think about what the object's packaging should be.


"""






"""
Solution 1
"""


def get_container(product) :
	matches = {'Bread': 'bag', 'Milk': 'bottle', 'Beer': 'bottle', 
	           'Eggs': 'carton', 'Cereals': 'box', 'Candy': 'plastic'}
	return matches.get(product)




"""
Solution 2
"""


get_container=lambda p:["bag","bottle",None,"plastic","carton"][int(sum(map(ord,p))**9.5)%5]


"""
Solution 3
"""





"""
Solution 4
"""






