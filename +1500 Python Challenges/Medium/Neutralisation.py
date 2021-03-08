"""
Neutralisation

Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
Examples
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"

Notes
The two strings will be the same length.
"""



################################################################
"""
Solution 1
"""


def neutralise(s1, s2):
		return ''.join(a if a == b else '0' for a, b in zip(s1, s2))



################################################################
"""
Solution 2
"""


def neutralise(s1, s2):
  return ''.join('0' if i.count('+') == 1 else i[0] for i in zip(s1, s2))



  

################################################################
"""
Solution 3
"""


def neutralise(s1, s2):
	results = {"++": "+", "--": "-", "+-": "0", "-+": "0"}
	return "".join(results[x + y] for x, y in zip(s1, s2))






#################################################################
"""
Solution 4
"""


def neutralise(s1, s2):
	d = { "++":"+", 
          "--":"-", 
          "+-":"0", 
          "-+":"0"}
	return "".join([d.get(s1[i]+s2[i]) for i in range(len(s1))])



