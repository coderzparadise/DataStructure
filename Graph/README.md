# Data Structure: Graph()

Background: Graph data structure is a collection of nodes connected by edges. It's used to represent relationships between different entities using functions like DFS, BFS, Topological Sort, Kruskal...

## Adjacency List Functions
insert() - Adds an edge between two nodes (or indices) (overloaded).\
add() -Adds an edge between two nodes (or indices) (overloaded).

display() - Prints the adjacency list.

display_nodes() - Prints the list of nodes.

in_degree() - Calculates and returns the in-degree of each node.

adj_list_to_edge_list() - Converts the adjacency list to an edge list.

adj_list_to_adj_matrix() - Converts the adjacency list to an adjacency matrix.

bfs() - iterates graph nodes checking all nodes in certain depth before increasing depth n times (n = depth of graph).

dfs() - iterates graph going down 1 path until cannot go further and explores other nodes.

topological() - iterates graph nodes in pre-requiste order.


## Adjacency Matrix Functions
insert() - Adds an edge between two nodes (or indices) (overloaded).\
add() - Adds an edge between two nodes (or indices) (overloaded).

display() - Prints the adjacency matrix.

adj_matrix_to_adj_list() - Converts the adjacency matrix to an adjacency list.

adj_matrix_to_edge_list() - Converts the adjacency matrix to an edge list.


## Edge List Functions
insert() - Adds an edge between two nodes (or indices) with a default weight of 0(overloaded).\
add() - Adds an edge between two nodes (or indices) with a default weight of 0 (overloaded).

display() - Prints the edge list.

edge_list_to_adj_list() - Converts the edge list to an adjacency list.

edge_list_to_adj_matrix() - Converts the edge list to an adjacency matrix.

kruskal() - Using custom disjoint forrest set and edge list, able to create weighted graph and find min-span tree, lowest weight edges covering graph.
