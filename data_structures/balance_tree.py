from typing import TypeVar, Generic, Optional, Iterator
from queue import SimpleQueue

K = TypeVar("K")
V = TypeVar("V")

class AVLTree(Generic[K]):
    """ A custom implementation of the AVL Tree """

    class Node(Generic[K]):
        def __init__(self, data: K):
            self.data = data
            self.height = 0
            self.left: Optional['AVLTree.Node[K]'] = None
            self.right: Optional['AVLTree.Node[K]'] = None

    def __init__(self):
        self.root: Optional[AVLTree.Node[K]] = None
        self.size = 0

    def get_height(self, root: Optional['AVLTree.Node[K]']) -> int:
        """Helper function to get the height of a given node"""
        return -1 if root is None else root.height

    def left_rotate(self, root: 'AVLTree.Node[K]') -> 'AVLTree.Node[K]':
        right_child = root.right
        sub_tree = right_child.left if right_child else None

        right_child.left = root
        root.right = sub_tree

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        right_child.height = max(self.get_height(right_child.left), self.get_height(right_child.right)) + 1
        
        return right_child

    def right_rotate(self, root: 'AVLTree.Node[K]') -> 'AVLTree.Node[K]':
        left_child = root.left
        sub_tree = left_child.right if left_child else None

        left_child.right = root
        root.left = sub_tree

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        left_child.height = max(self.get_height(left_child.left), self.get_height(left_child.right)) + 1
        
        return left_child

    def get_balance(self, root: Optional['AVLTree.Node[K]']) -> int:
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def add(self, data: K) -> None:
        """Adds a node to the AVL tree and ensures it remains balanced"""
        self.root = self.add_helper(self.root, data)

    def add_helper(self, root: Optional['AVLTree.Node[K]'], data: K) -> 'AVLTree.Node[K]':
        if root is None:
            self.size += 1
            return AVLTree.Node(data)

        if data < root.data:
            root.left = self.add_helper(root.left, data)
        elif data > root.data:
            root.right = self.add_helper(root.right, data)
        else:
            return root  # Duplicate values are not allowed

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.balance_tree(root)

    def balance_tree(self, root: 'AVLTree.Node[K]') -> 'AVLTree.Node[K]':
        balance = self.get_balance(root)

        # Left heavy
        if balance > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right heavy
        if balance < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def remove(self, data: K) -> None:
        """Removes a node from the AVL tree and ensures it remains balanced"""
        self.root = self.remove_helper(self.root, data)

    def remove_helper(self, root: Optional['AVLTree.Node[K]'], data: K) -> Optional['AVLTree.Node[K]']:
        if root is None:
            return None

        if data < root.data:
            root.left = self.remove_helper(root.left, data)
        elif data > root.data:
            root.right = self.remove_helper(root.right, data)
        else:
            # Node to be deleted found
            if root.left is None or root.right is None:
                self.size -= 1
                return root.left if root.left is not None else root.right

            # Node with two children: Get the inorder successor (leftmost node in the right subtree)
            temp = self.get_left_most(root.right)
            root.data = temp.data
            root.right = self.remove_helper(root.right, temp.data)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.balance_tree(root)

    def get_left_most(self, root: 'AVLTree.Node[K]') -> 'AVLTree.Node[K]':
        """Helper to get the leftmost (smallest) node"""
        current = root
        while current.left is not None:
            current = current.left
        return current

    def get(self, data: K) -> Optional[K]:
        """Returns the data if found, else None"""
        return self.get_helper(self.root, data)

    def get_helper(self, root: Optional['AVLTree.Node[K]'], data: K) -> Optional[K]:
        if root is None:
            return None
        if data < root.data:
            return self.get_helper(root.left, data)
        elif data > root.data:
            return self.get_helper(root.right, data)
        return root.data
    
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1 
    
    def tree_grid(self):
        """
        Returns a 2 dimension list of strings representing this bst
        """
        height = self.height(self.root)
        width = pow(2, height) - 1
        grid = []
        for _ in range(height):
            grid.append([" " for _ in range(width)])
        self.set_rows(grid, self.root, 0, 0, width - 1)
        return grid

    def set_rows(self, grid, root, row, left, right):
        if root != None:
            mid = (left + right) // 2
            self.set_rows(grid, root.left, row + 1, left, mid - 1)
            grid[row][mid] = str(root.data)
            self.set_rows(grid, root.right, row + 1, mid + 1, right)

    def print_tree_grid(self):
        """
        Prints a 2 dimension list of stirngs representing this bst
        """
        grid = self.tree_grid()
        for row in grid:
            print(row)

    def __iter__(self) -> Iterator[K]:
        return AVLTreeIter(self)


class AVLTreeIter(Generic[K], Iterator[K]):
    """Custom iterator for AVL Tree using in-order traversal"""

    def __init__(self, tree: AVLTree[K]):
        self.queue = SimpleQueue()
        self.populate_queue(tree.root)

    def populate_queue(self, root: Optional['AVLTree.Node[K]']) -> None:
        if root:
            self.populate_queue(root.left)
            self.queue.put(root.data)
            self.populate_queue(root.right)

    def __iter__(self) -> 'AVLTreeIter[K]':
        return self

    def __next__(self) -> K:
        if not self.queue.empty():
            return self.queue.get()
        raise StopIteration()
