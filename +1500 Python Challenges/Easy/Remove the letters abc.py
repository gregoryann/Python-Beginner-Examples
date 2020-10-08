"""
Remove the letters abc

Create a function that will remove the letters a, b and c from the words. If the word has no a, b, c letters, return None

Examples
remove_abc("This might be a bit hard") ➞ This might e  it hrd

remove_abc("hello world!") ➞  None

remove_abc("") ➞ None

Notes
Don't forget to use return.
"""



################################################################
"""
Solution 1
"""

import re
def remove_abc(t):
	s=re.sub('[abc]','',t)
	return None if s==t else s






################################################################
"""
Solution 2
"""

from typing import Union


def remove_abc(txt: str) -> Union[str, None]:
	if 'a' in txt or 'b' in txt or 'c' in txt:
		return txt.replace('a', '').replace('b', '').replace('c', '')
	return None





################################################################
"""
Solution 3
"""

letters = "abc"
def remove_abc(txt):
  a = "".join([i for i in txt if i not in letters])
  return None if len(a)  == len(txt) else a







#################################################################
"""
Solution 4
"""

def remove_abc(txt):
		return None if "a" not in txt and "b" not in txt and "c" not in txt else txt.replace("a","",txt.count("a")).replace("b","",txt.count("b")).replace("c","",txt.count("c"))




