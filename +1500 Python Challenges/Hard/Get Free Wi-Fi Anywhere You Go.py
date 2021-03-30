"""
Get Free Wi-Fi Anywhere You Go

A new 'hacky' phone is launched, which has the feature of connecting to any Wi-Fi network from any distance away, as long as there aren't any obstructions between the hotspot and the phone. Given a string, return how many Wi-Fi hotspots I'm able to connect to.

The phone is represented as a P.
A hotspot is represented as an *.
An obstruction is represented as a #. You cannot access a hotspot if they are behind one of these obstructions.
Examples
nonstop_hotspot("*   P  *   *") ➞ 3

nonstop_hotspot("*  * #  * P # * #") ➞ 1

nonstop_hotspot("***#P#***") ➞ 0

Notes
There will be only one phone.
No other characters, other than spaces, will appear in the tests.
"""






################################################################
"""
Solution 1
"""


import re
def nonstop_hotspot(area):
    ans = re.search(r'[* ]*P[* ]*',area)
    return ans.group().count('*')




################################################################
"""
Solution 2
"""


import re
def nonstop_hotspot(area):
	return "".join(re.findall(r"\*(?=[^#]*P)|(?<=P)[^#]*\*", area)).count("*")



################################################################
"""
Solution 3
"""


def nonstop_hotspot(area):
  area = area.replace(' ','')
  return sum(i.count('*') for i in area.split('#') if 'P' in i)






