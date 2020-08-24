"""
The Study of Wumbology
Create a function that flips M's to W's (all uppercase).

Examples
wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"

wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"

wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"

"""


"""
Solution 1
"""

def wumbo(words):
	return words.replace('M', 'W')


"""
Solution 2
"""

def wumbo(words):
	return ''.join([i if i != 'M' else 'W' for i in words])

"""
Solution 3
"""

wumbo = lambda words: words.replace('M', 'W')

"""
Solution 4
"""

def wumbo(words):
	replacedLetters  = "MW";
	converted_lst =  [ "W"  if (letter == "M")  else letter for letter in words];
	return "".join(converted_lst);


"""
Solution 5
"""


def wumbo(words):
    new_words = ""
    for i in words:
        if i == 'M':
            new_words += 'W'
        else:
            new_words += i
    return(new_words)

