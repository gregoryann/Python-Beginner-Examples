"""
Upvotes vs Downvotes
Given a dictionary containing counts of both upvotes and downvotes, return what vote count should be displayed. This is calculated by subtracting the number of downvotes from upvotes.

Examples
get_vote_count({ "upvotes": 13, "downvotes": 0 }) ➞ 13

get_vote_count({ "upvotes": 2, "downvotes": 33 }) ➞ -31

get_vote_count({ "upvotes": 132, "downvotes": 132 }) ➞ 0
Notes
You can expect only positive integers for vote counts.

"""






"""
Solution 1
"""

def get_vote_count(votes):
	return votes['upvotes'] - votes['downvotes']


"""
Solution 2
"""

def get_vote_count(votes):
    votes = int(votes['upvotes']) - int(votes[
                                                    'downvotes'])
    return int(votes)

print(get_vote_count({'downvotes': 4, 'upvotes': 1}))


"""
Solution 3
"""

def get_vote_count(votes):
	up=votes.get('upvotes')
	down=votes.get('downvotes')
	return up-down





