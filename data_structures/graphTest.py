from graph import Graph

graph: Graph = Graph(5)

#Adding edges to the graph nodes
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 1)
graph.add_edge(0, 3, 1)
graph.add_edge(1, 4, 1)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 4, 1)

print("#" * 5 + " Testing BFS Method " + "#" * 5)

graph.bfs(0) # [0 1 2 3 4]

print("#" * 5 + " Testing DFS Method " + "#" * 5)

graph.dfs(0) # [0 1 4 2 3] or [0 3 4 2 1] or [0 3 4 1 2]

graph.shortest_path(0) # [0 1 4 2 3] or [0 3 4 2 1] or [0 3 4 1 2]