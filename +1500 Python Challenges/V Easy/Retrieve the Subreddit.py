"""
Retrieve the Subreddit
Create a function to extract the name of the subreddit from its URL.

Examples
sub_reddit("https://www.reddit.com/r/funny/") ➞ "funny"

sub_reddit("https://www.reddit.com/r/relationships/") ➞ "relationships"

sub_reddit("https://www.reddit.com/r/mildlyinteresting/") ➞ "mildlyinteresting"
"""



"""
Solution 1
"""

def sub_reddit(link):
  return link.split("/")[-2]

"""
Solution 2
"""

def sub_reddit(link):
	import re
	r = re.findall(r'/r/(.*)/',link)
	return r[0]

"""
Solution 3
"""

def sub_reddit(link):
	x = (link.index('/r/'))
	return (link[x+3:-1])

"""
Solution 4
"""

def sub_reddit(link):

    link = link.split("/")

    sub = link[-2]

    return "".join(sub)




