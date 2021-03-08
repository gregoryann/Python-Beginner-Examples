"""
Microwave Buttons

In microwave ovens, when buttons are pressed from 0-9, it will add that number to the microwave oven timer (starting from the left). All microwave ovens have the functionality where you can hit a "+30" button and it will add 30 seconds to the timer to cook your food. If you want to heat something for 5 mins, you can hit the "+30" button 10 times instead of thinking if there are fewer button presses that can give you the same result.

Create a function that takes an argument time and returns the shortest amount of button presses to set the given time on the microwave oven. The microwave oven timer always starts at 00:00.

Buttons
Buttons from "0-9"

# It will add that number to the microwave oven timer (starting from the left).
# If the number "5" is pressed followed by "0" twice, it will put 05:00 on the timer.
# If the number "3" is pressed followed by "0", it will put 00:30 on the timer.

Button "+30", which adds 30 seconds to the current timer.

# If the number "+30" is pressed twice, it will put 00:60 on the timer.

A "Start" button which you have to finally press to start the microwave oven.

# Remember to press this!
Examples
microwave_buttons("00:30") ➞ 2
# "+30" to put 30 seconds on the timer.
# "Start" button to start the oven.

microwave_buttons("00:70") ➞ 3
# "7" followed by "0" to put 70 seconds on the timer.
# "Start" button to start the oven.

microwave_buttons("00:00") ➞ 1
# "Start" button to start the oven.


Notes
Input may not always be what you expect (e.g. you can put in 00:70, which is valid).
No exception handling is required for this challenge.
"""



################################################################
"""
Solution 1
"""


def microwave_buttons(time):
	ts = [ int(i) for i in time.split(":") ]
	totalsec = ts[0]*60 + ts[1]
	if totalsec == 0 : 
		return 1
	if totalsec <= 60 and ts[1] <= 60 : 
		t1 = totalsec // 30 + 1 if totalsec >= 30 else len(str(totalsec)) + 1 
		t2 = len(str(totalsec)) + 1 
	else : 
		return len(time.strip(':').lstrip('0')) 
	return t1 if t1<t2 else t2



################################################################
"""
Solution 2
"""


def microwave_buttons(time):
	try:
		return ('00:00', '00:30', '01:00').index(time) + 1
	except:
		return len(time.lstrip('0'))




################################################################
"""
Solution 3
"""


microwave_buttons=lambda t:({"00:30":1,"01:00":2,"00:00":0}.get(t,len(str(int(t.replace(":",""))))))+1



#################################################################
"""
Solution 4
"""


def microwave_buttons(time):
	a, b = [int(x) for x in time.split(":")]
	a = (a * 60 + b) // 30
	return min((a if a else 10000, button(time))) + 1

def button(x):
	x=x.replace(":", "")
	for y in range(len(x)):
		if int(x[y]) > 0:
			return len(x[y:])
	return 0




#################################################################
"""
Solution 5
"""


class Microwave:

  def __init__(self, tm = '00:00'):
    
    self.mins, self.secs = [int(t) for t in tm.split(':')]

    while self.secs >= 60:
      self.mins += 1
      self.secs -= 60
    
    mins = str(self.mins)
    secs = str(self.secs)

    while len(mins) < 2:
      mins = '0' + mins
    while len(secs) < 2:
      secs = '0' + secs
    
    self.time = '{}:{}'.format(mins, secs)

  def __str__(self):
    return self.time

  def add_30(self):
    
    self.secs += 30
    while self.secs >= 60:
      self.mins += 1
      self.secs -= 60
    
    mins = str(self.mins)
    secs = str(self.secs)
    
    while len(mins) < 2:
      mins = '0' + mins
     
    while len(secs) < 2:
      secs = '0' + secs
    
    self.time = '{}:{}'.format(mins, secs)
    
    return True
  
  def input(self, inpt):
    tm = ''
    c = 0
    b_press = False
    for item in inpt:
      if item != ':':
        if b_press == False:
          if item != '0':
            b_press = True
            tm += item
            c += 1
        else:
          tm += item
          c += 1
    while len(tm) < 4:
      tm = '0' + tm
    tm = '{}:{}'.format(tm[:2], tm[2:])
    mins = int(tm[:2])
    secs = int(tm[3:])

    self.time = tm
    self.mins = mins
    self.secs = secs

    return c

  def __eq__(self, other):
    return self.time == other.time

  def __lt__(self, other):
    return (self.mins * 60 + self.secs) < (other.mins * 60 + other.secs)

def microwave_buttons(t):

  m1 = Microwave()
  m2 = Microwave()

  goal = Microwave(t)

  c1 = 0
  while m1 < goal:
    m1.add_30()
    c1 += 1
  
  if m1 == goal:
    c1valid = True
  else:
    c1valid = False
  
  c2 = m2.input(t)

  if c1valid == True:
    return min(c1, c2) + 1
  else:
    return c2 + 1
