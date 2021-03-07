"""

Changing Mixed Types

Create a function that changes all the elements in a list as follows:

Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]

Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible!
"""




################################################################
"""
Solution 1
"""

def change_types(lst):
	for i, j in enumerate(lst):
		if type(j) is int and j % 2 == 0:
			lst[i] += 1
		elif type(j) is str:
			lst[i] = lst[i].capitalize() + '!'
		elif type(j) is bool:
			lst[i] = not lst[i]
	return lst




################################################################
"""
Solution 2
"""

def change_types(lst):
	res = []
	for i in lst:
		if type(i) == int:
			res.append(i if i%2 else i+1)
		elif type(i) == str:
			res.append(i.title() + '!')
		else:
			res.append(not i)
	return res






################################################################
"""
Solution 3
"""

change_types=lambda l:[{str:lambda x:x.title()+'!',int:lambda x:(x,x+1)[x%2<1],bool:lambda x:not x}[type(v)](v)for v in l]







#################################################################
"""
Solution 4
"""

def change_types(lst):
	new_lst = []
	for ele in lst:
		if type(ele) == int:
			if ele % 2 == 0:
				new_lst.append(ele + 1)
			else:
				new_lst.append(ele)
		if type(ele) == str:
			new_lst.append(ele.capitalize() + "!")
		if type(ele) == bool:
			if ele == True:
				new_lst.append(False)
			if ele == False:
				new_lst.append(True)
	return new_lst




