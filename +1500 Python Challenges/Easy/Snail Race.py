"""
Snail Race

Steve and Maurice have racing snails. They each have 3, a slow (s), medium (m) and fast (f) one. Although Steve's snails are all a bit stronger than Maurice's, Maurice has a trick up his sleeve. His plan is:

Round 1: [s, f] Sacrifice his slowest snail against Steve's fastest.
Round 2: [m, s] Use his middle snail against Steve's slowest.
Round 3: [f, m] Use his fastest snail against Steve's middle.
Create a function that determines whether Maurice's plan will work by outputting True if Maurice wins 2/3 games.

The function inputs:

List 1: [s, m, f] for Maurice.
List 2: [s, m, f] for Steve.
Examples
maurice_wins([3, 5, 10], [4, 7, 11]) ➞ True
# Since the matches are (3, 11), (5, 4) and (10, 7), Maurice wins 2 out of 3.

maurice_wins([6, 8, 9], [7, 12, 14]) ➞ False
# Since the matches are (6, 14), (8, 7) and (9, 12), Steve wins 2 out of 3.

maurice_wins([1, 8, 20], [2, 9, 100]) ➞ True

Notes
Maurice wins if his competing snail's speed strictly exceeds Steve's competing snail's speed.
Steve will always play in this order: [f, s, m].
"""



########################################################################






########################################################################
"""
Solution 1
"""

def maurice_wins(m_snails, s_snails):
	return m_snails[1] > s_snails[0] and m_snails[2]>s_snails[1]




########################################################################
"""
Solution 2
"""

def maurice_wins(m_snails, s_snails):
    ms, mm, mf = m_snails
    ss, sm, sf = s_snails
    
    return ms < sf and mm > ss and mf > sm





########################################################################
"""
Solution 3
"""

def maurice_wins(m, s):
	mw = 0
	if m[0] > s[2]: mw += 1
	if m[1] > s[0]: mw += 1
	if m[2] > s[1]: mw += 1
	return mw >= 2







########################################################################
"""
Solution 4
"""

def maurice_wins(m_snails, s_snails):
	m_snails.remove(min(m_snails))
	s_snails.remove(max(s_snails))

	m_wins = s_wins = 0

	for i in range(2):
		if m_snails[i] > s_snails[i]:
			m_wins += 1
		else:
			s_wins += 1
	
	return m_wins > s_wins






########################################################################
"""
Solution 5
"""


def maurice_wins(m_snails, s_snails):
	s = s_snails
	wins = [i>j for i,j in zip(m_snails,[s[2],s[0],s[1]])]
	return max(set(wins),key=wins.count)






########################################################################
"""
Solution 6
"""


def maurice_wins(m_snails, s_snails):
	m_wins = 0
	if sorted(m_snails)[0] > sorted(s_snails)[2]:
		m_wins += 1
	if sorted(m_snails)[1] > sorted(s_snails)[0]:
		m_wins += 1
	if sorted(m_snails)[2] > sorted(s_snails)[1]:
		m_wins += 1
	return m_wins >= 2