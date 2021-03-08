"""
The 3 Programmers Problem
You hired three programmers and you (hopefully) pay them. Create a function that takes three numbers (the hourly wages of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.

Examples
programmers(147, 33, 526) ➞ 493

programmers(33, 72, 74) ➞ 41

programmers(1, 5, 9) ➞ 8
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.



"""






"""
Solution 1
"""



def programmers(*args):
	return max(args) - min(args)



"""
Solution 2
"""

def programmers(one, two, three):
	lst=[one,two,three]
	return(max(lst)-min(lst))



"""
Solution 3
"""

def programmers(one, two, three):
	return max(one, two, three)-min(one, two, three)



"""
Solution 4
"""

def programmers(one, two, three):
	myDevs = [one, two, three]
	myDevs.sort()
	return myDevs[-1] - myDevs[0]





