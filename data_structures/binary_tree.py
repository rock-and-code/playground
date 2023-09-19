from typing import TypeVar, Generic

from myqueue import Queue

T = TypeVar("T")

class BinaryTree(Generic[T]):
    """
    A custom implementation of a tree data structure
    """
    
    class Node(Generic[T]):
        """
        A custome implementation of a Node class
        to support reference of non-contiguous data allocated
        in memory 
        """

        def __init__(self, value: T) -> None:
            super().__init__()
            self.value: T = value
            self.left: BinaryTree.Node = None
            self.right: BinaryTree.Node = None
        
    def __init__(self) -> None:
        """
        Creates an empty binary tree
        """
        super().__init__()
        self.root: BinaryTree.Node = None
        self.size: int = 0

    # Time: O(N) Space: O(1)
    def add(self, value: T) -> None:
        """
        Inserts a new element in this binary Tree
        """
        if self.root == None:
            self.root = BinaryTree.Node(value)
            self.size += 1
        else:
            queue: Queue = Queue()
            queue.add(self.root)

            while not queue.empty():
                currentNode: BinaryTree.Node = queue.remove()
                if currentNode.left == None:
                    currentNode.left = BinaryTree.Node(value)
                    self.size += 1
                    return
                else:
                    queue.add(currentNode.left)

                if currentNode.right == None:
                    currentNode.right = BinaryTree.Node(value)
                    self.size += 1
                    return
                else:
                    queue.add(currentNode.right)

    # Time: O(N) Space: O(N)
    def delete(self, value: T) -> T:
        """
        Removes the first occurrence of the specified element from this list, if it is present.
        """
        deletedValue: T = None
        if self.root == None:
            self.size -= 1
            return None
        if self.root.left == None and self.root.right == None:
            if self.root.value == value:
                deletedValue = self.root.value
                self.root = None
                return deletedValue
            else:
                return None
        queue: Queue = Queue()
        queue.add(self.root)
        node: BinaryTree.Node = None
        keyNode: BinaryTree.Node = None
        while not queue.empty():
            node = queue.remove()

            if node.value == value:
                keyNode = node
                deletedValue = node.value
            
            if node.left != None:
                queue.add(node.left)

            if node.right != None:
                queue.add(node.right)

        # Checks if we found the specified element in the binary tree
        if keyNode != None:
            x: T = node.value # last node of the tree which will replace the node to be deleted
            self.deleteDeepest(node)
            keyNode.value = x
            self.size -= 1
        return deletedValue

    # Time: O(N) Space: O(2)
    def deleteDeepest(self, node: Node) -> None:
        queue: Queue = Queue()
        queue.add(self.root)

        while not queue.empty():
            currentNode: BinaryTree.Node = queue.remove()

            if currentNode == node:
                currentNode = None
                return
            
            if currentNode.left != None:
                if currentNode.left == node:
                    currentNode.left = None
                    return
                else:
                    queue.add(currentNode.left)
            
            if currentNode.right != None:
                if currentNode.right == node:
                    currentNode.right = None
                    return
                else:
                    queue.add(currentNode)

    # Time: O(N) Space: O(1)
    def printBinaryTreeInOrder(self) -> None:
        """
        Prints all the elements in this binary tree in order fashion (left child, parent, right child)
        """
        print("[", end=" ")
        self.inOrder(self.root)
        print("]")

    def inOrder(self, root: Node) -> None:
        if root != None:
            self.inOrder(root.left)
            print(root.value, end=" ")
            self.inOrder(root.right)

    def __iter__(self) -> iter:
        return BinaryTreeIter(self)
    

class BinaryTreeIter(Generic[T]):
    """
    A custom iterator to make the custom binary tree implementation 
    iterable
    """
    def __init__(self, binary_tree_class: BinaryTree) -> None:
        super().__init__()
        self.queue: Queue = Queue()
        self.queue.add(binary_tree_class.root)


    def __iter__(self) -> iter:
        return self
    
    def __next__(self) -> T:
        if not self.queue.empty():
            currentNode: BinaryTree.Node = self.queue.remove()
            if currentNode.left != None:
                self.queue.add(currentNode.left);
            if currentNode.right != None:
                self.queue.add(currentNode.right)
            return currentNode.value
        else:
            raise StopIteration
