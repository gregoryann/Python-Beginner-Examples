"""
Reverse Words in a String

Given an input string, reverse the string word by word.

Examples
reverse_words("the sky is blue") ➞ "blue is sky the"

reverse_words("  hello world!  ") ➞ "world! hello"

reverse_words("a good   example") ➞ "example good a"

Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
Try to solve this in linear time.
"""



################################################################
"""
Solution 1
"""


def reverse_words(words):
	return ' '.join(list(filter(None, words.split()))[::-1])



################################################################
"""
Solution 2
"""


def reverse_words(words):
	a = words.strip()
	b = a.split(' ')
	return ' '.join(b[::-1])



################################################################
"""
Solution 3
"""


reverse_words=lambda w:' '.join(w.split()[::-1])



#################################################################
"""
Solution 4
"""


def reverse_words(words):
    words = words.lstrip()
    words = words.rstrip()
    split = words.split(" ")
    finalstring = ""
    firstword = split[0]
    index = 1
    reverser = True
    stringmaker = True
    while reverser == True:
        if split[-1] == firstword:
            reverser = False
        else:
            split.insert(0, split[index])
            index += 1
            del split[index]
    while stringmaker == True:
        if not split:
            finalstring = finalstring.lstrip()
            finalstring = finalstring.rstrip()
            stringmaker = False
        else:
            finalstring += split[0] + " "
            del split[0]
    return finalstring




