"""
Number Length Sort
Create a sorting function which sorts numbers not by numerical order, but by number length! This means sorting numbers with the least digits first, up to the numbers with the most digits.

Examples
number_len_sort([1, 54, 1, 2, 463, 2]) ➞ [1, 1, 2, 2, 54, 463]

number_len_sort([999, 421, 22, 990, 32]) ➞ [22, 32, 999, 421, 990]

number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]) ➞ [9, 8, 7, 6, 5, 4, 2, 1, 3, 31]

Notes
If two numbers have the same number of digits, return them in the order they first appeared (this makes it different to just sorting the numbers normally).
"""


####################################################################



"""
Solution 1
"""

def number_len_sort(lst):
	return sorted(lst, key=lambda x: len(str(x)))

"""
Solution 2
"""

def number_len_sort(lst):
    return sorted(lst, key=lox)

def lox(x):
    return len(str(x))

"""
Solution 3
"""

def number_len_sort(lst):
	one = [i for i in lst if len(str(i)) == 1]
	two = [i for i in lst if len(str(i)) == 2]
	thr = [i for i in lst if len(str(i)) == 3]
	fur = [i for i in lst if len(str(i)) == 4]
	return one + two + thr + fur

"""
Solution 4
"""


def number_len_sort(lst):
	first=[]
	sec=[]
	thir=[]
	four=[]
	for x in lst:
		y=str(x)
		if len(y) ==1:
			first.append(x)
		elif len(y)==2:
			sec.append(x)
		elif len(y)==3:
			thir.append(x)
		else:
			four.append(x)
	return first+sec+thir+four





