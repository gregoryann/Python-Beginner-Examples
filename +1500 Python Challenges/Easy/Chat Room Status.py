"""
Chat Room Status
Write a function that returns the number of users in a chatroom based on the following rules:

If there is no one, return "no one online".
If there is 1 person, return "user1 online".
If there are 2 people, return user1 and user2 online".
If there are n>2 people, return the first two names and add "and n-2 more online".
For example, if there are 5 users, return:

"user1, user2 and 3 more online"
Examples
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"
"""


"""
Solution 1
"""

def chatroom_status(users):
	if not users:
		return 'no one online'
	elif len(users)==1:
		return users[0]+' online'
	elif len(users)==2:
		return users[0]+' and '+users[1]+' online'
	else:
		return users[0]+', '+users[1]+' and '+str(len(users)-2)+' more online'


"""
Solution 2
"""

def chatroom_status(users):
	if users == []:
		return "no one online"
	a = ' and '.join(users)
	if len(users) > 2:
		a = users[0] +", " + users[1] +" and " + str(len(users)-2) + " more"
	
	return a + " online"


"""
Solution 3
"""

def chatroom_status(users):
    persons = len(users)

    if not persons:
        people = 'no one'
    elif persons == 1:
        people = '{}'.format(users[0])
    elif persons == 2:
        people = '{} and {}'.format(users[0], users[1])
    else:
        people = '{}, {} and {} more'.format(users[0], users[1], persons - 2)

    return people + ' online'







