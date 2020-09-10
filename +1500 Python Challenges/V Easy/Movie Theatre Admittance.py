"""
Movie Theatre Admittance

Write a function that checks whether a person can watch an MA15+ rated movie. One of the following two conditions is required for admittance:

The person is at least 15 years old.
They have parental supervision.
The function accepts two parameters, age and is_supervised. Return a boolean.

Examples
accept_into_movie(14, True) ➞ True

accept_into_movie(14, False) ➞ False

accept_into_movie(16, False) ➞ True

Notes
age is a decimal.
is_supervised is a boolean.

"""



"""
Solution 1
"""

def accept_into_movie(age, is_supervised):
		return age >= 15 or is_supervised



"""
Solution 2
"""

accept_into_movie = lambda a,s: int(a) > 14 or s







