"""
Coding Website Score Calculator
Imagine you run a website that presents users with different coding challenges in levels Easy, Medium, and Hard, where users get points for completing challenges. An Easy challenge is worth 5 points, a Medium challenge is worth 10 points, and a Hard challenge is worth 20 points.

Create a function that takes in the number of each challenge level a user has played and calculates the user's total number of points. Keep in mind that a user cannot complete negative challenges, so the function should return the string "invalid" if any of the passed parameters are negative.

Examples
score_calculator(1, 2, 3) ➞ 85

score_calculator(1, 0, 10) ➞ 205

score_calculator(5, 2, -6) ➞ "invalid"

"""



"""
Solution 1
"""

def score_calculator(easy, med, hard):
	if easy < 0 or med < 0 or hard < 0:
		return "invalid"
	else:
		return easy * 5 + med * 10 + hard * 20

"""
Solution 2
"""

def score_calculator(e, m, h):
  return "invalid" if min([e,m,h]) < 0 else e * 5 + m * 10 + h * 20


"""
Solution 3
"""

def score_calculator(easy, med, hard):
	return 'invalid' if any([i<0 for i in [easy,med,hard]]) else (5*easy)+(10*med)+(20*hard)

"""
Solution 4
"""

def score_calculator(easy, med, hard):
	totEasy = easy * 5
	totMed = med * 10
	totHard = hard * 20
	if easy < 0 or med < 0 or hard < 0:
		return "invalid"
	sum = totEasy + totMed + totHard
	return sum





