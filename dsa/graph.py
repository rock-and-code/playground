from singlyLinkedList import SiglyLinkedList
from myqueue import Queue
from stack import Stack

class Graph(object):
    """
    A custom implementation of a graph data structure
    """
    class Node(object):
        """
        A custom node class to support non-contiguous memory allocation
        to support the custom graph class
        """
        def __init__(self, vertex: int, weight: int) -> None:
            super().__init__()
            self.vertex: int = vertex
            self.weight: int = weight
        
    def __init__(self, verteces: int) -> None:
        """
        Construct a new empty graph with given verteces
        """
        super().__init__()
        self.verteces: int = verteces
        self.adj_list: list[SiglyLinkedList[Graph.Node]] = [SiglyLinkedList() for vertex in range(verteces)]

    def add_vertex(self) -> None:
        """
        Adds an empty singly linked list to the adjacent list
        """
        self.verteces += 1
        self.adj_list.append(SiglyLinkedList())
    
    def add_edge(self, source: int, destination: int, weigth: int) -> None:
        """
        Adds a new edge from a given source to a given destination with a specified weigth
        """
        if not self.adj_list[source].contains(destination):
            self.adj_list[source].add(Graph.Node(destination, weigth))
        
        if not self.adj_list[destination].contains(source):
            self.adj_list[destination].add(Graph.Node(source, weigth))

    def bfs(self, source: int) -> None:
        """
        Traverse the graph from the source using the breath first search algorithm
        """
        visited: list[bool] = [False] * self.verteces
        queue: Queue = Queue()
        queue.add(source)
        visited[source] = True
        print("bfs ->[", end=" ")
        while not queue.empty():
            current_node: int = queue.remove()
            print(current_node, end=" ")
            for adj_node in self.adj_list[current_node]:
                if not visited[adj_node.vertex]:
                    visited[adj_node.vertex] = True
                    queue.add(adj_node.vertex)
        print("]")

    def dfs(self, source: int) -> None:
        """
        Traverse the graph from the source using the breath first search algorithm
        """
        visited: list[bool] = [False] * self.verteces
        stack: Stack = Stack()
        stack.push(source)
        visited[source] = True
        print("dfs ->[", end=" ")
        while not stack.empty():
            current_node: int = stack.pop()
            print(current_node, end=" ")
            for adj_node in self.adj_list[current_node]:
                if not visited[adj_node.vertex]:
                    visited[adj_node.vertex] = True
                    stack.push(adj_node.vertex)
        print("]")

    def shortest_path(self, source: int) -> None:
        """
        Traverse the graph from the source using the breath first search algorithm
        """
        visited: list[bool] = [False] * self.verteces
        distance: list[int] = [1000000] * self.verteces
        distance[source] = 0 # distance of source will always be zero
        queue: Queue = Queue()
        queue.add(source)
        while not queue.empty():
            current_node: int = queue.remove()
            if not visited[current_node]:
                visited[current_node] = True
                for adj_node in self.adj_list[current_node]:
                    current_distance: int = distance[current_node] + adj_node.weight
                    if distance[adj_node.vertex] > current_distance:
                        # Update the distance
                        distance[adj_node.vertex] = current_distance
                    queue.add(adj_node.vertex)
        print("### Shortest path")
        print(f"Source: {source}")
        for i in range(len(distance)):
            print(f"\t{i} -> {distance[i]}")




    

