"""
Is it Time for Milk and Cookies?

Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.

Examples
time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True

time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False

time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True

Notes
All test cases contain valid dates.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""
def time_for_milk_and_cookies(date):
	return "12-24" in str(date)

"""
Solution 2
"""

time_for_milk_and_cookies=lambda d:True if str(d)[5:7]=='12'and str(d)[8:]=='24'else False





