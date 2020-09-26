"""
Reverse Words Starting With a Particular Letter

Write a function that reverses all the words in a sentence that start with a particular letter.

Examples
special_reverse("word searches are super fun", "s")
➞ "word sehcraes are repus fun"

special_reverse("first man to walk on the moon", "m")
➞ "first nam to walk on the noom"

special_reverse("peter piper picked pickled peppers", "p")
➞ "retep repip dekcip delkcip sreppep"

Notes
Reverse the words themselves, not the entire sentence.
All characters in the sentence will be in lower case.
"""



"""
Solution 1
"""

def special_reverse(s, c):
  return ' '.join(i[::-1] if i[0]==c else i for i in s.split())

"""
Solution 2
"""

def special_reverse(s, c):
	s = s.split()
	return ' '.join(word[::-1] if word.startswith(c) else word for word in s)

"""
Solution 3
"""

special_reverse=lambda s,c:" ".join([w[::1-2*(w[0]==c)]for w in s.split()])

"""
Solution 4
"""

def special_reverse(s, c):
	l = s.split()
	for i in range(len(l)):
		if l[i][0] == c:
			l[i] = l[i][::-1]
	s = " ".join(l)
	return s




