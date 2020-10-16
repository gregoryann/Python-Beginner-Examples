"""
International Greetings

Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
Write a function that takes in a name and returns a name tag, that should read:

"Hi! I'm [name], and I'm from [country]."
If the name is not in the dictionary, return:

"Hi! I'm a guest."

Examples
greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."

greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."

greeting("Monti") ➞ "Hi! I'm a guest."
"""



################################################################
"""
Solution 1
"""

GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}

def greeting(name):
	return "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name]) if name in GUEST_LIST.keys() else "Hi! I'm a guest."




################################################################
"""
Solution 2
"""


GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}

def greeting(name):
      return "Hi! I\'m a guest." if name not in GUEST_LIST else  "".join("Hi! I\'m "+ name + ", and I\'m from " + GUEST_LIST[name]+".")





################################################################
"""
Solution 3
"""

GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}

def greeting(name):
		if name in GUEST_LIST.keys():
				return "Hi! I'm {}, and I'm from {}.".format(name,GUEST_LIST[name])
		else:
				return "Hi! I'm a guest."







