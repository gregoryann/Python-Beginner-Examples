"""
Video Length in Seconds
You are given the length of a video in minutes. The format is mm:ss (e.g.: "02:54"). Create a function that takes the video length and return it in seconds.

Examples
minutes_to_seconds("01:00") ➞ 60

minutes_to_seconds("13:56") ➞ 836

minutes_to_seconds("10:60") ➞ False

Notes
The video length is given as a string.
If the number of seconds is 60 or over, return False (see example #3).
You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################






"""
Solution 1
"""

def minutes_to_seconds(time):
	m, s = map(int, time.split(':'))
	return False if s >= 60 else m*60 + s

"""
Solution 2
"""

def minutes_to_seconds(time):
    l = time.split(":")
    return int(l[1])+int(l[0])*60 if int(l[1]) < 60 else False

"""
Solution 3
"""

def minutes_to_seconds(time):
	n = time.split(':')
	s = int(n[0])*60
	if int(n[1]) >= 60:
		return False
	else:
		return s + int(n[1])

"""
Solution 4
"""

def minutes_to_seconds(time):
	if int(time.split(":")[1]) >= 60:
		return False
	mins = int(time.split(":")[0]) * 60
	seconds = int(time.split(":")[1])
	return mins + seconds



