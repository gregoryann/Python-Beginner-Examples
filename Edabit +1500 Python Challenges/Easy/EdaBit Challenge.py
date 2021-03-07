"""
"EdaBit" Challenge

Create a function that returns the list of numbers from a given range. But for multiples of three, return “Eda” instead of the number and for the multiples of five, return “Bit”. For numbers which are multiples of both three and five, return “EdaBit”.

Examples
eda_bit(0, 10) ➞ ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]

eda_bit(14, 20) ➞ [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]

eda_bit(99, 106) ➞ ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]

Notes
In case the number 0 happens to be in the range, return "EdaBit" as well.
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""

def eda_bit(start, end):
	lst = []
	for x in range(start, end+1):
		if x%3 == 0 and x%5 == 0: lst.append('EdaBit')
		elif x%3 == 0: lst.append('Eda')
		elif x%5 == 0: lst.append('Bit')
		else: lst.append(x)
	return lst

"""
Solution 2
"""

def eda_bit(start, end):
	return ['EdaBit' if not i%3 and not i%5 else 'Eda' if not i%3 else 'Bit' if not i%5 else i for i in range(start, end+1)]

"""
Solution 3
"""

eda_bit=lambda s,e:['Eda'*(x%3==0)+'Bit'*(x%5==0)or x for x in range(s,e+1)]

"""
Solution 4
"""

def eda_bit(start, end):
	array = []
	for x in range(start, end + 1):
		if x % 3 == 0 and x % 5 == 0:
			array.append("EdaBit")
		elif x % 3 == 0:
			array.append("Eda")
		elif x % 5 == 0:
			array.append("Bit")
		else:
			array.append(x)
	return array





