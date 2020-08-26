"""
Scoring System
Andy, Ben and Charlotte are playing a board game. The three of them decided to come up with a new scoring system. A player's first initial ("A", "B" or "C") denotes that player scoring a single point. Given a string of capital letters, return a list of the players' scores.

For instance, if ABBACCCCAC is written when the game is over, then Andy scored 3 points, Ben scored 2 points, and Charlotte scored 5 points, since there are 3 instances of letter A, 2 instances of letter B, and 5 instances of letter C. So the list [3, 2, 5] should be returned.

Examples
calculate_scores("A") ➞ [1, 0, 0]

calculate_scores("ABC") ➞ [1, 1, 1]

calculate_scores("ABCBACC") ➞ [2, 2, 3]
Notes
If given an empty string as an input, return [0, 0, 0].

"""






"""
Solution 1
"""

def calculate_scores(txt):
	return [txt.count(x) for x in 'ABC']


"""
Solution 2
"""
def calculate_scores(txt):
    return [txt.count('A'),txt.count('B'),txt.count('C')]

"""
Solution 3
"""

def calculate_scores(txt):
	a = txt.count('A')
	b = txt.count('B')
	c = txt.count('C')
	
	return [a,b,c]

"""
Solution 4
"""

def calculate_scores(txt):
    count = 0
    count1 = 0
    count2 = 0
    for char in txt:
        if (char=='A'): 
            count += 1
        elif (char=='B'):
            count1 += 1
        else:
            count2 += 1
    return [count,count1,count2]

"""
Solution 5
"""

def calculate_scores(txt):
	new = [0, 0, 0]
	new[0] = txt.count("A")
	new[1] = txt.count("B")
	new[2] = txt.count("C")
	return new

