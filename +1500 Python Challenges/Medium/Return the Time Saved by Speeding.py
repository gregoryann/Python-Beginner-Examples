"""
Return the Time Saved by Speeding

One cause for speeding is the desire to shorten the time spent traveling. In long distance trips speeding does save an appreciable amount of time. However, the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.

Examples
# The parameter's format is as follows:
# (speed limit, avg speed, distance traveled at avg speed)

time_saved(80, 90, 40) ➞ 3.3

time_saved(80, 90, 4000) ➞ 333.3

time_saved(80, 100, 40 ) ➞ 6.0

time_saved(80, 100, 10) ➞ 1.5

Notes
Speed = distance/time
The time returned should be in minutes, not hours.
The unit of speed is assumed to be miles per hour (mph).
"""




################################################################
"""
Solution 1
"""


def time_saved(lim, avg, d):
	return round((d/lim - d/avg)*60, 1)





################################################################
"""
Solution 2
"""


#def time_saved(s_lim, s_avg, d):
def time_saved(s_lim, s_avg, d):
    norm_time = (d / s_lim) * 60
    fast_time = (d / s_avg) * 60
    worth = norm_time - fast_time
    return round(worth, 1)





################################################################
"""
Solution 3
"""


time_saved=lambda s,r,d:round(60*d*(1/s-1/r),1)




#################################################################
"""
Solution 4
"""


def time_saved(s_lim, s_avg, d):
	slower_speed_time_minutes  = d/s_lim * 60;
	faster_speed_time_minutes  = d/s_avg * 60;
	speed_difference  = slower_speed_time_minutes - faster_speed_time_minutes;
	return round(speed_difference , 1);



