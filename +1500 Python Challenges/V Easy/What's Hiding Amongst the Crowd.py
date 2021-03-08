"""
What's Hiding Amongst the Crowd?
A word is on the loose and now has tried to hide amongst a crowd of tall letters! Help write a function to detect what the word is, knowing the following rules:

The wanted word is in lowercase.
The crowd of letters is all in uppercase.
Note that the word will be spread out amongst the random letters, but their letters remain in the same order.

Examples

detect_word("UcUNFYGaFYFYGtNUH") ➞ "cat"
detect_word("bEEFGBuFBRrHgUHlNFYaYr") ➞ "burglar"
detect_word("YFemHUFBbezFBYzFBYLleGBYEFGBMENTment") ➞ "embezzlement"

"""


"""
Solution 1
"""

def detect_word(txt):
	return "".join(c for c in txt if c.islower())

"""
Solution 2
"""

def detect_word(b):
    a = ("")
    for i in b:
        if i.islower() == True:
            a = a + i 
    return a
print (detect_word("DDaArRRRRi"))

"""
Solution 3
"""
def detect_word(txt):
	
	# Convert to List
	List = list(txt)
	
	# Beginning and End of List
	Counter = 0
	Length = len(List)
	
	# Bucket for Mystery Word
	Mystery_Word = ""
	
	# Finding Lower Case Letters
	
	while (Counter < Length):
		
		if (List[Counter].islower()):
			Mystery_Word = Mystery_Word + List[Counter]
			Counter +=1
		
		else:
			Counter +=1	
		
	# Giving Answer
	return Mystery_Word



"""
Solution 4
"""

def detect_word(txt):
    word = []
    for i in txt:
        if i.islower():
            word.append(i)
    return ''.join(word)


"""
Solution 5
"""

def detect_word(txt):
	word = ""
	i = 0
	while(i < len(txt)):
		if(txt[i:i+1].islower()):
			word += txt[i:i+1]
		i += 1
	else:
		return word