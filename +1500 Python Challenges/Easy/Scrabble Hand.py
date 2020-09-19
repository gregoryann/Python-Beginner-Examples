"""
Scrabble Hand

Given a list of scrabble tiles (as dictionaries), create a function that outputs the maximum possible score a player can achieve by summing up the total number of points for all the tiles in their hand. Each hand contains 7 scrabble tiles.

Here's an example hand:

[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
The player's maximum_score from playing all these tiles would be 1 + 5 + 10 + 8 + 2 + 1 + 1, or 28.

Examples
maximum_score([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]) ➞ 28

maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
]) ➞ 15

Notes
Here, each tile is represented as an dictionary with two keys: tile and score.
"""


"""
Solution 1
"""

def maximum_score(tile_hand):
	return sum([i['score'] for i in tile_hand])

"""
Solution 2
"""

def maximum_score(tile_hand):
    answer = 0
    
    for i in tile_hand:
        answer += i['score']
    return answer

"""
Solution 3
"""

def maximum_score(tile_hand):
    lst = []
    for i in tile_hand:
        lst.append(i.get('score'))
    return sum(lst)


"""
Solution 4
"""

def maximum_score(tile_hand):
	score=0
	for el in tile_hand:
		score = el.get("score") + score
	return score




