"""
Find the Index
Create a function that takes a list and a string as arguments and return the index of the string.

Examples
find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2

find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1

find_index(["a", "g", "y", "d"], "d") ➞ 3

find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0
Notes
Don't forget to return the result.
If you are stuck, find help in the Resources tab.
The variable for list is lst, not 1st.

"""



"""
Solution 1
"""

def find_index(lst, str):
	return lst.index(str)
    
"""
Solution 2
"""

def find_index(lst, str):
    for i, x in enumerate(lst):
        if x == str:
            break
    return i

"""
Solution 3
"""

def find_index(lst, str):
	resp = 0
	for len in lst:
		if len == str:
			return resp
		resp = resp + 1

"""
Solution 4
"""

def find_index(lst, txt):
	lstLen = len(lst)
	for i in range(lstLen):
		if lst[i] == txt:
			return i



"""
Solution 5
"""

# Find the Index
def find_index(List,Index_Variable):
    return List.index(Index_Variable)
print(find_index(["hi","edabit","fgh","abc"],"fgh"))


"""
Solution 5
"""

def find_index(lst, str):
	k = 0
	for i in lst:
		if i == str:
			return k
		else:
			k = k+1
	return	-1

