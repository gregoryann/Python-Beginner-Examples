"""
Which Generation Are You?
Try finding your ancestors and offspring with code.

Create a function that takes a number and "m" (for male) or "f" (for female), and returns the name of an ancestor (m/f) or descendant (m/f).

If the number is negative, return the related ancestor.
If positive, return the related descendant.
You are generation 0. In the case of 0 (male or female), return "me!".
Examples
generation(2, "f") ➞ "granddaughter"

generation(-3, "m") ➞ "great grandfather"

generation(1, "f") ➞ "daughter"
Generation	Male	Female
-3	great grandfather	great grandmother
-2	grandfather	grandmother
-1	father	mother
0	me!	me!
1	son	daughter
2	grandson	granddaughter
3	great grandson	great granddaughter
Notes
Check the Resources tab for helpful hints.

"""



"""
Solution 1
"""

def generation(x, y):
    g = {
        -3: {
            'm': 'great grandfather',
            'f': 'great grandmother',
        },
        -2: {
            'm': 'grandfather',
            'f': 'grandmother',
        },
        -1: {
            'm': 'father',
            'f': 'mother',
        },
        0: {
            'm': 'me!',
            'f': 'me!',
        },
        1: {
            'm': 'son',
            'f': 'daughter',
        },
        2: {
            'm': 'grandson',
            'f': 'granddaughter',
        },
        3: {
            'm': 'great grandson',
            'f': 'great granddaughter',
        }
    }
    return g[x][y]



"""
Solution 2
"""

def generation(x, y):
	m={-3:'great grandfather',-2:'grandfather',-1:'father',0:'me!',1:'son',2:'grandson',3:'great grandson'}
	f={-3:'great grandmother',-2:'grandmother',-1:'mother',0:'me!',1:'daughter',2:'granddaughter',3:'great granddaughter'}
	return m[x] if y=='m' else f[x]

"""
Solution 3
"""

def generation(x, y):
    f = {"-3":"great grandmother","-2":"grandmother","-1":"mother","0":"me!","1":"daughter","2":"granddaughter","3":"great granddaughter"}
    m = {"-3":"great grandfather","-2":"grandfather","-1":"father","0":"me!","1":"son","2":"grandson","3":"great grandson"}
    if y=='f' :return f["{}".format(x)]
    return m["{}".format(x)]

"""
Solution 4
"""

def generation(x, y):
	g = {-3: ['great grandfather', 'great grandmother'],
			-2: ['grandfather', 'grandmother'],
			-1: ['father', 'mother'], 
			0: ['me!', 'me!'],
			1: ['son', 'daughter'],
			2: ['grandson', 'granddaughter'],
			3: ['great grandson', 'great granddaughter']}
	return g[x][y=='f']




