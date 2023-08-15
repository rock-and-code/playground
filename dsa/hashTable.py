from typing import TypeVar, Generic
from singlyLinkedList import SiglyLinkedList

K = TypeVar("K")
V = TypeVar("V")

class HashTable(Generic[K, V]):
    """
    A custom implementation of a hash table
    """

    class Entry(Generic[K,V]):
        """
        A custom implememtation of a hash table entry class
        to allow non-contiguous allocation of memory
        to support the custom hash map implementation
        """
        def __init__(self, key: K, value: V) -> None:
            """
            Construct a new hash table entry with a given key and value
            """
            super().__init__()
            self.key: K = key
            self.value: V = value
            
    
    def __init__(self) -> None:
        """
        Construct an empty hash table with a default size of 16
        """
        super().__init__()
        self.load_factor: float = 0.75
        self.size: int = 0
        self.default_size: int = 16
        self.table: list[SiglyLinkedList[HashTable.Entry]] = [SiglyLinkedList() for i in range(self.default_size)]

    # Time: O(1), Space: O1()
    def hashKey(self, key: K, table_size: int) -> int:
        return hash(key) % table_size

    # Time: O(1) average Space: O(2)
    def put(self, key: K, value: V) -> None:
        """
        Adds the specified entry in the hash table if it is not present in the table.
        Otherwise it will update the value of the key-matching entry
        """
        index: int = self.hashKey(key, len(self.table))
        insert: bool = True
        for entry in self.table[index]:
            if entry.key == key:
                insert = False
                entry.value = value
        if insert:
            self.ensureCapacity()
            # recalculates the index since table size may have changed, thus changing 
            # the hash key value
            index = self.hashKey(key, len(self.table))
            self.table[index].add(HashTable.Entry(key, value))
            self.size += 1
    
    # Time: O(N) average Space: O(N)
    def ensureCapacity(self) -> None:
        """
        Increases the hash table size if the tracked hash table size is greater
        or equals than the product of hash table length and load factor (0.75)
        """
        if self.size >= self.load_factor * len(self.table):
            # doubling the current hash table size
            newHashTable: list[SiglyLinkedList[HashTable.Entry]] = [SiglyLinkedList() for i in range(len(self.table) * 2)]
            # populating new hash table with current table entries
            for entry_list in self.table:
                for entry in entry_list:
                    index: int = self.hashKey(entry.key, len(newHashTable))
                    newHashTable[index].add(entry)
            self.table = newHashTable

    # Time: O(1) average Space: O(2)
    def remove(self, key: K) -> V:
        """
        Removes the mapping for the specified key from this map if present.
        """
        index: int = self.hashKey(key, len(self.table))
        for entry in self.table[index]:
            if entry.key == key:
                value: V = entry.value
                # removing element from the current chain
                self.table[index].remove(entry)
                self.size -= 1
                return entry.value
        return None

    # Time: O(1) average Space: O(1)
    def get(self, key: K) -> V:
        """
        Returns the value to which the specified key is mapped, or None if this map contains no mapping for the key.
        """
        index: int = self.hashKey(key, len(self.table))
        for entry in self.table[index]:
            if entry.key == key:
                return entry.value
        return None
    
    def __iter__(self) -> iter:
        return HashTableIter(self)
    
    # Time: O(N) Space: O(N)
    def keySet(self) -> set[K]:
        keySet: set[K] = set()
        for entry in self:
            keySet.add(entry.key)
        return keySet
    
    # Time: O(N) Space: O(N)
    def valueSet(self) -> set[V]:
        valueSet: set[V] = set()
        for entry in self:
            valueSet.add(entry.value)
        return valueSet
    
    def printTableKeys(self) -> None:
        """
        Prints the keys of each mapping in the hash table
        """
        print("[", end=" ")
        for entry_list in self.table:
            for entry in entry_list:
                print(entry.key, end=" ")
        print("]")

    

class HashTableIter(Generic[K, V]):
    """
    A custom iterator class to make the generic custom hash table implementation
    iterable
    """      
    def __init__(self, hash_table: HashTable) -> None:
        super().__init__()
        # creating a list of the hashtable entries using Nested List Comprehensions in Python
        # inspired by examples shown in https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/#
        self.entry_list: list[HashTable.Entry] = [entry for entry_list in hash_table.table for entry in entry_list]
        self.len: int = len(self.entry_list)
        self.current_index: int = 0
     

    def __iter__(self) -> iter:
        return self
    
    def __next__(self) -> HashTable.Entry:
        if self.current_index < self.len:
            entry: HashTable.Entry = self.entry_list[self.current_index]
            self.current_index += 1
            return entry
        else:
            raise StopIteration

