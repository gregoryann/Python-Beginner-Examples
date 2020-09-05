"""
Owofied a Sentence
Create a function that takes a sentence and turns every "i" into "wi" and "e" into "we", and add "owo" at the end.

Examples
owofied("I'm gonna ride 'til I can't no more")
➞ "I'm gonna rwidwe 'twil I can't no morwe owo"

owofied("Do you ever feel like a plastic bag")
➞ "Do you wevwer fwewel lwikwe a plastwic bag owo"

owofied("Cause baby you're a firework")
➞ "Causwe baby you'rwe a fwirwework owo"


Notes
Don't forget to return the value!
There's a space in front of owo!
uwu

"""



"""
Solution 1
"""

def owofied(sentence):
	return sentence.replace('i','wi').replace('e','we')+' owo'

"""
Solution 2
"""

def owofied(sentence):
	return ''.join('w'+c if c in 'ie' else c for c in sentence) + ' owo'


"""
Solution 3
"""

def owofied(s):
	return s.replace('i', 'wi').replace('e', 'we') + ' owo'

"""
Solution 4
"""

def owofied(sentence):
	a = {'i':'wi','e':'we'}
	sentence2 = []
	for n in [l for l in sentence]:
		if n in a:
			sentence2.append(a[n])
		else:
			sentence2.append(n)
	return "".join(sentence2)+" owo"




