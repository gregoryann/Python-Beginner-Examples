"""
Reverse the Odd Length Words
Given a string, reverse all the words which have odd length. The even length words are not changed.

Examples
reverse_odd("Bananas") ➞ "sananaB"

reverse_odd("One two three four") ➞ "enO owt eerht four"

reverse_odd("Make sure uoy only esrever sdrow of ddo length")
➞ "Make sure you only reverse words of odd length"

Notes
There is exactly one space between each word and no punctuation is used.
"""



################################################################
"""
Solution 1
"""


def reverse_odd(txt):
	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())



################################################################
"""
Solution 2
"""


def reverse_odd(txt):
	temp = list(txt.split(' '))
	for i in range(len(temp)):
		if len(temp[i]) % 2 == 1:
			temp[i] = temp[i][::-1]
	return ' '.join(temp)


################################################################
"""
Solution 3
"""


def reverse_odd(txt):
    new_txt = []
    for word in txt.split(' '):
        if len(word) % 2 != 0:
            word = list(reversed(word))
            new_txt.append("".join(word))
        else:
            new_txt.append(word)
    return " ".join(new_txt)



#################################################################
"""
Solution 4
"""


reverse_odd = lambda txt: ' '.join([w[::-1 if len(w)%2 else 1] for w in txt.split()])



