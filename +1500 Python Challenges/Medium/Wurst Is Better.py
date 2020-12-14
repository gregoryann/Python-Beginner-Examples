"""
Wurst Is Better

Wurst is the best. Create a function that takes a string and replaces every mention of any type of sausage with the German word "Wurst," unless—of course—the sausage is already a type of German "Wurst" (i.e. "Bratwurst", see below), then leave the sausage name unchanged.

German Wursts	Convert to Wurst
Bratwurst	Kielbasa
Kochwurst	Chorizo
Leberwurst	Moronga
Mettwurst	Salami
Rostbratwurst	Sausage
~	Andouille
~	Naem
~	Merguez
~	Gurka
~	Snorkers
~	Pepperoni
Rules
Append sausages from the "Convert to Wurst" column with "wurst".
Do not replace any German sausage with the word "Wurst".
The word "Wurst" must be title case.
Examples
wurst_is_better("I like chorizos, but not sausages") ➞ "I like Wursts, but not Wursts"

wurst_is_better("sich die Wurst vom Brot nehmen lassen") ➞ "sich die Wurst vom Brot nehmen lassen"

wurst_is_better("Bratwurst and Rostbratwurst are sausages") ➞ "Bratwurst and Rostbratwurst are Wursts"


Notes
All German sausage names contain the word "wurst".
"""



################################################################
"""
Solution 1
"""


import re
pattern = re.compile('|'.join(['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']), re.IGNORECASE)
def wurst_is_better(txt):
  return pattern.sub('Wurst', txt)



################################################################
"""
Solution 2
"""


import re
wurst_is_better=lambda t:re.sub('kielbasa|chorizo|moronga|salami|sausage|andouille|naem|merguez|gurka|snorkers|pepperoni|Kielbasa|Chorizo|Moronga|Salami|Sausage|Andouille|Naem|Merguez|Gurka|Snorkers|Pepperoni','Wurst',t)



################################################################
"""
Solution 3
"""


def wurst_is_better(txt):
	sausages = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille', 'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']
	for i in sausages:
		txt = txt.replace(i,"Wurst")
		txt = txt.replace(i.capitalize(),"Wurst")
	return txt



#################################################################
"""
Solution 4
"""


def wurst_is_better(txt):
	lst = txt.split(" ")
	saulst = ["kielbasa", "chorizo", "moronga", "salami", "sausage", "andouille", "naem", "merguez", "gurka", "snorkers", "pepperoni"]
	for i, x in enumerate(lst):
		if(saulst.count(x.lower())==1):
			lst[i] = "Wurst"
	return ' '.join(lst)



#################################################################
"""
Solution 5
"""


import re

def wurst_is_better(txt):
	all = re.findall(r"Kielbasa|Chorizo|Moronga|Salami|Sausage|Andouille|Naem|Merguez|Gurka|Snorkers|Pepperoni", txt, re.I)
	for item in all:
		txt = txt.replace(item, "Wurst")
	return txt