from typing import TypeVar, Generic

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
    currentNode: SiglyLinkedList.Node = self.head
    newNode = self.Node(value)
    if currentNode == None:
      self.head = newNode
      self.tail = self.head
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.size += 1
    
  # Time: O(N) Space: (4)
  def insert(self, index: int, value: T) -> None:
    """
    Inserts the specified element at the specified position in this list.
    """
    if index < 0 or index >= self.size:
      raise Exception("Out of Index Exception")
    
    currentIndex: int = 0
    prevNode: SiglyLinkedList.Node = None
    currentNode: SiglyLinkedList.Node = self.head
    newNode: SiglyLinkedList.Node = SiglyLinkedList.Node(value)

    while currentIndex < index:
      prevNode = currentNode
      currentNode = currentNode.next
      currentIndex += 1
    # Pointing to the index
    if prevNode == None:
      # Pointing to the head
      newNode.next = currentNode
      self.head = newNode
    else:
      # Pointing to some point between second element and last element in the list
      newNode.next = currentNode
      prevNode.next = newNode
    self.size += 1
  
  # Time: O(N) Space: O(1)
  def remove(self, value: T) -> bool:
    """
    Removes the first occurrence of the specified element from this list, if it is present.
    """
    currentNode: SiglyLinkedList.Node = self.head
    if currentNode == None:
      return False
    elif currentNode.value == value:
      # head moved
      self.head = currentNode.next
      self.size -= 1
      return True
    else:
      # Traversing the list 
      while currentNode.next != None:
        if currentNode.next.value == value:
          currentNode.next = currentNode.next.next
          self.size -= 1
          return True
        currentNode = currentNode.next
      return False
    
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
    currentNode: SiglyLinkedList.Node = self.head
    while currentNode != None:
      if currentNode.value == value:
        return True
    return False
  
  # Time: O(N) Space: O(1)
  def reverse(self) -> None:
    """
    Reverse the order of the elements in this list.
    """
    currentNode: SiglyLinkedList.Node = self.head
    prevNode: SiglyLinkedList.Node = currentNode
    nextNode: SiglyLinkedList.Node = None
    self.tail = prevNode
    currentNode = currentNode.next
    prevNode.next = None
    
    while currentNode != None:
      nextNode = currentNode.next
      currentNode.next = prevNode
      prevNode = currentNode
      currentNode = nextNode

    self.head = prevNode

  # Time: O(N) Space: O(1)
  def get(self, index: int) -> T:
    """
    Returns the element at the specified position in this list.
    """
    if index < 0 or index >= self.size:
      raise Exception("Out of Index Exception")
    currentIndex: int = 0
    currentNode: SiglyLinkedList.Node = self.head
    while currentIndex < index:
      currentNode = currentNode.next
      currentIndex += 1
    return currentNode.value
  
  # Time: O(N) Space: O(1)
  def printList(self) -> None:
    """
    Prints all the elements in the list
    """
    currentNode: SiglyLinkedList.Node = self.head
    print("[", end=" ")
    while currentNode != None:
      print(currentNode.value, end=" ")
      currentNode = currentNode.next
    print("]")



    




          

      
    


