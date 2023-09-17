
class sum_segment_tree(object):
    """
    A custom implementation of a segment tree to get the sum of 
    a given range
    """

    class TreeNode(object):
        """
        A class to support the segment tree implementation and allow
        non-contiguous memory address allocation
        """
        def __init__(self, start_index: int, end_index: int) -> None:
            self.start_index: int = start_index
            self.end_index: int = end_index
            self.value: int = 0
            self.left: sum_segment_tree.TreeNode = None
            self.right: sum_segment_tree.TreeNode = None

    #method to get height
    def __init__(self, arr: list[int]) -> None:
        """
        Construct a new segment tree with a given array of intengers
        """
        self.root = self.create_tree(arr)

    def create_tree(self, arr: list[int]) -> TreeNode:
        """
        Creates a binary tree with a given array of integers
        """
        return self.create_tree_helper(arr, 0, len(arr) - 1)
    
    def create_tree_helper(self, arr: list[int], start: int, end: int) -> TreeNode:
        """
        Creates a two dimentional list of strings representing the elements of this binary tree
        """
        if start == end:
            tree_node: sum_segment_tree.TreeNode = sum_segment_tree.TreeNode(start, end)
            tree_node.value = arr[start]
            return tree_node
        
        mid: int = (start + end) // 2

        tree_node: sum_segment_tree.TreeNode = sum_segment_tree.TreeNode(start, end)

        tree_node.left = self.create_tree_helper(arr, start, mid)
        tree_node.right = self.create_tree_helper(arr, mid + 1, end)

        tree_node.value = tree_node.left.value + tree_node.right.value

        return tree_node
    
    def get_sum(self, start_index: int, end_index: int) -> int:
      """
      Returns the sum of a given interval (start, end)
      """
      return self.get_sum_helper(self.root, start_index, end_index)
    
    def get_sum_helper(self, root: TreeNode, start_index: int, end_index: int) -> int:
        # base cases
        # option 1: given interval inside of current node interval
        if root.start_index >= start_index and root.end_index <= end_index:
            return root.value
        # option 2: given interval out of scope of the current node
        if root.end_index < start_index or root.start_index > end_index:
            return 0
        # option 3: given interval overlaps the current node interval
        # Delegate it to children
        return self.get_sum_helper(root.left, start_index, end_index) \
            + self.get_sum_helper(root.right, start_index, end_index)

    def update_value(self, index: int, new_value: int) -> None:
        """
        Updates the value of the node tree at a given index
        """
        self.update_value_helper(self.root, index, new_value)

    def update_value_helper(self, root: TreeNode, index: int, new_value: int) -> None:
        if root != None:
            if index >= root.start_index or index <= root.end_index:
                if root.start_index == index and root.end_index == index:
                    root.value = new_value
                    return
                
                self.update_value_helper(root.left, index, new_value)
                self.update_value_helper(root.right, index, new_value)
                if root.left != None and root.right != None:
                    root.value = root.left.value + root.right.value

    def get_height(self, tree_node: TreeNode) -> int:
        """
        Returns the height of the given tree node in the tree.
        The height is the distant from a given node to the most distant
        leaf node.
        """
        if tree_node == None:
            return 0
        return max(self.get_height(tree_node.left), self.get_height(tree_node.right)) + 1
    # method to craete tree given an array

    def print_two_dim_tree(self) -> None:
        """
        Prints the two dimensional binary tree grid
        """
        grid: list[list[str]] = self.get_tree_grid()
        for row in grid:
            print(row)

    def get_tree_grid(self) -> list[list[str]]:
        """
        Helper function to create a two dimensional list of string representing
        this binary tree elements
        """
        height: int = self.get_height(self.root)
        width: int = self.binary_exponentiation(2, height)
        grid: list[list[str]] = []
        for _ in range(height):
            grid.append([" " for _ in range(width)])
        self.create_tree_grid(self.root, grid, 0, 0, width - 1)
        return grid

    def create_tree_grid(self, root: TreeNode, grid: list[list[str]], row: int, start: int, end: int) -> None:
        """
        A helper function that populates the two dimensional list of strings representing the elements of this
        tree by traving the tree in order
        """
        if root != None:
            mid: int = (start + end) // 2
            grid[row][mid] = root.value
            self.create_tree_grid(root.left, grid, row + 1, start, mid -1)
            self.create_tree_grid(root.right, grid, row + 1, mid + 1, end)


    def binary_exponentiation(self, a: int, n: int) -> int:
        """
        Calculates the exponent of a given base and power
        Time: O(LOG N)
        """
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.binary_exponentiation(a*a, n//2)
        else:
            return a * self.binary_exponentiation(a*a, (n - 1)//2)

    