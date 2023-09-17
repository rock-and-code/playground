from typing import TypeVar, Generic

T = TypeVar("T")

class Queue(Generic[T]):
    """
    A custom implementation of a Queue data structure
    for practicing dsa concepts sake
    """

    class Node(Generic[T]):
        """
        A custom implementation of a node to implement
        the custom queue implementation.
        This class will allow us to create a linked list
        to store the reference of non-contiguosu allocated data in
        memory
        """
        def __init__(self, value: T) -> None:
            super().__init__()
            self.value: T = value
            self.next: Queue.Node = None



    def __init__(self) -> None:
        super().__init__()
        self.head: Queue.Node = None
        self.tail: Queue.Node = None

    # Time: O(1) Space: O(1)
    def add(self, element: T) -> None:
        """
        Inserts the specified element into this queue.
        """
        newElement: Queue.Node = Queue.Node(element)

        if self.head == None:
            self.head = newElement
            self.tail = self.head
        else:
            self.tail.next = newElement
            self.tail = newElement

    # Time: O(1) Space: O(1)
    def remove(self) -> T:
        """
        Retrieves and removes the head of this queue.
        """
        if self.head == None:
            return None
        else:
            if self.head == self.tail:
                self.tail = None
            removedElement: Queue.Node = self.head
            self.head = removedElement.next
            return removedElement.value
        
    # Time: O(1) Space: O(1)
    def empty(self) -> bool:
        """
        Returns true if the queue is empty
        """
        return self.head == None
    
    # Time: O(1) Space: O(1)
    def peek(self) -> T:
        """
        Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.
        """
        return self.head.value
    
    def __iter__(self) -> iter:
        return QueueIter(self)
    

class QueueIter(object):
        """
        A custom iterator class to make the custom queue class iterable
        """
        def __init__(self, queue_class: Queue) -> None:
            super().__init__()
            self.currentElement: Queue.Node = queue_class.head

        def __iter__(self) -> iter:
            return self
        
        def __next__(self) -> Queue.Node:
            if self.currentElement != None:
                element = self.currentElement
                self.currentElement = self.currentElement.next
                return element.value
            else:
                raise StopIteration
    