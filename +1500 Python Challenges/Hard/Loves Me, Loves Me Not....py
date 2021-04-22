"""
Loves Me, Loves Me Not...

"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"


Notes
Remember to return a string.
The first phrase is always "Loves me".
"""




################################################################
"""
Solution 1
"""


def loves_me(n):
    arr = (['Loves me', 'Loves me not']*n)[:n]
    arr[-1] = arr[-1].upper()
    return ', '.join(arr)




################################################################
"""
Solution 2
"""


def loves_me(n):
	s = list()
	for x in range(n):
		s.append(['Loves me not','Loves me'][x%2==0])
	s[-1] = s[-1].upper()
	return ', '.join(s)



################################################################
"""
Solution 3
"""


def loves_me(n):
    a = "Loves me" 
    b = "Loves me not"
    if n==1:
        return "LOVES ME"
    else:
        return ', '.join([a if i%2==0 else b for i in range(n-1)])+ ', ' +[a if i%2==0 else b for i in range(n)][-1].upper()







