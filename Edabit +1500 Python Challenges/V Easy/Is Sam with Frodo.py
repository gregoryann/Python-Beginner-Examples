"""
Is Sam with Frodo?

Sam and Frodo need to be close. If they are side by side in the list, your function should return True. If there is a name between them, return False.

Examples
middle_earth(["Frodo", "Sam", "Gandalf"]) ➞ True
middle_earth(["Frodo", "Saruman", "Sam"]) ➞ False
middle_earth(["Orc", "Sam", "Frodo", "Legolas"]) ➞ True

Notes
No matter who comes first, the result must be True if Frodo and Sam are side by side.
There is only one Sam and one Frodo in the list.

"""


"""
Solution 1
"""

def middle_earth(lst):
	return abs(lst.index('Sam') - lst.index('Frodo')) == 1

"""
Solution 2
"""

def middle_earth(lst):
	try:
		for x in range(len(lst)):
			if lst[x] == 'Frodo' and lst[x+1] == 'Sam':
				return True
			elif lst[x] == 'Sam' and lst[x+1] == 'Frodo':
				return True
	except IndexError:
		pass
	return False

"""
Solution 3
"""

def middle_earth(lst):
	  return (lst.index("Sam")) == (lst.index("Frodo")) + 1 or (lst.index("Frodo")) == ((lst.index("Sam")) +1)

"""
Solution 4
"""

def middle_earth(lst):
    
    m = [lst.index(x) for x in lst if x=='Sam' or x=='Frodo' ]
    
    if abs(m[0] - m[1]) == 1:
        return True
    else:
        return False




