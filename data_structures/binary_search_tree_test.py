from binary_search_tree import BinarySearchTree
from stack import Stack

bst: BinarySearchTree = BinarySearchTree()


import unittest


class TestMathMethods(unittest.TestCase):

    def is_valid_bst(self, bst: BinarySearchTree) -> bool:
        """
        Returns true if the given bst is valid, meaning that that parent's left child value
        is lower and parent's right child value is greater than parents value.
        """
        stack: Stack = Stack()
        stack.push(bst.root)
        while not stack.empty():
            currentNode: BinarySearchTree.Node = stack.pop()
            if currentNode != None:
                if currentNode.left != None and currentNode.value < currentNode.left.value:
                    return False
                if currentNode.right != None and currentNode.value > currentNode.right.value:
                    return False
                if currentNode.left != None:
                    stack.push(currentNode.left)
                if currentNode.right != None:
                    stack.push(currentNode.right)
        return True

    def recursive_is_valid_bst(self, root: BinarySearchTree.Node) -> bool:
        """
        Returns true if the given bst is valid (root.left.val < root.value < root.right.val)
        Using a recursive approach
        """
        if root != None:
            if root.left != None and root.left.value > root.value:
                return False
            if root.right != None and root.right.value < root.value:
                return False
            return self.recursive_is_valid_bst(root.left) and self.recursive_is_valid_bst(root.right)
        return True
    

    def is_balanced(self, root: BinarySearchTree.Node) -> bool:
        """
        Returns true if the given binary search tree is height balanced. 
        A bst is height balance if the depth of 
        the two subtrees of every node never differs by more than one.s
        """
        if root == None:
            return True
        left_node_height: int = self.height(root.left)
        right_node_height: int = self.height(root.right)
        if abs(left_node_height - right_node_height) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right):
            return True
        return False

    def height(self, root: BinarySearchTree.Node) -> int:
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        
    def test_is_valid_method(self) -> None:
        print("#" * 5 + " Testing Add Method " + "#" * 5)
        bst.add("A")
        bst.add("B")
        bst.add("C")
        bst.add("D")
        print(f"Is the binary search balanced after inserting 4 elements [A B C D]? {self.is_balanced(bst.root)}")
        bst.add("E")
        bst.add("F")
        bst.add("G")
        bst.add("H")
        bst.add("I")
        print(f"Is the binary search balanced after inserting 5 more elements [E F G H I]? {self.is_balanced(bst.root)}")
        self.assertTrue(self.is_balanced(bst.root))
        print("#" * 5 + " Testing Get Method " + "#" * 5)
        print(f"bst.get(E) returns E {bst.get('E') == 'E'}")
        self.assertEqual("E", bst.get('E'))
        print("#" * 5 + " Testing In Order Tree Traversal Method " + "#" * 5)
        bst.print_bst_in_order() 
        

    def test_two_dimension_tree_print(self) -> None:
        print("#" * 5 + " Testing Print Tree Method " + "#" * 5)
        bst.print_tree_grid()

    def test_pre_order_tree_traversal(self) -> None:
        print("#" * 5 + " Testing Pre Order Tree Traversal Method " + "#" * 5)
        bst.print_bst_pre_order() # [A B C ...]

    def test_one(self) -> None:
        self.assertTrue(bst.delete('F'))

        print(f"Is the binary search balanced after deleting one element? {self.is_balanced(bst.root)}")

        print("Printing Binary tree in order after removing one element from it")
        bst.print_bst_in_order()

        print("Deleting elements: A, b, and H from the binary search tree...")
        bst.delete("A")
        self.assertFalse(bst.delete('b'))
        bst.delete("H")
        self.assertTrue(self.is_valid_bst(bst))
        print(f"Is the binary search tree valid? {self.is_valid_bst(bst)}")
        print(f"Is the binary search tree valid? (Recursive) {self.recursive_is_valid_bst(bst.root)}")
        print(f"Is the binary search balanced? {self.is_balanced(bst.root)}")

        print("Deleting element C from binary search tree..")
        bst.delete("C")
        print(f"Is the binary search tree still valid? {self.is_valid_bst(bst)}")
        print(f"Is the binary search tree valid? (Recursive) {self.recursive_is_valid_bst(bst.root)}")
        print(f"Is the binary search balanced? {self.is_balanced(bst.root)}")

        bst.print_tree_grid()
        
        print("Printing the elements of the binary search tree using iterator")

        print("[", end=" ")
        for element in bst:
            print(element, end=" ")
        print("]")


if __name__ == '__main__':
    unittest.main()
















