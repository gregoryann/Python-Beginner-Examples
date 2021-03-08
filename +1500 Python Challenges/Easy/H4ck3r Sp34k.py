"""
H4ck3r Sp34k

Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"

Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.
"""


################################################################





################################################################
"""
Solution 1
"""

def hacker_speak(txt):
	return txt.translate(str.maketrans('aeios', '43105'))




################################################################
"""
Solution 2
"""

def hacker_speak(txt):
	return txt.translate({ord(i): v for i, v in zip('aeios', '43105')})




################################################################
"""
Solution 3
"""


def hacker_speak(txt):
	hack = {'a': '4', 'e':'3', 'i':'1', 'o':'0','s':'5'}
	
	new_str = ''
	
	for ch in txt:
		if ch in hack:
			new_str += hack[ch]
		else:
			new_str += ch
	return new_str






################################################################
"""
Solution 4
"""

hacker_speak=lambda t:t.translate(str.maketrans('aeios','43105'))







################################################################
"""
Solution 5
"""


def hacker_speak(txt):
	d = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5'}
	s = list(txt)
	for i in range(len(s)):
			e = s[i]
			e = d.get(e.lower(), e)
			s[i] = e
	return ''.join(s)