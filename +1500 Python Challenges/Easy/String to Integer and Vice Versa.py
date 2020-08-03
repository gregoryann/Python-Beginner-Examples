"""

String to Integer and Vice Versa
Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.
Examples
to_int("77") ➞ 77

to_int("532") ➞ 532

to_str(77) ➞ "77"

to_str(532) ➞ "532"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""






"""
Solution 1
"""



to_int = int
to_str = str



"""
Solution 2
"""

def to_int(txt):
	return int(txt)

def to_str(num):
	return str(num)



"""
Solution 3
"""

def to_int(txt):
	try:
		out=int(txt)
	except:
		out="impossible"
	return out

def to_str(num):
	try:
		out=str(num)
	except:
		out="impossible"
	return out



"""
Solution 4
"""


txt=    37
num=    "37"

def to_int(txt):
	return int(txt)

def to_str(num):
	return str(num)

print(to_int(txt))
print(to_str(num))



