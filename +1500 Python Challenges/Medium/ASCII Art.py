"""
ASCII Art!
Given a very long string of ASCII characters, split the string up into equal sized groups of size width. To properly display the image, join up the groups with the newline character \n and return the output string.

See the miniature examples below for clarity!

Examples
format_ascii("0123456789", 2) ➞ "01\n23\n45\n67\n89"

format_ascii("................................", 8) ➞ "........\n........\n........\n........"

format_ascii("^^^^^^^^", 1) ➞ "^\n^\n^\n^\n^\n^\n^\n^"

Notes
Enjoy the (somewhat oversized) art in the Tests tab.
"""



################################################################
"""
Solution 1
"""


import re

def format_ascii(txt, width):
	return '\n'.join(re.findall('.'*width, txt))



################################################################
"""
Solution 2
"""


def format_ascii(txt, width):
    x=[txt[i:i+width] for i in range(0, len(txt), width)]
    for i in range(len(x)*2-1):
        if i%2!=0:
            x.insert(i,'\n')
    return ''.join(x)



################################################################
"""
Solution 3
"""


format_ascii=lambda t,w:'\n'.join([t[i:i+w]for i in range(0,len(t),w)])



#################################################################
"""
Solution 4
"""


import re
format_ascii=lambda t,w:'\n'.join(re.findall('.{'+str(w)+'}',t))




