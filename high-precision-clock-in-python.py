'''
I need to print a message right at 08:00:00.000000. Hence, I tried to get the current time of my system with microsecond precision. To do so, I used datetime.datetime.now(). But, I found something weird, that made me think it is not that accurate. When I run the following code on a system with Intel (R) Corei7-8550U CPU @ 1.80GHz 1.99GHz and Windows 10:
 '''
import datetime
import time

x = datetime.datetime.now()
t=2**10000
y = datetime.datetime.now()
print(x, '\n', y)

'''
Will give you  get exact same times, e.g.:
2020-07-13 02:28:28.763578
2020-07-13 02:28:28.763602
So to resolve the above lack of precision, we can depend onf time.time_ns() -
 which was introduced in Python 3.7 as new functions to the time module providing higher resolution:
https://docs.python.org/3/library/time.html - Similar to time() but returns time as an integer number of nanoseconds since the epoch.
'''

time1 = time.time_ns()
print(time1)
# 1530228533161016309

time2 = time.time_ns() / (10 ** 9)
# The above will convert to floating-point seconds
print(time2)
# 1530228544.0792289