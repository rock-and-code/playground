from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
  """
  A custom implementation of a stack
  """

  class Node(Generic[T]):
    """
    A custom implementation of a Node class
    to support the custom implementation of the stack
    """
    def __init__(self, value: T) -> None:
      super().__init__()
      self.next: Stack.Node = None
      self.value: T = value


  def __init__(self) -> None:
    """
    Construct an empty stack
    """
    super().__init__()
    self.top: Stack.Node = None

  # Time: O(1) Space: O(1)
  def empty(self) -> bool:
    """
    Returns true if the stack is empty
    """
    return self.top == None
  
  # Time: O(1) Space: O(1)
  def peek(self) -> T:
    """
    Looks at the object at the top of this stack without removing it from the stack.
    """
    return self.top.value
  
  # Time: O(1) Space: O(1)
  def push(self, value: T) -> T:
    """
    Pushes an item onto the top of this stack.
    """
    newNode: Stack.Node = Stack.Node(value)
    newNode.next = self.top
    self.top = newNode
    return newNode.value
  
  # Time: O(1) Space: O(1)
  def pop(self) -> T:
    """
    Removes the object at the top of this stack and returns that object as the value of this function.
    """
    poppedNode = self.top
    self.top = poppedNode.next
    return poppedNode.value

  # Time: O(N) Space: O(1)
  def printStack(self) -> None:
    """
    Prints all the elements in this stack from the top to the bottom
    """
    currentNode = self.top
    print("[", end=" ")
    while currentNode != None:
      print(currentNode.value, end=" ")
      currentNode = currentNode.next
    print("]")
      

  
    
  


