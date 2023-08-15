from singlyLinkedList import SiglyLinkedList

print("#" * 5 + " Testing Add Method " + "#" * 5)
list: SiglyLinkedList = SiglyLinkedList()
list.add(1)
list.add(3)
list.add(4)
list.add(5)
expResult = 4
list.printList() #  [1 3 4 5]
print(f"List expected size: {expResult} : List current size: {list.size}")

print("#" * 5 + " Testing Insert Method " + "#" * 5)
list.insert(2, 11)
list.printList() #  [1 3 11 4 5]
expResult = 5
print(f"List expected size: {expResult} : List current size: {list.size}")
list.insert(4, 99)
list.printList() #  [1 3 11 4 99 5]
expResult = 6
print(f"List expected size: {expResult} : List current size: {list.size}")

print("#" * 5 + " Testing Remove Method " + "#" * 5)
list.remove(11) 
list.printList() # [1 3 4 99 5]
expResult = 5
print(f"List expected size: {expResult} : List current size: {list.size}")
list.remove(5) 
list.printList() # [1 3 4 99]
expResult = 4
print(f"List expected size: {expResult} : List current size: {list.size}")

print("#" * 5 + " Testing Get Method " + "#" * 5)
expResult = 99
print(f"get({3}) expected returned value: {expResult} : get({3}) returned value: {list.get(3)}")

print("#" * 5 + " Testing Reversed Method " + "#" * 5)
print("List before calling reversed method")
list.printList()  # [1 3 4 99]
print("List after calling reverse method")
list.reverse()
list.printList()  # [99 4 3 1]

print("#" * 5 + " Testing Clear Method " + "#" * 5)
list.clear()
expResult = 0
print(f"List expected size: {expResult} : List current size: {list.size}")
print(f"Is list's head None after calling clear method? {list.head==None}")