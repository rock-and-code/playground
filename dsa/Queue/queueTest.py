from myqueue import Queue

queue: Queue = Queue()

print("#" * 5 + " Testing Empty Method " + "#" * 5)
expResult = True
print(f"Expected empty() result: {expResult} | empty() result: {queue.empty()}")

print("#" * 5 + " Testing Add Method " + "#" * 5)

queue.add("A")
queue.add("B")
queue.add("C")
print("Adding three elements in the queue...")
# Prints the elements in the queue [A B C]
print("[", end=" ")
for element in queue:
    print(element, end=" ")
print("]")

print("After adding three elements in the queue...")
print(f"Is the queue empty? {queue.empty()}")

print("#" * 5 + "T esting Peek Method " + "#" * 5)
expResult = "A"
print(f"Expected peek() result: {expResult} | peek() result: {queue.peek()}")

print("#" * 5 + " Testing Remove Method " + "#" * 5)
expResult = "A"
print(f"Expected pop() result: {expResult} | pop() result: {queue.remove()}")
print("Queue after removing one element from it")

# Prints the elements in the queue [B C]
print("[", end=" ")
for element in queue:
    print(element, end=" ")
print("]")


print("Removing two elements from the stack...")
queue.remove()
queue.remove()

print(f"Is the queue empty? {queue.empty()}")



