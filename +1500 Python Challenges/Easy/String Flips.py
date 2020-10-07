"""
String Flips

Create a function that takes a string as the first argument, and a (string) specification as a second argument. If the specification is "word", return a string with each word reversed while maintaining their original order. If the specification is "sentence", reverse the order of the words in the string, while keeping the words intact.

Examples
txt = "There's never enough time to do all the nothing you want"


flip("Hello", "word") ➞ "olleH"

flip("Hello", "sentence") ➞ "Hello"

flip(txt, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"

flip(txt, "sentence") ➞ "want you nothing the all do to time enough never There's"
"""



################################################################
"""
Solution 1
"""

flip=lambda t,s:' '.join(x[::-1]for x in t.split())if s=='word'else' '.join(t.split()[::-1])





################################################################
"""
Solution 2
"""

def flip(txt, spec):
	if spec=='word': 
		return ' '.join([word[::-1] for word in txt.split(' ')])
	if spec=='sentence':	
		return ' '.join([word for word in reversed(txt.split(' '))])





################################################################
"""
Solution 3
"""

def flip(txt, spec):
	if spec=="word":
		lst2=txt.split(" ")
		for i in range(0,len(lst2)):
			lst2[i]=lst2[i][::-1]
		return ("".join(x+" " for x in lst2)).strip()
	elif spec=="sentence":
		lst2=txt.split(" ")
		lst2.reverse()
		return ("".join(x+" " for x in lst2)).strip()






#################################################################
"""
Solution 4
"""

def flip(txt, spec):

    words = txt.split()[::-1] if spec == 'sentence' \
        else [word[::-1] for word in txt.split()]

    return ' '.join(words)




#################################################################
"""
Solution 5
"""

def flip(txt, spec):
	if spec=='sentence':
		return ' '.join([c for c in txt.split()[::-1]])
	elif spec=='word':
		return ' '.join([c[::-1] for c in txt.split()])