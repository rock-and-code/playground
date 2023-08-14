from stack import Stack

stack: Stack = Stack()

print("#" * 5 + " Testing Empty Method " + "#" * 5)
expResult = True
print(f"Expected empty() result: {expResult} | empty() result: {stack.empty()}")

print("#" * 5 + " Testing Push Method " + "#" * 5)
stack.push("A")
stack.push("B")
stack.push("C")
stack.printStack() # [C B A]
print(f"Is the stack empty? {stack.empty()}")

print("#" * 5 + "T esting Peek Method " + "#" * 5)
expResult = "C"
print(f"Expected peek() result: {expResult} | peek() result: {stack.peek()}")

print("#" * 5 + " Testing Pop Method " + "#" * 5)
expResult = "C"
print(f"Expected pop() result: {expResult} | pop() result: {stack.pop()}")
print("Stack after popping one element from it")
#stack.printStack() # [B A]
print("[", end=" ")
for s in stack:
    print(s, end=" ")
print("]")

print("Popping two elements from the stack...")
stack.pop()
stack.pop()

print(f"Is the stack empty? {stack.empty()}")



