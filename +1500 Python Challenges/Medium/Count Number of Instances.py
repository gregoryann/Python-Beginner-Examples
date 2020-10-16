"""
Count Number of Instances

Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"

Notes
Feel free to check out the resources provided in the Resources tab for some helpful information on Python classes!
"""





################################################################
"""
Solution 1
"""


class User:
	user_count=0
	def __init__(self,u):
		self.username = u 
		User.user_count+=1




################################################################
"""
Solution 2
"""


class User:

    users = []
    user_count = 0
    
    def __init__(self, username):
        self.username = username
        User.users.append(username)
        User.user_count = len(User.users)




################################################################
"""
Solution 3
"""

class User:
	user_count = 0
	def __init__(self, username):
		self.username = username
		User.user_count += 1
	def username(self):
		return self.username







