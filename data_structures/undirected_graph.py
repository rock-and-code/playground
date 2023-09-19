from stack import Stack
from myqueue import Queue
import copy

from typing import TypeVar, Generic

T = TypeVar("T")

Self = TypeVar("Self", bound="UndirectedGraph")

class UndirectedGraph(Generic[T]):
    """
    A custom implementation of a generic undirected graph
    """
    class Edge(Generic[T]):
        """
        Represents a graph edge between two nodes
        """
        def __init__(self, source: T, destination: T, weight: int) -> None:
            """
            Construct a new Edge with given source, destination, and weight
            """
            super().__init__()
            self.source: T = source
            self.destination: T = destination
            self.weight: int = weight


        def __str__(self) -> str:
            """
            Returns a string representation of the graph edge
            """
            return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"
        
        def __eq__(self, obj: object) -> bool:
            """
            Returns true if the given edge is equals to this edge
            """
            if isinstance(obj, UndirectedGraph.Edge):
                return self.source == obj.source and self.destination == obj.destination
            return NotImplemented
        
        def __ne__(self, other):
            x = self.__eq__(other)
            if x == NotImplemented:
                return NotImplemented
            return not x
        
        def __hash__(self):
            return hash(self.source + self.destination)

    def __init__(self) -> None:
        super().__init__()
        self.adj_list: dict[T, set[UndirectedGraph.Edge]] = {}
        self.vertexes: int = 0

    
    def add_vertex(self, vertex: T) -> None:
        """
        Inserts a new vertex in this graph if it does not exists.
        """
        if vertex not in self.adj_list:
            self.vertexes += 1
            self.adj_list[vertex] = set()

    def add_edge(self, source: T, destination: T, weight: int) -> None:
        """
        Adds a new edge to both source and destination graph vertexes if both exists 
        in the graph
        """
        if source in self.adj_list and destination in self.adj_list:
            self.adj_list[source].add(UndirectedGraph.Edge(source, destination, weight))
            self.adj_list[destination].add(UndirectedGraph.Edge(destination, source, weight))

    def remove_edge(self, source: T, destination: T, weight: int) -> None:
        """
        Removes a edge from both source and destination graph vertexes if both vertexes exists 
        in the graph
        """
        if source in self.adj_list and destination in self.adj_list:
            for edge in self.adj_list[source].copy():
                if edge.source == source and edge.destination == destination:
                    self.adj_list[source].remove(edge)
            for edge in self.adj_list[destination].copy():
                if edge.source == destination and edge.destination == source:
                    self.adj_list[destination].remove(edge)

    def is_cyclic(self) -> bool:
        """
        Returns true if there is a cycle in this graph
        """
        visited: set[T] = set()
        for k in self.adj_list:
            if k not in visited:
                if self.is_cyclic_util(k, visited, None):
                    return True
        return False
    
    def is_cyclic_util(self, vertex: T, visited: set[T], parent: T) -> bool:
        visited.add(vertex)
        for edge in self.adj_list[vertex]:
            if edge.destination not in visited:
                if self.is_cyclic_util(edge.destination, visited, vertex):
                    return True
            elif edge.destination != parent:
                    return True
        return False
    
    def bfs(self, source: T) -> None:
        if source not in self.adj_list:
            return
        """
        Traverses and prints the vertexes of this graph using a breath search first
        algorith from a given source vertex
        """
        visited: set[T] = set()
        visited.add(source)
        queue: Queue = Queue()
        queue.add(source)
        print("BFS: [", end=" ")
        while not queue.empty():
            vertex: T = queue.remove()
            print(vertex, end=" ")
            for edge in self.adj_list[vertex]:
                if edge.destination not in visited:
                    visited.add(edge.destination)
                    queue.add(edge.destination)
        print("]")

    def dfs(self, source: T) -> Self:
        if source not in self.adj_list:
            return
        """
        Traverses and prints the vertexes of this graph using a depth first search
        algorith from a given source vertex
        """
        visited: set[T] = set()
        visited.add(source)
        stack: Stack = Stack()
        stack.push(source)
        print("BFS: [", end=" ")
        while not stack.empty():
            vertex: T = stack.pop()
            print(vertex, end=" ")
            for edge in self.adj_list[vertex]:
                if edge.destination not in visited:
                    visited.add(edge.destination)
                    stack.push(edge.destination)
        print("]")


    def shortes_path(self, source: T) -> None:
        """
        Traverses the graph and prints the vertices with its shortest distance from 
        a given source
        """
        visited: set[T] = set()
        visited.add(source)
        distance: dict[T, int] = {}
        for vertex in self.adj_list:
            distance[vertex] = 10000000
        distance[source] = 0 # distance from source is always zero
        queue: Queue = Queue()
        queue.add(source)
        while not queue.empty():
            vertex: T = queue.remove()
            for edge in self.adj_list[vertex]:
                current_distance: int = distance[vertex] + edge.weight
                if distance[edge.destination] > current_distance:
                    distance[edge.destination] = current_distance
                if edge.destination not in visited:
                    visited.add(edge.destination)
                    queue.add(edge.destination)
        # Printing results
        print(f"Source: {source}")
        for vertex in distance:
            print(f"{vertex} : {distance[vertex]}")


        # Time: O(MN + N LOG N)
    def spanning_tree(self):
        """
        Returns a new unidirected graph with all the vertexes of the 
        of this graph and the minimum number of edges
        """
        # Getting all the egdes from the graph
        visited: set[T] = set()
        spanning_tree: UndirectedGraph = UndirectedGraph()
        edges: list[UndirectedGraph.Edge] = []

        for vertex in self.adj_list:
            visited.add(vertex)
            spanning_tree.add_vertex(vertex)
            for edge in self.adj_list[vertex]:
                if edge.destination not in visited:
                    edges.append(edge)
                    # visited.add(edge.destination)

        edges.sort(key=lambda edge: edge.weight)
        added_edges: int = 0 
        for edge in edges:
            spanning_tree.add_edge(edge.source, edge.destination, edge.weight)
            added_edges += 1
            if spanning_tree.is_cyclic():
                added_edges -= 1
                spanning_tree.remove_edge(edge.source, edge.destination, edge.weight)
            if added_edges == len(self.adj_list) - 1:
                break

        return spanning_tree
    
    def print_edges(self) -> None:
        total_cost: int = 0
        visited: set[T] = set()
        print(f"Edges: ")
        for vertex in self.adj_list:
            visited.add(vertex)
            for edge in self.adj_list[vertex]:
                if edge.destination not in visited:
                    # visited.add(edge.destination)
                    total_cost += edge.weight
                    print(edge)
        print(f"Total cost: {total_cost}")

    def print_vertexes(self) -> None:
        print("Vertexes [", end=" ")
        for vertex in self.adj_list:
            print(vertex, end=" ")
        print("]")

    



    