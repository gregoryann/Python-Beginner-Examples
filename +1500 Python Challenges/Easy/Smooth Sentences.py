"""
Smooth Sentences

Carlos is a huge fan of something he calls smooth sentences. A smooth sentence is one where the last letter of each word is identical to the first letter the following word.

The following would be a smooth sentence: "Carlos swam masterfully." Since "Carlos" ends with an "s" and swam begins with an "s" and swam ends with an "m" and masterfully begins with an "m".

Create a function that determines whether the input sentence is a smooth sentence, returning a boolean value True if it is, False if it is not.

Examples
is_smooth("Marta appreciated deep perpendicular right trapezoids") ➞ True

is_smooth("Someone is outside the doorway") ➞ False

is_smooth("She eats super righteously") ➞ True
"""





################################################################
"""
Solution 1
"""

def is_smooth(sentence):
    sentence = sentence.lower().split()
    first = [first_letter[0] for first_letter in sentence]
    last = [last_letter[-1] for last_letter in sentence]
    return first[1:] == last [:-1]







################################################################
"""
Solution 2
"""

is_smooth=lambda s:all(x[-1].lower()==y[0].lower()for x,y in zip(s.split(),s.split()[1:]))







################################################################
"""
Solution 3
"""

def is_smooth(sentence):
	a=[]
	b=True
	w=0
	a=sentence.split(" ")
	if len(a)==1:
		b=False
	else:
		for w in range(len(a)-1):
			if a[w][-1].upper()!=a[w+1][0].upper():
				b=False
				break
	return b









#################################################################
"""
Solution 4
"""



def is_smooth(sentence):

    sentence = sentence.lower()

    sentence_lst = sentence.split()

    index = 0

    check = []

    while index < len(sentence_lst) - 1:

        if sentence_lst[index][-1] == sentence_lst[index + 1][0]:

            check.append('pass')

        else:

            check.append('fail')

        index = index + 1

    return 'fail' not in check




