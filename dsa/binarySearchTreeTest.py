from binarySearchTree import BinarySearchTree
from stack import Stack

bst: BinarySearchTree = BinarySearchTree()


def isValidBST(bst: BinarySearchTree) -> bool:
    """
    Returns true if the given bst is valid
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



print("#" * 5 + " Testing Add Method " + "#" * 5)

bst.add("A")
bst.add("B")
bst.add("C")
bst.add("D")
bst.add("E")
bst.add("F")
bst.add("G")
bst.add("H")
bst.add("I")
print("Adding three elements in the binary search tree...")
# Prints the elements in the queue [A B C ...]
print("[", end=" ")
for element in bst:
    print(element, end=" ")
print("]")

print("Printing the binary search tree in order")
bst.printBSTInOrder() # [A B C ...]


print("#" * 5 + " Testing Delete Method " + "#" * 5)
expResult = True
print(f"Expected delete('F') result: {expResult} | delete('F') result: {bst.delete('F')}")

print("Binary tree after removing one element from it")

# Prints the elements in the queue [A B C ...]
bst.printBSTInOrder()

print("Deleting elements: A, b, and H from the binary search tree...")
bst.delete("A")
print(f"delete('b') returns: {bst.delete('b')}")
bst.delete("H")

print("Printing binary search tree elements...")
bst.printBSTInOrder()
print(f"Is the binary search tree valid? {isValidBST(bst)}")

print("Deleting ement H from binary search tree..")
bst.delete("C")
print(f"Is the binary search tree still valid? {isValidBST(bst)}")

print("Printing the elements of the binary search tree one more time...")

print("[", end=" ")
for element in bst:
    print(element, end=" ")
print("]")




