"""
Letter Occurrences Per Word

Create a function that takes in a sentence and a character to find. Return a dictionary of each word in the sentence, with the number of the specified character as the value.

Examples
find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}

find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") ➞ {
  "an" : 1,
  "apple" : 1,
  "a" : 1,
  "day" : 1,
  "keeps" : 0,
  "archeologist" : 1,
  "away..." : 2
}


Notes

The function shouldn't be case sensitive.
Words in the dictionary should be in lowercase.
You may be required to find punctuation.
Duplicate words should be ignored (see example #3 for the word "an").
"""





################################################################
"""
Solution 1
"""


def find_occurrences(txt, ch):
	return {w:w.count(ch.lower()) for w in txt.lower().split()}





################################################################
"""
Solution 2
"""


find_occurrences=lambda t,c:{x:x.count(c.lower())for x in t.lower().split()}






################################################################
"""
Solution 3
"""


def find_occurrences(txt, ch):
    lst = txt.split(" ")
    output = {}
    for i in lst:
        count = 0
        for j in i:
            if j == ch.upper() or j == ch.lower():
                count += 1
        output[i.lower()] = count
        count = 0
    return output







#################################################################
"""
Solution 4
"""


def find_occurrences(txt, ch):
	d = {}
	for i in txt.lower().split():
		d[i] = i.count(ch.lower())
	return d




#################################################################
"""
Solution 5
"""


def find_occurrences(t, c):
    a = {}
    t = t.lower()
    c = c.lower()
    t = t.split( )

    for i in t:
        a[i.lower()] = i.count(c)
        
    return a