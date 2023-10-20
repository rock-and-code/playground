from typing import TypeVar, Generic
from .my_queue import Queue 

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
            """
            Creates a new BST node
            """
            super().__init__()
            self.value: T = value
            self.height: int = 1
            self.left: BinarySearchTree.Node = None
            self.right: BinarySearchTree.Node = None

    def __init__(self) -> None:
        super().__init__()
        self.root: BinarySearchTree.Node = None

    def get(self, value: T) -> T:
        """
        Returns the the given element if it exists in the bst
        """
        current_node: BinarySearchTree.Node = self.root
        while current_node != None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node.value
        return None

    # Time: O(LOG N) Space: O(2)
    def add(self, value: T) -> None:
        """
        Adds the specified element in the binary search tree.
        And the rebalance the tree
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
            # Balances the tree after adding new node
            self.balance_tree_after_modification(value, True)

    def height(self, node: Node) -> int:
        """
        Returns the height of the given bst node is not null, otherwise will return zero
        """
        if node == None:
            return 0
        return node.height

    def left_rotate(self, node: Node, parent: Node) -> None:
        right_child: BinarySearchTree.Node = node.right
        sub_tree: BinarySearchTree.Node = right_child.left

        node.right = sub_tree
        right_child.left = node

        #update height
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1

        node = right_child

        # checks if we are rotating the root 
        if parent == None:
            self.root = node
        else:
            if node.value < parent.value:
                parent.left = node
            else:
                parent.right = node

    def right_rotate(self, node: Node, parent: Node) -> None:
        left_child: BinarySearchTree.Node = node.left
        sub_tree: BinarySearchTree.Node = left_child.right

        node.left = sub_tree
        left_child.right = node

        # update the height
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1

        node = left_child

        if parent == None:
            self.root = node
        else:
            if node.value < parent.value:
                parent.left = node
            else:
                parent.right = node

    def update_tree_height(self) -> None:
        """
        Updates the heigths of the bst after either and insertion or a deletion of a node
        from the root to the leafs
        """
        self.update_height(self.root)

    def update_height(self, node: Node) -> int:
        """
        Helper function to update the height of all the nodes in the bst after either an insertion
        or a deletion of a node
        """
        left_child_height: int
        right_child_height: int

        if node.left == None:
            left_child_height = 0
        else:
            left_child_height = node.left.height = self.update_height(node.left)

        if node.right == None:
            right_child_height = 0
        else:
            right_child_height = node.right.height = self.update_height(node.right)

        return 1 + max(left_child_height, right_child_height)
    

    def get_balance(self, node: Node) -> int:
        """
        Returns the balance of a given node (left-child height - right-child height)
        """
        if node == None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def balance_tree_after_modification(self, value: T, insertion: bool) -> None:
        """
        Balances the tree after either an insertion or a deletion from the root to the leaf nodes
        """
        parent: BinarySearchTree.Node = None
        node: BinarySearchTree.Node = self.root

        # Updateing the tree height (Important to calculate the balance and thus rotate the nodes)
        self.update_tree_height()
        while node != None:
            balance: int = self.get_balance(node)

            # 4 cases for rotation
            if balance > 1:
                # left-hand side of tree is unbalance
                if (value > node.left.value if insertion == True else self.get_balance(node.left) < -1):
                    self.left_rotate(node.left, node)
                
                self.right_rotate(node, parent)
            elif balance < -1:
                # right-hand side of tree is unbalanced
                if (value < node.right.value if insertion == True else self.get_balance(node.right) > 1):
                    self.right_rotate(node.right, node)
                
                self.left_rotate(node, parent)

            # Traversing to the tree throught the path either the added or delete node passed
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

    def balance_tree_after_deletion(self, value: T) -> None:
        """
        Balances the tree after either an insertion or a deletion from the root to the leaf nodes
        """
        parent: BinarySearchTree.Node = None
        node: BinarySearchTree.Node = self.root

        # Updateing the tree height (Important to calculate the balance and thus rotate the nodes)
        self.update_tree_height()
        while node != None:
            balance: int = self.get_balance(node)

            # 4 cases for rotation
            if balance > 1:
                # left-hand side of tree is unbalance
                if self.get_balance(node.left) < 0:
                    self.left_rotate(node.left, node)
                
                self.right_rotate(node, parent)
            elif balance < -1:
                # right-hand side of tree is unbalanced
                if self.get_balance(node.right) > 0:
                    self.right_rotate(node.right, node)
                
                self.left_rotate(node, parent)

            # Traversing to the tree throught the path either the added or delete node passed
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
    
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
        And rebalances the tree.
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
                # Option No. 1 - no parent right child
                if currentNode.right == None:
                    # Checking if we are deleting the root
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left
                    self.balance_tree_after_modification(value, False)
                    return True
                # Option No. 2 - parent's right child has no left child
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
                    self.balance_tree_after_modification(value, False)
                    return True
                # Option No. 3 - Parents right child has a left child 
                # (must find left most child of parent's right child)
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
                    self.balance_tree_after_modification(value, False)
                    return True

        return False
    
    # Time: O(N) Space: O(1)
    def print_bst_in_order(self) -> None:
        """
        Prints the elemtns of this BST in order
        """
        print("[", end=" ")
        self.in_order(self.root)
        print("]")

    def in_order(self, node: Node) -> None:
        if node != None:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    def print_bst_pre_order(self) -> None:
        """
        Prints the elemtns of this BST in order
        """
        print("[", end=" ")
        self.pre_order(self.root)
        print("]")
    
    def pre_order(self, node: Node) -> None:
        if node != None:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def tree_grid(self) -> list[list[str]]:
        """
        Returns a 2 dimension list of strings representing this bst
        """
        height: int = self.height(self.root)
        width: int = pow(2, height) - 1
        grid: list[list[str]] = []
        for _ in range(height):
            grid.append([" " for _ in range(width)])
        self.set_rows(grid, self.root, 0, 0, width - 1)
        return grid

    def set_rows(self, grid: list[list[str]], root: Node, row: int, left: int, right: int) -> None:
        if root != None:
            mid: int = (left + right) // 2
            self.set_rows(grid, root.left, row + 1, left, mid - 1)
            grid[row][mid] = str(root.value)
            self.set_rows(grid, root.right, row + 1, mid + 1, right)

    def print_tree_grid(self) -> None:
        """
        Prints a 2 dimension list of stirngs representing this bst
        """
        grid: list[list[str]] = self.tree_grid()
        for row in grid:
            print(row)


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
            raise StopIteration()
        
        