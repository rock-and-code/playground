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
    self.size: int = 0

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
    if self.top != None:
      return self.top.value
    return None
  
  # Time: O(1) Space: O(1)
  def push(self, value: T) -> T:
    """
    Pushes an item onto the top of this stack.
    """
    new_node: Stack.Node = Stack.Node(value)
    new_node.next = self.top
    self.top = new_node
    self.size += 1
    return new_node.value
  
  # Time: O(1) Space: O(1)
  def pop(self) -> T:
    """
    Removes the object at the top of this stack and returns that object as the value of this function.
    """
    if self.top == None:
      return None
    popped_node = self.top
    self.top = popped_node.next
    self.size -= 1
    return popped_node.value

  # Time: O(N) Space: O(1)
  def print_stack(self) -> None:
    """
    Prints all the elements in this stack from the top to the bottom
    """
    current_node = self.top
    print("[", end=" ")
    while current_node != None:
      print(current_node.value, end=" ")
      current_node = current_node.next
    print("]")


  def __iter__(self) -> iter:
    return StackIter(self)


class StackIter(object):
  """
  A custom Iterator class to make the custom stack class iterable
  """

  #Implement __iter__ and __next__
  def __init__(self, stack_class: Stack) -> None:
    super().__init__()
    self.current_stack: Stack.Node = stack_class.top

  def __iter__(self) -> iter:
    return self
  
  def __next__(self) -> Stack.Node:
    if self.current_stack != None:
      cur_stack = self.current_stack
      self.current_stack = self.current_stack.next
      return cur_stack.value
    else:
      raise StopIteration()
      

  
    
  


