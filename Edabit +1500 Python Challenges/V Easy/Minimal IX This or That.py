"""
Minimal IX: This or That
Check the principles of minimalist code in the intro to the first challenge.

In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.

Write a function that returns the first truthy argument passed to the function. If all arguments are falsy, return the string "not found". The function will be called with a minimum of one and a maximum of four arguments: a, b, c, d.

Tips
The operator or can be used to assign or return the first truthy value among two or more elements. If no truthy value is found, the last element will be returned.

For example, the code:

def one_of_these(a, b, c):
    return a if a else b if b else c
Can be simplified to:

def one_of_these(a, b, c):
    return a or b or c
Bonus
Once a truthy value is found, the rest of the elements will not be checked. This can be used to define a sort of default value that will be returned if all of the previous elements happen to be false or empty:

txt1 = ""
txt2 = "Edabit"

txt1 or "Empty string" ➞ "Empty string"
txt2 or "Empty string" ➞ "Edabit"
Notes
This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
You can find all the exercises in this series over here.

"""


"""
Solution 1
"""

def first_one(a, b=None, c=None, d=None):
	return a or b or c or d or 'not found'

"""
Solution 2
"""

first_one=lambda*a:next((e for e in a if e),"not found")

"""
Solution 3
"""

def first_one(a, b=None, c=None, d=None):
	list= [a,b,c,d]
	for x in list:
		if bool(x) == True:
			return x
	else:
		return "not found"

"""
Solution 4
"""

def first_one(*args):
	for i in args:
		if bool(i):
			return i
	return 'not found'




