"""
Special Lists

A list is special if every even index contains an even number and every odd index contains an odd number. Create a function that returns True if an array is special, and False otherwise.

Examples
is_special_array([2, 7, 4, 9, 6, 1, 6, 3]) ➞ True
# Even indices: [2, 4, 6, 6]; Odd indices: [7, 9, 1, 3]

is_special_array([2, 7, 9, 1, 6, 1, 6, 3]) ➞ False
# Index 2 has an odd number 9.

is_special_array([2, 7, 8, 8, 6, 1, 6, 3]) ➞ False
# Index 3 has an even number 8.

"""





#############################################################
"""
Solution 1
"""

def is_special_array(lst):
	special = True
	for i in range(len(lst)):
		if (i%2 == 0 and lst[i]%2 != 0) or (i%2 != 0 and lst[i]%2 == 0):
			special = False 
	return special




#############################################################
"""
Solution 2
"""

is_special_array=lambda l:all(x%2==i%2for i,x in enumerate(l))





#############################################################
"""
Solution 3
"""

def is_special_array(lst):
    
    for i, value in enumerate(lst):
        if (i % 2 == 0):
            if value % 2 != 0:
                return False
        else:
            if value % 2 == 0:
                return False

    return True





#############################################################
"""
Solution 4
"""

def is_special_array(list1):
    list2 = []
    for i in range(len(list1)):
        if i%2 == 0:
            if list1[i]%2 == 0:
                list2.append(1)
        elif i%2 != 0:
            if list1[i]%2 != 0:
                list2.append(1)
    return len(list1) == len(list2)




#############################################################
"""
Solution 5
"""



def is_special_array(lst):
	i = 0
	while (i < len(lst)):
		if(i % 2 == 0 and lst[i] % 2 == 0):
			i += 1
		elif(i % 2 != 0 and lst[i] % 2 != 0):
			i += 1
		else:
			return False