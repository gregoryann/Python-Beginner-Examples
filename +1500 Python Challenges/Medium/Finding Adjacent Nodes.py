"""

Finding Adjacent Nodes
A graph is a set of nodes and edges that connect those nodes.

Graph Example

There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no particular direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it (like a one-way street).

For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.

We can encode graphs using an adjaceny matrix. An adjacency matrix for a graph with 'n' nodes is an 'n * n' matrix where the entry at row 'i' and column 'j' is a 0 if nodes 'i' and 'j' are not adjacent, and 1 if nodes 'i' and 'j' are adjacent.

For the example above, the adjacency matrix woudl be as follows:

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
Your task is to determine if two nodes are adjacent in a graph when given the adjacency matrix and the two nodes.

Examples
Graph Example

Adjacency Matrix:

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
Nodes 0,1 should return true.
Nodes 0,2 should return false.
Graph Example 2

[
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]
Nodes 0,3 should return true.
Nodes 1,4 should return false.
Notes
Graphs may have between 0 and 25,000 nodes.
Time Limit: 100 milliseconds.


"""





################################################################
"""
Solution 1
"""


def is_adjacent(matrix, node1, node2):
	return matrix[node1][node2] == 1





################################################################
"""
Solution 2
"""


def is_adjacent(matrix, node1, node2):
	return (matrix[node1][node2] == matrix[node2][node1]) and (matrix[node1][node2] == 1)







