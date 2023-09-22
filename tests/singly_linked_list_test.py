from data_structures import SiglyLinkedList

print("#" * 5 + " Testing Add Method " + "#" * 5)
list: SiglyLinkedList = SiglyLinkedList()
list.add(1)
list.add(3)
list.add(4)
list.add(5)
expResult = 4
list.printList() #  [1 3 4 5]
print("Iterating over the singly linked list elements")
print("[", end=" ")
for element in list:
    print(element, end=" ")
print("]")
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

print("#" * 5 + " Testing Insert Method # 2 " + "#" * 5)
list.clear()
list.insert(0, 5)
list.insert(0, 7)
list.insert(0, 8)
list.insert(0, 9)
print("Printing list after inserting four elements...") # [9 8 7 5]
print("List -> [", end=" ")
for element in list:
    print(element, end=" ")
print("]")
list.insert(1, 77)  # [9 77 8 7 5]
list.insert(3, 80)  # [9 77 8 80 7 5]
list.printList()

list.remove(9)
list.printList() # [77 8 80 7 5]

list.add(5) 
list.insert(0, 5) # [5 77 8 80 7 5 5]

list.printList() # [5 77 8 80 7 5 5]
list.removeAll(5) 
list.printList() # [77 8 80 7]

list.add(99)
list.printList() # [77 8 80 7 99]

list.reverseFrom(1, 4) 
list.printList() # [77 99 7 80 8]

list.reverseFrom(1, 3) 
list.printList() # [77 80 7 99 8]

list.reverse() # [8 99 7 80 77]

list.insert(0, 11) # [11 8 99 7 80 77]
list.add(50) # [11 8 99 7 80 77 50]

list.printList() # [11 8 99 7 80 77 50]

list.remove(11)
list.remove(50)
list.remove(7)

list.printList() # [8 99 80 77 ]

list.add(77)

list.printList() # [8 99 80 77 77 ]

list.removeAll(77)

arr = [element for element in list]

print(arr)


