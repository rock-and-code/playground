from typing import TypeVar, Generic, Optional, Iterator
from balance_tree import AVLTree
from queue import SimpleQueue

K = TypeVar("K")
V = TypeVar("V")
class TreeMap(Generic[K, V]):
    """ A custom implementation of a TreeMap using an AVL Tree """

    class Entry(Generic[K, V]):
        def __init__(self, key: K, value: V):
            self.key: K = key
            self.value: V = value

        def __lt__(self, other: 'TreeMap.Entry[K, V]') -> bool:
            return self.key < other.key

        def __le__(self, other: 'TreeMap.Entry[K, V]') -> bool:
            return self.key <= other.key

        def __eq__(self, other: 'TreeMap.Entry[K, V]') -> bool:
            return self.key == other.key

        def __gt__(self, other: 'TreeMap.Entry[K, V]') -> bool:
            return self.key > other.key

        def __ge__(self, other: 'TreeMap.Entry[K, V]') -> bool:
            return self.key >= other.key
        
        def __str__(self) -> str:
            return f"{self.key}:{self.value}"

    def __init__(self):
        self.bst: AVLTree[TreeMap.Entry[K, V]] = AVLTree()
        self.size = 0

    def put(self, key: K, value: V) -> None:
        """Adds or updates the value associated with the key"""
        new_entry = self.Entry(key, value)
        existing_entry = self.bst.get(new_entry)
        if existing_entry:
            existing_entry.value = value
        else:
            self.bst.add(new_entry)
            self.size += 1

    def get(self, key: K) -> Optional[V]:
        """Gets the value associated with the key, or None if not present"""
        entry = self.bst.get(self.Entry(key, None))
        return entry.value if entry else None

    def remove(self, key: K) -> Optional[V]:
        """Removes the entry associated with the key, if present"""
        entry = self.bst.get(self.Entry(key, None))
        if entry:
            self.bst.remove(self.Entry(key, None))
            self.size -= 1
            return entry.value
        return None

    def key_set(self) -> set[K]:
        """Returns a set of all keys"""
        return {entry.key for entry in self.bst}

    def value_set(self) -> set[V]:
        """Returns a set of all values"""
        return {entry.value for entry in self.bst}
    
    def __str__(self) -> str:
        out: str = '{\n'
        for entry in self.bst:
            out += f"  {entry},\n"
        out += '}\n'
        return out

    def __iter__(self) -> Iterator[K]:
        return TreeMapIter(self)


class TreeMapIter(Generic[K, V], Iterator[K]):

    """
    A custom iterator class to make the generic custom hash table implementation
    iterable
    """      
    def __init__(self, bst):
        self.entries = [entry for entry in bst.bst]
        self.indx = 0
        self.n = len(self.entries)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indx < self.n:
            currentNode = self.entries[self.indx]
            self.indx +=1
            return [currentNode.key, currentNode.value]
        else:
            raise StopIteration()