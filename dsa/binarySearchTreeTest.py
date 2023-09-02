from binarySearchTree import BinarySearchTree
from stack import Stack

bst: BinarySearchTree = BinarySearchTree()


def is_valid_bst(bst: BinarySearchTree) -> bool:
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

def recursive_is_valid_bst(root: BinarySearchTree.Node) -> bool:
    """
    Returns true if the given bst is valid (root.left.val < root.value < root.right.val)
    Using a recursive approach
    """
    if root != None:
        if root.left != None and root.left.value > root.value:
            return False
        if root.right != None and root.right.value < root.value:
            return False
        return recursive_is_valid_bst(root.left) and recursive_is_valid_bst(root.right)
    return True
    

def is_balanced(root: BinarySearchTree.Node) -> bool:
    """
    Returns true if the given binary search tree is height balanced. 
    A bst is height balance if the depth of 
    the two subtrees of every node never differs by more than one.
    """
    if root == None:
        return True
    left_node_height: int = height(root.left)
    right_node_height: int = height(root.right)
    if abs(left_node_height - right_node_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    return False

def height(root: BinarySearchTree.Node) -> int:
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))



print("#" * 5 + " Testing Add Method " + "#" * 5)

bst.add("A")
bst.add("B")
bst.add("C")
bst.add("D")
print(f"Is the binary search balanced after inserting 4 elements [A B C D]? {is_balanced(bst.root)}")
bst.add("E")
bst.add("F")
bst.add("G")
bst.add("H")
bst.add("I")
print(f"Is the binary search balanced after inserting 5 more elements [E F G H I]? {is_balanced(bst.root)}")

print("Printing a 2 dimension list of strings representing the bst")
bst.print_tree_grid()

print(f"Testing get method")
print(f"bst.get(E) returns E {bst.get('E') == 'E'}")

print("Priting the elements of the tree using iterator...")

print("[", end=" ")
for element in bst:
    print(element, end=" ")
print("]")

print("Printing the binary search tree in order")
bst.print_bst_in_order() 

print("Printing the binary search tree pre order")
bst.print_bst_pre_order() # [A B C ...]


print("#" * 5 + " Testing Delete Method " + "#" * 5)
expResult = True
print(f"Expected delete('F') result: {expResult} | delete('F') result: {bst.delete('F')}")

print(f"Is the binary search balanced after deleting one element? {is_balanced(bst.root)}")

print("Binary tree after removing one element from it")

# Prints the elements in the queue [A B C ...]
bst.print_bst_in_order()

print("Deleting elements: A, b, and H from the binary search tree...")
bst.delete("A")
print(f"delete('b') returns: {bst.delete('b')}")
bst.delete("H")

print("Printing binary search tree elements...")
bst.print_bst_in_order()
print(f"Is the binary search tree valid? {is_valid_bst(bst)}")
print(f"Is the binary search tree valid? (Recursive) {recursive_is_valid_bst(bst.root)}")
print(f"Is the binary search balanced? {is_balanced(bst.root)}")

print("Deleting element C from binary search tree..")
bst.delete("C")
print(f"Is the binary search tree still valid? {is_valid_bst(bst)}")
print(f"Is the binary search tree valid? (Recursive) {recursive_is_valid_bst(bst.root)}")
print(f"Is the binary search balanced? {is_balanced(bst.root)}")

print("Printing the elements of the binary search tree one more time...")

print("[", end=" ")
for element in bst:
    print(element, end=" ")
print("]")


bst.print_tree_grid()







