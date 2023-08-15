from binaryTree import BinaryTree

binaryTree: BinaryTree = BinaryTree()

print("#" * 5 + " Testing Add Method " + "#" * 5)

binaryTree.add("A")
binaryTree.add("B")
binaryTree.add("C")
print("Adding three elements in the binary tree...")
# Prints the elements in the queue [B A C]
print("[", end=" ")
for element in binaryTree:
    print(element, end=" ")
print("]")

print("Printing the binary tree in order")
binaryTree.printBinaryTreeInOrder()


print("#" * 5 + " Testing Delete Method " + "#" * 5)
expResult = "A"
print(f"Expected delete() result: {expResult} | delete() result: {binaryTree.delete('A')}")

print("Binary tree after removing one element from it")

# Prints the elements in the queue [B C]
binaryTree.printBinaryTreeInOrder()




