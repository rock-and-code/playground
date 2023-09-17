from hashTable import HashTable
import random

hash_table: HashTable[int, int] = HashTable()

def rand_interger_hash_table_generator(max_value: int, size: int) -> None:
    """
    Creates a new hash table with a specified number of entries comprised of integers key-value pairs ranged from zero to given max_value.
    """
    hash_table = HashTable()
    for i in range(size+1):
        rand_int: int = random.randint(0, max_value)
        hash_table.put(rand_int, rand_int)
    return hash_table

print("#" * 5 + " Testing Put Method " + "#" * 5)

hash_table.put(1, 1)
hash_table.put(2, 2)
hash_table.put(3, 3)
hash_table.put(4, 4)
hash_table.put(5, 5)
hash_table.put(6, 6)
hash_table.put(7, 7)
hash_table.put(8, 8)


print("Adding eight elements in the hash table...")
print(f"Hash table size: {hash_table.size}")
print("Printing a list of the hash table entry keys...")
hash_table.printTableKeys()
print("Printing the key-value pairs of the entries in the hash table...")
# Prints the key value pairs of the entries in the hash table...
print("[", end=" ")
for entry in hash_table:
    print(f"({entry.key},{entry.value})", end=" ")
print("]")

print("#" * 5 + " Testing Delete Method " + "#" * 5)
expResult = 7
print(f"Expected hash_table.delete(7) result: {expResult} | hash_table.delete(7) result: {hash_table.remove(7)}")
print("Printing hash table key-values pairs after removing mapping for key 7...")
print("[", end=" ")
for entry in hash_table:
    print(f"({entry.key},{entry.value})", end=" ")
print("]")
print(f"Hash table size: {hash_table.size}")

print("#" * 5 + " Testing Get Method " + "#" * 5)
expResult = 3
print(f"Expected hash_table.get(3) result: {expResult} | hash_table.get(3) result: {hash_table.get(3)}")

print("#" * 5 + " Testing Get Method " + "#" * 5)
expResult = 3
print(f"Expected hash_table.get(3) result: {expResult} | hash_table.get(3) result: {hash_table.get(3)}")

print("#" * 5 + " Testing keySet Method " + "#" * 5)
print(f"hash_table.keySet() result: {hash_table.keySet()}")

print("Removing mappings for keys 1, 2, and 3...")
hash_table.remove(1)
hash_table.remove(2)
hash_table.remove(3)

print("Iterating over the hash table's entries...")
print("Printing the key-value pairs of the entries in the hash table...")
# Prints the key value pairs of the entries in the hash table...
print("[", end=" ")
for entry in hash_table:
    print(f"({entry.key},{entry.value})", end=" ")
print("]")

print("#" * 5 + " Testing valueSet Method " + "#" * 5)
print(f"hash_table.valueSet() result: {hash_table.valueSet()}")

print("#" * 5 + " Testing the dynamic resizing feature the custom hash table " + "#" * 5)
max = 50
size = 60
print(f"Creating a new hash table of aprox {size} entries comprised of integers key-value pairs ranging from 0 to {max}")
hash_table = rand_interger_hash_table_generator(max, size)
print(f"hash_table.keySet() result: {hash_table.keySet()}")

print("Printing the key-value pairs of the entries in the hash table...")
# Prints the key value pairs of the entries in the hash table...
print("[", end=" ")
for entry in hash_table:
    print(f"({entry.key},{entry.value})", end=" ")
print("]")



