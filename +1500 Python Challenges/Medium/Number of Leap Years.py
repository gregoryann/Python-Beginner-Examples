"""
Number of Leap Years

Given a range of years as a string, return the number of leap years there are within the range (inclusive).

Examples
num_of_leapyears("1980-1984") ➞ 2
# 1980 and 1984 are leapyears.

num_of_leapyears("2000-2020") ➞ 6

num_of_leapyears("1600-2000") ➞ 98

Notes
Remember that a hyphen separates the years.
Check the Resources tab for help on checking whether a year is a leap year.
"""




################################################################
"""
Solution 1
"""


from calendar import isleap

def num_of_leapyears(years):
	start, end = map(int, years.split('-'))
	return sum(isleap(year) for year in range(start, end+1))



################################################################
"""
Solution 2
"""


def num_of_leapyears(years):
	yrs = years.split('-')

	cnt = 0
	for i in range (int(yrs[0]), int(yrs[1]) + 1):
			if((i % 4 == 0) and ((i%400==0) or (i%100 != 0))):
					cnt+=1

	return cnt


################################################################
"""
Solution 3
"""


def leap_year(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%4==0 and year%400==0:
        return True
    else:
        return False
    
def num_of_leapyears(years):
    years = years.replace("-",",")
    lst_years = list(eval("range({})" .format(years)))
    lst_years = lst_years+[lst_years[-1]+1]
    return [leap_year(y) for y in lst_years].count(True)



#################################################################
"""
Solution 4
"""


def num_of_leapyears(years):
	f, l = map(int, years.split('-'))
	is_lp = lambda y: y % 400 == 0 or y % 100 != 0 and y % 4 == 0
	
	return sum(is_lp(i) for i in range(f, l+1))



