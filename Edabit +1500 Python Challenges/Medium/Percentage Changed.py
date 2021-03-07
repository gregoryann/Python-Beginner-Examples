"""
Percentage Changed

Create a function that takes an old price old, a new price new, and returns what percent the price decreased or increased. Round the percentage to the nearest whole percent.

Examples
percentage_changed("$800", "$600") ➞ "25% decrease"

percentage_changed("$1000", "$840") ➞ "16% decrease"

percentage_changed("$100", "$950") ➞ "850% increase"
"""




################################################################
"""
Solution 1
"""


def percentage_changed(old, new):
	old = int(old[1:])
	new = int(new[1:])
	perc = int(100*new/old-100)
	return '{}% {}'.format(abs(perc), 'increase' if perc>0 else 'decrease')



################################################################
"""
Solution 2
"""


def percentage_changed(old, new):
    old, new = int(old[1:]), int(new[1:])
    return '{:.0%} {}'.format(abs(old-new)/old, 'increase' if new > old else 'decrease')




################################################################
"""
Solution 3
"""


def percentage_changed(old, new):
	x, y = int(new[1:]), int(old[1:])	
	if x/y < 1:
		return "{0}% decrease".format(int((1-x/y)*100))
	else : return "{0}% increase".format(int((x-y)/y*100))



#################################################################
"""
Solution 4
"""


def percentage_changed(old, new):
 per = 0
 old = int(old.strip("$"))
 new = int(new.strip("$"))
 dif = int(new) - int(old)
 per = int(((abs(dif))/old) * 100)
 if dif > 0:  
  return str(per) + "% increase"
 else:
  return str(per) + "% decrease"




#################################################################
"""
Solution 5
"""


def percentage_changed(old, new):
	x = int(old.strip('$'))
	y = int(new.strip('$'))
	z = int(abs((y - x) / x * 100))
	if y > x:
		return '{}% increase'.format(z)
	else:
		return '{}% decrease'.format(z)