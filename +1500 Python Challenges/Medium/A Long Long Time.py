"""
A Long Long Time

Create a function that takes three values:

h hours
m minutes
s seconds
Return the value that's the longest duration.

Examples
longest_time(1, 59, 3598) ➞ 1

longest_time(2, 300, 15000) ➞ 300

longest_time(15, 955, 59400) ➞ 59400

Notes
No two durations will be the same.
"""



################################################################
"""
Solution 1
"""


def longest_time(h, m, s):
	return [h, m, s][[h*3600, m*60, s].index(max([h*3600, m*60, s]))]



################################################################
"""
Solution 2
"""


def longest_time(h, m, s):
	return max([(h*60*60,h),(m*60,m),(s,s)],key=lambda x:x[0])[1]




################################################################
"""
Solution 3
"""


def longest_time(h, m, s):
	hour_s = (60 * h * 60)
	min_s = (60 * m)
	ans = {h:hour_s, m:min_s, s:s}
	v = sorted(ans.values())[-1]
	for i in ans:
		if ans[i] == v:
			return i





#################################################################
"""
Solution 4
"""


def longest_time(h, m, s):
    lst=[]
    lst.append(h)
    lst.append(m/60)
    lst.append(s/3600)
    if lst.index(max(lst))==0:
        return h
    elif lst.index(max(lst))==1:
        return m
    else:
        return s







#################################################################
"""
Solution 5
"""


import datetime
def longest_time(h, m, s):
	a = datetime.timedelta(hours=h)
	b = datetime.timedelta(minutes=m)
	c = datetime.timedelta(seconds=s)
	d = max([a,b,c])
	return h if d == a else m if d == b else s