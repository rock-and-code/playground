import unittest
from data_structures import BinaryTree

binaryTree: BinaryTree = BinaryTree()

class BinaryTreeTest(unittest.TestCase):

    def test_add_method(self) -> None:
        print("#" * 5 + " Testing Add Method " + "#" * 5)

        binaryTree.add("A")
        binaryTree.add("B")
        binaryTree.add("C")
        print("Adding three elements (A, B, C) in the binary tree...")
        # Prints the elements in the queue [A B C]
        print("[", end=" ")
        for element in binaryTree:
            print(element, end=" ")
        print("]")
        self.assertEqual(binaryTree.size, 3)

    def test_print_binary_tree_in_order_method(self) -> None:
        print("Printing the binary tree in order")
        binaryTree.printBinaryTreeInOrder()

    def test_delete_method(self) -> None:
        print("#" * 5 + " Testing Delete Method " + "#" * 5)
        expResult = "A"
        print(f"Expected delete() result: {expResult} | delete() result: {binaryTree.delete('A')}")
        print("Binary tree after removing one element from it")
        # Prints the elements in the queue [B C]
        binaryTree.printBinaryTreeInOrder()


if __name__ == '__main__':
    unittest.main()





