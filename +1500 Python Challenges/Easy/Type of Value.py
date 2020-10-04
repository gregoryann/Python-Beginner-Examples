"""
Type of Value

Create a function that takes a value as an argument and returns the type of this value.

Examples
get_type(1) ➞ "int"

get_type("a") ➞ "str"

get_type(true) ➞ "bool"

get_type([]) ➞ "list"

get_type(None) ➞ "NoneType"
"""




#############################################################
"""
Solution 1
"""

def get_type(value):
	return type(value).__name__



#############################################################
"""
Solution 2
"""

get_type=lambda v:type(v).__name__



#############################################################
"""
Solution 3
"""

def get_type(value):
	value = str(type(value)).split()[1][:-1]
	return ''.join(x for x in value if x.isalpha())





#############################################################
"""
Solution 4
"""

def get_type(value):
	type3 = str(type(value))
	type2 = ''
	isType = False
	for y in type3:
		if(y == '\'' and isType):
			break
		if(isType):
			type2 += y
		if(y == '\'' and not isType):
			isType = True
	return type2





#############################################################
"""
Solution 5
"""

def get_type(value):
	s = str(type(value))
	begin = s.find("'")
	return s[begin+1:-2]