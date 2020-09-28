"""
Fix the Spacing

Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.

Examples
correct_spacing("The film   starts       at      midnight. ")
➞ "The film starts at midnight."

correct_spacing("The     waves were crashing  on the     shore.   ")
➞ "The waves were crashing on the shore."

correct_spacing(" Always look on    the bright   side of  life.")
➞ "Always look on the bright side of life."
"""





#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def correct_spacing(sentence):
    return ' '.join(sentence.split())

"""
Solution 2
"""

correct_spacing=lambda s:' '.join(s.split())

"""
Solution 3
"""

def correct_spacing(sentence):
    words = sentence.split()
    new_sentence = ''
    for word in words:
        if word is words[-1]:
            new_sentence += word
        else:
            new_sentence += word + ' '
    return new_sentence


"""
Solution 4
"""

def correct_spacing(sentence):
	l = sentence.split(' ')
	m = []
	for i in range(len(l)):
		if l[i] != '':
			m.append(l[i])
	return ' '.join(m)




