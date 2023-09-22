from typing import TypeVar, Generic
from .stack import Stack

T = TypeVar("T")



class SiglyLinkedList(Generic[T]):
  """A custom implementation of a generic linked list"""

  class Node(Generic[T]):
      """
      A Custome implementation of a Node class to support
      to support the linked list implementation
      """
      def __init__(self, value: T) -> None:
        super().__init__()
        self.next: SiglyLinkedList.Node = None
        self.value: T = value


  def __init__(self) -> None:
    """
    Construct an empty list
    """
    super().__init__()
    self.size = 0
    self.head: SiglyLinkedList.Node = None
    self.tail: SiglyLinkedList.Node = None

  # Time: O(1) Space: 0(2)
  def add(self, value: T) -> None:
    """
    Adds a new element in the list
    """
    current_node: SiglyLinkedList.Node = self.head
    new_node = self.Node(value)
    if current_node == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.size += 1
    
  # Time: O(N) Space: (4)
  def insert(self, index: int, value: T) -> None:
    """
    Inserts the specified element at the specified position in this list.
    """
    if index < 0 or index > self.size:
      raise Exception("Out of Index Exception")
    
    current_index: int = 0
    prev_node: SiglyLinkedList.Node = None
    current_node: SiglyLinkedList.Node = self.head
    new_node: SiglyLinkedList.Node = SiglyLinkedList.Node(value)

    while current_index < index:
      prev_node = current_node
      current_node = current_node.next
      current_index += 1
    # Pointing to the index
    if prev_node == None:
      # Pointing to the head
      if self.head == None:
        self.tail = new_node
      new_node.next = current_node
      self.head = new_node
    else:
      # Pointing to some point between second element and last element in the list
      new_node.next = current_node
      prev_node.next = new_node
    self.size += 1
  
  # Time: O(N) Space: O(1)
  def remove(self, value: T) -> bool:
    """
    Removes the first occurrence of the specified element from this list, if it is present.
    """
    prev_node: SiglyLinkedList.Node = None
    current_node: SiglyLinkedList.Node = self.head
    if current_node == None:
      return False
    # Traversing the list
    while current_node != None:
      if current_node.value == value:
        return self.removeNode(prev_node, current_node)
      prev_node = current_node
      current_node = current_node.next
    return False
    
  def removeNode(self, prev_node: Node, node: Node) -> bool:
    if node == self.head:
      if self.tail == node:
        self.tail = None
      self.head = self.head.next
    elif node == self.tail:
      prev_node.next = None
      self.tail = prev_node
    else:
      prev_node.next = node.next
    self.size -= 1
    return True

  # Time: O(N) Space: O(1)
  def removeAll(self, value: T) -> bool:
    """
    Removes all the occurrences of the specified element from this list, if it is present.
    """
    deleted: bool = False
    prev_node: SiglyLinkedList.Node = None
    current_node: SiglyLinkedList.Node = self.head
    if current_node == None:
      return False
    # Traversing the list
    while current_node != None:
      if current_node.value == value:
        if current_node == self.head:
          self.head = self.head.next
          current_node = self.head
        else:
          if current_node == self.tail:
            self.tail = prev_node
          prev_node.next = current_node.next
          current_node = prev_node.next
        deleted = True
        self.size -= 1
      else:
        prev_node = current_node
        current_node = current_node.next
    return deleted
  
  def removeFirst(self) -> T:
    """
    Removes the first element from the list
    """
    if self.head != None:
      if self.head == self.tail:
        self.tail = None
      self.head = self.head.next
      self.size -= 1
    
  # Time: O(1) Space: O(1)
  def clear(self) -> None:
    """
    Removes all the elements from the list.
    """
    self.head = None
    self.tail = None
    self.size = 0

  # Time: O(N) Space: O(1)
  def contains(self, value: T) -> bool:
    """
    Returns true if this list contains the specified element.
    """
    current_node: SiglyLinkedList.Node = self.head
    while current_node != None:
      if current_node.value == value:
        return True
      current_node = current_node.next
    return False
  
  # Time: O(N) Space: O(1)
  def reverse(self) -> None:
    """
    Reverse the order of the elements in this list.
    """
    current_node: SiglyLinkedList.Node = self.head
    prev_node: SiglyLinkedList.Node = current_node
    next_node: SiglyLinkedList.Node = None
    self.tail = prev_node
    current_node = current_node.next
    prev_node.next = None
    
    while current_node != None:
      next_node = current_node.next
      current_node.next = prev_node
      prev_node = current_node
      current_node = next_node

    self.head = prev_node

  def reverseFrom(self, start: int, end: int) -> None:
    """
    Reverses the element in this list from the given start index to the given end index
    """
    if start >= 0 and start < self.size and end >= start and end >=0 and end < self.size:
      stack: Stack = Stack()
      curren_node: SiglyLinkedList.Node = self.head
      index: int = 0
      while curren_node != None:
        if index >= start and index <= end:
          stack.push(curren_node.value)
        index += 1
        curren_node = curren_node.next
      index = 0
      curren_node = self.head
      while curren_node != None:
        if index >= start and index <= end:
          curren_node.value = stack.pop()
        index += 1
        curren_node = curren_node.next


  # Time: O(N) Space: O(1)
  def get(self, index: int) -> T:
    """
    Returns the element at the specified position in this list.
    """
    if index < 0 or index >= self.size:
      raise Exception("Out of Index Exception")
    current_index: int = 0
    current_node: SiglyLinkedList.Node = self.head
    while current_index < index:
      current_node = current_node.next
      current_index += 1
    return current_node.value
    
  
  # Time: O(N) Space: O(1)
  def printList(self) -> None:
    """
    Prints all the elements in the list
    """
    current_node: SiglyLinkedList.Node = self.head
    print("[", end=" ")
    while current_node != None:
      print(current_node.value, end=" ")
      current_node = current_node.next
    print("]")

  def __iter__(self) -> iter:
    return SinglyLinkedListIter(self)

class SinglyLinkedListIter(Generic[T]):
    """
    A custom iterator class to make the generic custom singly linked list implementation
    iterable
    """      
    def __init__(self, singly_linked_list: SiglyLinkedList) -> None:
        super().__init__()
        # creating a list of the hashtable entries using Nested List Comprehensions in Python
        # inspired by examples shown in https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/#
        self.current_node: SiglyLinkedList.Node = singly_linked_list.head
     

    def __iter__(self) -> iter:
        return self
    
    def __next__(self) -> T:
        if self.current_node != None:
          node: SiglyLinkedList.Node = self.current_node
          self.current_node = self.current_node.next
          return node.value
        else:
            raise StopIteration



    




          

      
    


