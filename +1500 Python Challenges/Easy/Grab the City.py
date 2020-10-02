"""

Grab the City

Write a function to return the city from each of these vacation spots.

Examples
grab_city("[Last Day!] Beer Festival [Munich]") ➞ "Munich"

grab_city("Cheese Factory Tour [Portland]") ➞ "Portland"

grab_city("[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]") ➞ "Kyoto"

Notes
There may be additional brackets, but the city will always be in the last bracket pair.
"""


########################################################################



"""
Solution 1
"""

def grab_city(txt):
	return txt.replace("]","").split("[")[-1]

"""
Solution 2
"""

import re
def grab_city(txt):
	return re.findall('\[.*?\]',txt)[-1][1:-1]

"""
Solution 3
"""

grab_city=lambda t:t.split('[')[-1][:-1]

"""
Solution 4
"""

import re
def grab_city(txt):
	p = re.compile('\[(.*?)\]')
	return p.findall(txt)[-1]

"""
Solution 5
"""

def grab_city(txt):
    txt = txt.split()
    if txt[-1] == 'Picchu]':
        txt = txt[-2:]
        return txt[0][1:] + ' ' + txt[1][:-1] 
    else: return ''.join([i for i in txt[-1] if i.isalpha()])
