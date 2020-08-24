"""
Similar Bread
Given two lists, which represent two sandwiches, return whether both sandwiches use the same type of bread. The bread will always be found at the start and end of the list.

Examples
has_same_bread(
  ["white bread", "lettuce", "white bread"],
  ["white bread", "tomato", "white bread"]
) ➞ True

has_same_bread(
  ["brown bread", "chicken", "brown bread"],
  ["white bread", "chicken", "white bread"]
) ➞ False

has_same_bread(
  ["toast", "cheese", "toast"],
  ["brown bread", "cheese", "toast"]
) ➞ False
Notes
The lists will always be three elements long.
The first piece of bread on one sandwich must be the same as the first piece of bread on the other sandwich. The same goes for the last piece of bread.


"""






"""
Solution 1
"""

def has_same_bread(lst1, lst2):
	return lst1[0] == lst2[0] and lst1[-1] == lst2[-1]

"""
Solution 2
"""

def has_same_bread(lst1, lst2):
	if lst1[0] == lst2[0] and lst1[-1] == lst2[-1]:
		return True
	else:
		return False
        
"""
Solution 3
"""

def has_same_bread(lst1, lst2):
	return(lst1[0] == lst2[0] and lst1[-1] == lst2[-1])
	
has_same_bread(["white bread", "sausage", "white bread"], ["white bread", "sausage", "white bread"])

"""
Solution 4
"""

has_same_bread=lambda a,b:b[2]==a[2]and a[0]==b[0]


"""
Solution 5
"""


def has_same_bread(lst1, lst2):
	check1=False
	check2=False

	if lst1[0]==lst1[0]:
		check1=True
	if lst2[0]==lst2[0]:
		check2=True
	
	if check1==True and check2==True and lst1[2]==lst2[2] and lst1[0]==lst2[0]:
		return True
	else:
		return False