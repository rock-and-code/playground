from typing import TypeVar, Generic
from myqueue import Queue 

T = TypeVar("T")

class BinarySearchTree(Generic[T]):
    """
    A custom implementation of a binary search tree
    """

    class Node(Generic[T]):
        """
        A custom node class to support non-contiguous data allocation
        in memory to support the custom binary search tree
        """
        def __init__(self, value: T) -> None:
            super().__init__()
            self.value: T = value
            self.left: BinarySearchTree.Node = None
            self.right: BinarySearchTree.Node = None

    def __init__(self) -> None:
        super().__init__()
        self.root: BinarySearchTree.Node = None
    
    # Time: O(LOG N) Space: O(2)
    def add(self, value: T) -> None:
        """
        Adds the specified element in the binary search tree.
        """
        newNode: BinarySearchTree.Node = BinarySearchTree.Node(value)

        if self.root == None:
            self.root = newNode
        else:
            currentNode: BinarySearchTree.Node = self.root
            while True:
                if value <= currentNode.value:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        break
                    else:
                        # Traverse to the left-hand side of the BST
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        break
                    else:
                        # Traverse to the right-hand side of the BST
                        currentNode = currentNode.right
    
    # Time: O(LOG N) Space: O(2)
    def contains(self, value: T) -> bool:
        """
        Returns true if the specified element is in the BST
        """
        if self.root == None:
            return False
        currentNode: BinarySearchTree.Node = self.root
        while currentNode != None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode - currentNode.right
            else:
                # We found a matching value
                return True
        return False
    
    # Time: O(LOG N) Space: O(3)
    def delete(self, value: T) -> bool:
        """
        Removes the first occurrence of the specified element from this list, if it is present.
        """
        if self.root == None:
            return False
        parentNode: BinarySearchTree.Node = None
        currentNode: BinarySearchTree.Node = self.root

        while currentNode != None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # we found a matching value
                # Option No. 1 - child right is None
                if currentNode.right == None:
                    # Checking if we are deleting the root
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left
                    return True
                # Option No. 2 - child right left is None
                elif currentNode.right.left == None:
                    # Assigning the child left to the child right to maintain the balance
                    # since right child is greater than left
                    currentNode.right.left = currentNode.left
                    # Checking if we are deleting the root
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        else:
                            parentNode.right = currentNode.right
                    return True
                # Option No. 3 - child right left is not None (must find left most child of child right)
                else:
                    leftMostParent: BinarySearchTree.Node = currentNode.right
                    leftMost: BinarySearchTree.Node = currentNode.right.left
                    while leftMost.left != None:
                        leftMostParent = leftMost
                        leftMost = leftMost.left
                    # Parent left subtree is the leftmost's right subtree
                    leftMostParent.left = leftMost.right
                    leftMost.left = currentNode.left
                    leftMost.right = currentNode.right
                    # Checking if we are deleting the root
                    if parentNode == None:
                        self.root = leftMost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftMost
                        else:
                            parentNode.right = leftMost
                    return True

        return False
    
    # Time: O(N) Space: O(1)
    def printBSTInOrder(self) -> None:
        """
        Prints the elemtns of this BST in order
        """
        print("[", end=" ")
        self.inOrder(self.root)
        print("]")

    def inOrder(self, node: Node) -> None:
        if node != None:
            self.inOrder(node.left)
            print(node.value, end=" ")
            self.inOrder(node.right)

    def __iter__(self) -> iter:
        return BSTIter(self)

class BSTIter(Generic[T]):
    """
    A custom iterator to make the custom BST implementation
    iterable
    """
    def __init__(self, bst_class: BinarySearchTree) -> None:
        super().__init__()
        self.queue: Queue = Queue()
        self.queue.add(bst_class.root)

    def __iter__(self) -> iter:
        return self
    
    def __next__(self) -> T:
        if not self.queue.empty():
            currentNode: BinarySearchTree.Node = self.queue.remove()
            if currentNode.left != None:
                self.queue.add(currentNode.left)
            if currentNode.right != None:
                self.queue.add(currentNode.right)
            return currentNode.value
        else:
            raise StopIteration
        