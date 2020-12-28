"""
Imaginary Coding Interview


Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.
The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.

Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.


Notes
Try to solve the problem using only list methods.
"""




################################################################
"""
Solution 1
"""


def interview(lst, tot):
	meh = [5,5,10,10,15,15,20,20]
	return 'qualified' if all(a<=b for a,b in zip(lst,meh)) and tot<=120 and len(lst)==8 else 'disqualified'




################################################################
"""
Solution 2
"""


def interview(lst, tot):
	key=[5, 5, 10, 10, 15, 15, 20, 20]
	if tot>120 or len(lst)<8:
		return "disqualified"
	while len(lst)>0:
		if lst.pop()>key.pop():
			return "disqualified"
	return "qualified"




################################################################
"""
Solution 3
"""


def interview(lst, tot):
	return "{}qualified".format(["dis",""][all([all(x<=y for x,y in  \
		zip(lst, [5,5,10,10,15,15,20,20])), len(lst)==8, tot<=120])])




################################################################
"""
Solution 4
"""



def interview(times, total):
    fmt = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
    maxtimes = {
        "very easy": 5,
        "easy": 10,
        "medium": 15,
        "hard": 20
    }

    asserts = [not t > maxtimes[i] for t, i in zip(times, fmt)]

    if total <= 120 and all(asserts) and len(times) == len(fmt):
        return "qualified"
    return "disqualified"





################################################################
"""
Solution 5
"""


def interview(lst, tot):
	
	class Test:
		
		very_easy = 5
		easy = 10
		medium = 15
		hard = 20
		
		def __init__(self, questions):
			self.q = questions
		
		def check_time(self, quid, time):
			if self.q[quid] == 'VE':
				goal = Test.very_easy
			elif self.q[quid] == 'E':
				goal = Test.easy
			elif self.q[quid] == 'M':
				goal = Test.medium
			else:
				goal = Test.hard
			
			return time <= goal
		
		def check_total(self, time):
			return time <= 120
	
	if len(lst) < 8 or tot > 120:
		return 'disqualified'
	test = Test('VE,VE,E,E,M,M,H,H'.split(','))
	
	for n in range(len(lst)):
		if test.check_time(n, lst[n]) == False:
			return 'disqualified'
	
	if test.check_total(tot) == False:
		return 'disqualified'
	else:
		return 'qualified'