import  psutil

print ("battery charge left: " + str(psutil.sensors_battery()[0]) + "%")

# battery charge left: 25.0%

""" If I run the above function in a desktop machine will get
TypeError: 'NoneType' object is not subscriptable
"""
# And alternative way to get the above along with
# how many minutes of charging left

import psutil as ps

batterystats = dict(ps.sensors_battery()._asdict())
print(batterystats)
timeleft = batterystats.get('secsleft')
percent = batterystats.get('percent')

print('battery percent : '+str(percent)+'%')
print('time left (secs) : '+str(timeleft)+' secs')

"""
{'percent': 25.0, 'secsleft': <BatteryTime.POWER_TIME_UNLIMITED: -2>, 'power_plugged': True}
battery percent : 25.0%
time left (secs) : 680 secs
"""