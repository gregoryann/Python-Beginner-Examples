"""
Musical Cadences

In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two chords at the end of a phrase. The different cadences are as follows:

V followed by I is a Perfect Cadence
IV followed by I is a Plagal Cadence
V followed by Any chord other than I is an Interrupted Cadence
Any chord followed by V is an Imperfect Cadence
Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.

Examples
find_cadence(["I", "IV", "V"]) ➞ "imperfect"

find_cadence(["ii", "V", "I"]) ➞ "perfect"

find_cadence(["I", "IV", "I", "V", "vi"]) ➞ "interrupted"

Notes
Return strings all in lowercase.
Only focus on the last two chords of a progression.
Return "no cadence" if none of the criterea match up.
I is a capital i not a lowercase L.
"""



################################################################
"""
Solution 1
"""


def find_cadence(chords):
    if chords[-2] == 'V':
        return 'perfect' if chords[-1] == 'I' else 'interrupted'
    if chords[-2:] == ['IV', 'I']:
        return 'plagal'
    if chords[-1] == 'V':
        return 'imperfect'
    return 'no cadence'



################################################################
"""
Solution 2
"""

p="perfect"
find_cadence=lambda c:{"IVV":"im"+p,"IVI":"plagal","VI":p}.get(c[-2]+c[-1],"innot ecrarduepntceed"[c[-2]!="V"::2])


################################################################
"""
Solution 3
"""

def find_cadence(chords):
	pu, ul = chords[-2:]
	if (pu, ul) == ('V', 'I'): return 'perfect'
	if (pu, ul) == ('IV', 'I'): return 'plagal'
	if pu == 'V': return 'interrupted'
	if ul == 'V': return 'imperfect'
	return 'no cadence'



#################################################################
"""
Solution 4
"""


def find_cadence(chords):
	if chords[-2:] == ["V", "I"]: return "perfect"
	if chords[-2:] == ["IV", "I"]: return "plagal"
	if chords[-2] == "V": return "interrupted"
	if chords[-1] == "V": return "imperfect"
	return "no cadence"




#################################################################
"""
Solution 5
"""


def find_cadence(chords):
	a, b = [chord.upper() for chord in chords][-2:]
	if a == "V" and b == "I":
		return "perfect"
	elif b == "V":
		return "imperfect"
	elif a == "V" and b != "I":
		return "interrupted"
	elif a == "IV" and b == "I":
		return "plagal"
	else:
		return "no cadence"