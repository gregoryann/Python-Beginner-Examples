"""
Convert Kilometers to Miles
In this challenge, you have to implement a function that returns the given distance kilometers converted into miles. You have to round the result up to the fifth decimal digit.

Examples
km_to_miles(2) ➞ 1.24274

km_to_miles(6) ➞ 3.72823

km_to_miles(8) ➞ 4.97097
Notes
1 kilometer = 0.62137 miles.

"""



"""
Solution 1
"""

def km_to_miles(km):
	return round(km*0.621371,5)

"""
Solution 2
"""

def km_to_miles(kilometers):
	miles_conversion_ratio = 0.621371
	miles = kilometers * miles_conversion_ratio
	return round(miles, 5 )

"""
Solution 3
"""

km_to_miles = lambda k: round(k * 0.621371, 5)








