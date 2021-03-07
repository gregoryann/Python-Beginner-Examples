"""
Emotify Sentence
Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.

word	emoticon
smile	:D
grin	:)
sad	:(
mad	:P
Examples
emotify("Make me smile") ➞ "Make me :D"

emotify("Make me grin") ➞ "Make me :)"

emotify("Make me sad") ➞ "Make me :("

Notes
The sentence always starts with "Make me".
Try to solve this without using conditional statements like if/else.
"""


########################################################################



"""
Solution 1
"""

def emotify(txt):
	sub = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
	return txt[:8] + sub[txt[8:]]


########################################################################

"""
Solution 2
"""


def emotify(txt):
	dic = {
		"smile":":D",
		"grin":":)",
		"sad":":(",
		"mad":":P"
	}
	return "Make me " + dic[txt.split(" ")[-1]]



########################################################################

"""
Solution 3
"""


def emotify(txt):
	return txt.replace('smile', ':D').replace('grin', ':)').replace('sad', ':(').replace('mad', ':P')




########################################################################


"""
Solution 4
"""


def emotify(txt):
	if txt == "Make me smile":
		return "Make me :D"
	elif txt == "Make me grin":
		return "Make me :)"
	elif txt == "Make me sad":
		return "Make me :("
	elif txt == "Make me mad":
		return "Make me :P"



########################################################################


"""
Solution 5
"""

def emotify(txt):
    obj = {"smile": ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
    txt = txt.split(' ')
    txt[-1] = obj[txt[-1]]
    return ' '.join(txt)



    