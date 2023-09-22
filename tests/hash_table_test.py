from data_structures import HashTable
import random
import unittest

class HashTableTest(unittest.TestCase):

    def rand_interger_hash_table_generator(self, max_value: int, size: int) -> None:
        """
        Creates a new hash table with a specified number of entries comprised of integers key-value pairs ranged from zero to given max_value.
        """
        hash_table = HashTable()
        for i in range(size+1):
            rand_int: int = random.randint(0, max_value)
            hash_table.put(rand_int, rand_int)
        return hash_table

    def test_put_method(self) -> None:
        hash_table: HashTable[int, int] = HashTable()
        print("#" * 5 + " Testing Put Method " + "#" * 5)

        hash_table.put(1, 1)
        hash_table.put(2, 2)
        hash_table.put(3, 3)
        hash_table.put(4, 4)
        hash_table.put(5, 5)
        hash_table.put(6, 6)
        hash_table.put(7, 7)
        hash_table.put(8, 8)
        expResult: int = 8
        result: int = hash_table.size
        print(f"Hash table size: {hash_table.size}")
        self.assertEqual(expResult, result)


    def test_print_table_keys_method(self) -> None:
        print("#" * 5 + " Testing Print Keys Method " + "#" * 5)
        hash_table: HashTable[str, str] = HashTable()
        hash_table.put("A", "A")
        hash_table.put("B", "B")
        hash_table.put("C", "C")
        hash_table.put("D", "D")
        hash_table.put("E", "E")
        hash_table.print_table_keys()
        print("Printing the key-value pairs of the entries in the hash table...")
        # Prints the key value pairs of the entries in the hash table...
        print("[", end=" ")
        for entry in hash_table:
            print(f"({entry.key},{entry.value})", end=" ")
        print("]")

        self.assertEqual("C", hash_table.get("C"))

    def test_delete_method(self) -> None:
        hash_table: HashTable[int, int] = HashTable()
        hash_table.put(1, 1)
        hash_table.put(2, 2)
        hash_table.put(3, 3)
        hash_table.put(4, 4)
        hash_table.put(5, 5)
        hash_table.put(6, 6)
        hash_table.put(7, 7)
        hash_table.put(8, 8)

        print("#" * 5 + " Testing Delete Method " + "#" * 5)
        expResult: int = 7
        result: int = hash_table.remove(7)
        self.assertEqual(expResult, result)
        print(f"Printing hash table key-values pairs after removing mapping for key {expResult}...")
        print("[", end=" ")
        for entry in hash_table:
            print(f"({entry.key},{entry.value})", end=" ")
        print("]")
        print(f"Hash table size: {hash_table.size}")

    def test_get_method(self) -> None:
        hash_table: HashTable[int, int] = HashTable()
        hash_table.put(1, 1)
        hash_table.put(2, 2)
        hash_table.put(3, 3)
        hash_table.put(4, 4)
        hash_table.put(5, 5)
        hash_table.put(6, 6)
        hash_table.put(7, 7)
        hash_table.put(8, 8)
        print("#" * 5 + " Testing Get Method " + "#" * 5)
        expResult:int = 3
        result: int = hash_table.get(3)
        self.assertEqual(expResult, result)

    def test_key_set_method(self) -> None:
        print("#" * 5 + " Testing keySet Method " + "#" * 5)
        hash_table: HashTable[str, int] = HashTable()
        hash_table.put("Mathew", 17)
        hash_table.put("Eric", 20)
        hash_table.put("Jose", 22)
        hash_table.put("Keith", 33)
        hash_table.put("John", 19)
        hash_table.put("Barbara", 25)
        hash_table.put("Stacy", 27)
        
        expResult: set[str] = {"Mathew", "Eric", "Jose", "Keith", "John", "Barbara", "Stacy"}
        result: set[str] = hash_table.key_set()

        self.assertEqual(expResult, result)
        print(f"hash_table.keySet() result: {hash_table.key_set()}")
        print("[", end=" ")
        for entry in hash_table:
            print(f"({entry.key},{entry.value})", end=" ")
        print("]")

    def test_key_value_method(self) -> None:
        print("#" * 5 + " Testing key_value Method " + "#" * 5)
        hash_table: HashTable[str, int] = HashTable()
        hash_table.put("Mathew", 17)
        hash_table.put("Eric", 20)
        hash_table.put("Jose", 22)
        hash_table.put("Keith", 33)
        hash_table.put("John", 19)
        hash_table.put("Barbara", 25)
        hash_table.put("Stacy", 27)

        expResult: set[int] = {17, 20, 22, 33, 19, 25, 27}
        result: set[int] = hash_table.value_set()
        self.assertEqual(expResult, result)
        print(f"hash_table.valueSet() result: {hash_table.value_set()}")
        
    def test_resize_method(self) -> None:
        print("#" * 5 + " Testing the dynamic resizing feature the custom hash table " + "#" * 5)
        max = 50
        size = 60
        print(f"Creating a new hash table of aprox {size} entries comprised of integers key-value pairs ranging from 0 to {max}")
        hash_table: HashTable[int, int] = self.rand_interger_hash_table_generator(max, size)
        print(f"hash_table.keySet() result: {hash_table.key_set()}")

if __name__ == '__main__':
    unittest.main()



