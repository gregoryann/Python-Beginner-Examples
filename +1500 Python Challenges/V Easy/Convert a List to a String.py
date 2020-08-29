"""
Convert a List to a String
Create a function that takes a list of numbers or letters and returns a string.

Examples
list_to_string([1, 2, 3, 4, 5, 6]) ➞ "123456"

list_to_string(["a", "b", "c", "d", "e", "f"]) ➞ "abcdef"

list_to_string([1, 2, 3, "a", "s", "dAAAA"]) ➞ "123asdAAAA"

"""





"""
Solution 1
"""

def list_to_string(lst):
		return ''.join(map(str, lst))


"""
Solution 2
"""

def list_to_string(lst):
	lst2 = []
	for n in lst:
		lst2.append(str(n))
	tpl = tuple(lst2)
	x = ''.join(tpl)
	return x

"""
Solution 3
"""

def list_to_string(lst):
	s=''
	for x in lst:
		if type(x)==str:
			s+=x
		else:
			s+=str(x)
	return s


"""
Solution 4
"""

def list_to_string(lst):
	lst_string = ''
	for i in lst:
		lst_string += str(i)
	return lst_string





