"""
A Watermelon 🍉
Mubashir is eating a watermelon.

He spits out all watermelon seeds if seeds are more than five.
He can swallow all watermelon seeds if seeds are less than five.
He can eat 1/4 of watermelon each time.
Given a 2D array of watermelon where 0 is representing juicy watermelon while 1 is representing seed, return total number of seeds spit-out. See below example for detailed explanation :

Given a watermelon :

1, 0, 0, 1, 1, 1, 0, 1
1, 0, 1, 0, 1, 1, 0, 0
1, 1, 1, 1, 0, 0, 0, 0
0, 1, 0, 1, 1, 1, 1, 0
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 0
total seeds = 0
Mubashir eats 1/4 piece (4x4 matrix) of watermelon :

x, x, x, x, 1, 1, 0, 1
x, x, x, x, 1, 1, 0, 0
x, x, x, x, 0, 0, 0, 0
x, x, x, x, 1, 1, 1, 0
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 10
total seeds = 10 (All seeds were spit-out)
Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :

x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
0, 0, 0, 1, 0, 1, 0, 0
1, 1, 1, 0, 0, 0, 1, 1
1, 0, 1, 1, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0

seeds = 8
total seeds = 10+8 = 18 (All seeds were spit-out)
Mubashir eats next 1/4 piece (4x4 matrix) of watermelon :

x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, 0, 1, 0, 0
x, x, x, x, 0, 0, 1, 1
x, x, x, x, 0, 0, 0, 0
x, x, x, x, 0, 0, 0, 0

seeds = 7
total seeds = 18+7 = 25 (All seeds were spit-out)
Mubashir eats last 1/4 piece (4x4 matrix) of watermelon :

x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x
x, x, x, x, x, x, x, x

seeds = 3
total seeds = 25+0 = 25

Examples
total_seeds(watermelon) ➞ 25
"""



#########################################################
"""
Solution 1
"""


def total_seeds(watermelon):
	h = len(watermelon)//2
	sections = [
		[sum([j for j in i[:h]]) for i in watermelon[:h]],
		[sum([j for j in i[:h]]) for i in watermelon[h:]],
		[sum([j for j in i[h:]]) for i in watermelon[:h]],
		[sum([j for j in i[h:]]) for i in watermelon[h:]]
	]
	return sum([sum(s) for s in sections if sum(s) > 5])



#########################################################
"""
Solution 2
"""


import numpy as np

def total_seeds(watermelon):
  watermelon = np.array(watermelon)
  h, w = watermelon.shape
  seeds = np.add.reduceat(np.add.reduceat(watermelon, np.arange(0, h, h // 2), axis=0), np.arange(0, w, w // 2), axis=1)
  return sum(s if s > 5 else 0 for s in seeds.ravel())




#########################################################
"""
Solution 3
"""


class Watermelon:
	class Space:
		
		def __init__(self, r, c, seed):
			self.r = r
			self.c = c
			self.s = seed
	
	q1 = lambda mr, mc: ['{},{}'.format(r, c) for r in range(mr//2) for c in range(mc//2)]
	q2 = lambda mr, mc: ['{},{}'.format(r, c) for r in range(mr//2) for c in range(mc//2, mc)]
	q3 = lambda mr, mc: ['{},{}'.format(r, c) for r in range(mr//2, mr) for c in range(mc//2)]
	q4 = lambda mr, mc: ['{},{}'.format(r, c) for r in range(mr//2, mr) for c in range(mc//2, mc)]
	
	def __init__(self, watermelon):
		self.melon = watermelon
		self.spaces = {}
		
		for r in range(len(self.melon)):
			for c in range(len(self.melon[0])):
				sid = '{},{}'.format(r, c)
				space = Watermelon.Space(r, c, self.melon[r][c])
				self.spaces[sid] = space
	
	def seeds_spit_out(self):
		
		q_1 = Watermelon.q1(len(self.melon), len(self.melon[0]))
		q_2 = Watermelon.q2(len(self.melon), len(self.melon[0]))
		q_3 = Watermelon.q3(len(self.melon), len(self.melon[0]))
		q_4 = Watermelon.q4(len(self.melon), len(self.melon[0]))
		
		spit_out = 0
		
		for quarter in [q_1, q_2, q_3, q_4]:
			seeds = 0
			for sid in quarter:
				space = self.spaces[sid]
				seeds += space.s
			if seeds > 5:
				spit_out += seeds
		
		return spit_out

def total_seeds(watermelon):
	
	wm = Watermelon(watermelon)
	
	return wm.seeds_spit_out()




#########################################################
"""
Solution 4
"""


def total_seeds(watermelon):
    l,l1 = watermelon[:4],watermelon[4:]
    p1,p2 = sum(list(map(lambda x:x[:4],l)),[]).count(1),sum(list(map(lambda x:x[4:],l)),[]).count(1)
    p3,p4 = sum(list(map(lambda x:x[:4],l1)),[]).count(1),sum(list(map(lambda x:x[4:],l1)),[]).count(1)
    return sum(list(filter(lambda x:x>5,[p1,p2,p3,p4])))




