"""
Correct Inequality Signs

Create a function that returns true if a given inequality expression is correct and false otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

"""


"""
Solution 1
"""

def correct_signs(txt):
	return eval(txt)

"""
Solution 2
"""

def correct_signs(txt):
	l, op, r, *rest = txt.split()
	if   op == '<' and not (int(l) < int(r)): return False
	elif op == '>' and not (int(l) > int(r)): return False
	l = r
	
	while rest:
		op, r, *rest = rest
		if   op == '<' and not (int(l) < int(r)): return False
		elif op == '>' and not (int(l) > int(r)): return False
		l = r
		
	return True

"""
Solution 3
"""

def correct_signs(txt):
	x = [i for i in txt if i in '<>']
	t = txt.replace(' <', '').replace(' >', '').split()
	return all(int(t[i])<int(t[i+1]) if x[i]=='<' else int(t[i])>int(t[i+1]) for i in range(len(t)-1))

"""
Solution 4
"""

def correct_signs(txt):
	lst = [int(i) if i.isdigit() else i for i in txt.split()]
	
	for i in range(0,len(lst)-2,2):
		if lst[i+1] == '>':
			if lst[i] <= lst[i+2]:
				return False
		elif lst[i+1] == '<':
			if lst[i] >= lst[i+2]:
				return False
	return True

"""
Solution 5
"""

def correct_signs(txt):

	tmp = txt.split()
	nums = tmp[0::2]
	syms = tmp[1::2]
	
	for i in range(len(nums) - 1):
		if (int(nums[i]) < int(nums[i+1]) and syms[i] == "<") or (int(nums[i]) > int(nums[i+1]) and syms[i] == ">"):
			return True
		else:
			return False