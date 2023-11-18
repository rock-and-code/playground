from data_structures import UndirectedGraph
import unittest

graph: UndirectedGraph = UndirectedGraph()

class UndirectedGraphTest(unittest.TestCase):
    """
    Unit test for the custom undirected graph implementation
    """
    def test_bsf_method(self) -> None:
        print("#" * 5 + " Testing BFS Method " + 5 * "#")

        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_vertex("G")

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 3)
        graph.add_edge("B", "G", 1)
        graph.add_edge("B", "D", 6)
        graph.add_edge("C", "G", 4)
        graph.add_edge("C", "E", 5)
        graph.add_edge("D", "E", 5)
        graph.add_edge("D", "F", 1)
        graph.add_edge("E", "F", 2)

        graph.bfs("A")

        self.assertTrue(graph.is_cyclic())

    def test_dfs_method(self) -> None:
        print("#" * 5 + " Testing DFS Method " + 5 * "#")

        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_vertex("G")

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 3)
        graph.add_edge("B", "G", 1)
        graph.add_edge("B", "D", 6)
        graph.add_edge("C", "G", 4)
        graph.add_edge("C", "E", 5)
        graph.add_edge("D", "E", 5)
        graph.add_edge("D", "F", 1)
        graph.add_edge("E", "F", 2)

        graph.dfs("A")

        self.assertTrue(graph.is_cyclic())

    def test_shortest_path_method(self) -> None:
        print("#" * 5 + " Testing Shortest Path Method " + 5 * "#")

        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_vertex("G")

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 3)
        graph.add_edge("B", "G", 1)
        graph.add_edge("B", "D", 6)
        graph.add_edge("C", "G", 4)
        graph.add_edge("C", "E", 5)
        graph.add_edge("D", "E", 5)
        graph.add_edge("D", "F", 1)
        graph.add_edge("E", "F", 2)

        graph.shortes_path("A")

        self.assertTrue(graph.is_cyclic())

    def test_remove_edge(self) -> None:
        print("#" * 5 + " Testing Remove Ege Method " + 5 * "#")

        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_vertex("G")

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 3)
        graph.add_edge("B", "G", 1)
        graph.add_edge("B", "D", 6)
        graph.add_edge("C", "G", 4)
        graph.add_edge("C", "E", 5)
        graph.add_edge("D", "E", 5)
        graph.add_edge("D", "F", 1)
        graph.add_edge("E", "F", 2)

        # graph.print_all_edges()

        graph.remove_edge("E", "F", 2)

        # graph.print_all_edges()

    def test_spanning_tree_method(self) -> None:
        print("#" * 5 + " Testing Spanning Tree Method " + 5 * "#")

        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_vertex("G")

        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 3)
        graph.add_edge("B", "G", 1)
        graph.add_edge("B", "D", 6)
        graph.add_edge("C", "G", 4)
        graph.add_edge("C", "E", 5)
        graph.add_edge("D", "E", 5)
        graph.add_edge("D", "F", 1)
        graph.add_edge("E", "F", 2)

        # graph.print_edges()

        spanning_tree: UndirectedGraph = graph.spanning_tree()

        spanning_tree_two: UndirectedGraph = graph.kruskal_mst()

        spanning_tree.print_edges()
        spanning_tree_two.print_edges()

        print(f"Is spanning tree cyclic: {spanning_tree.is_cyclic()}")
        print(f"Is spanning two tree cyclic: {spanning_tree_two.is_cyclic()}")

        self.assertFalse(spanning_tree.is_cyclic())
        self.assertFalse(spanning_tree_two.is_cyclic())

if __name__ == '__main__':
    unittest.main()

