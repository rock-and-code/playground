from sorting import CollectionsSorter
from timeit import default_timer as timer
import numpy
import random

sorter: CollectionsSorter = CollectionsSorter()

def rand_int_list_generator(max_value: int, size: int, numpy_array: bool) -> list[int]:
    helper: list[int] = []
    for i in range(size + 1):
        rand_int: int = random.randint(0, max_value)
        helper.append(rand_int)
    if numpy_array:
        return numpy.array(helper)
    else:
        return helper



print("#" * 5 + " Testing Insertion Sort Method " + "#" * 5)

arr: list[int] = [1, 2, 4, 3, 5, 7, 9, 8, 11, 10]

print(f"List before sorting it -> {arr}")

sorter.insertion_sort(arr)

print(f"List after sorting it -> {arr}")

print("#" * 5 + " Testing Quick Sort Method " + "#" * 5)

arr: list[int] = [10, 7, 1, 8, 2, 5, 3, 11, 4, 0]

print(f"List before sorting it -> {arr}")

sorter.quick_sort(arr)

print(f"List after sorting it -> {arr}")

print("#" * 5 + " Testing Merge Sort Method " + "#" * 5)

arr: list[int] = [10, 7, 1, 8, 2, 5, 3, 11, 4, 0]

print(f"List before sorting it -> {arr}")

sorter.merge_sort(arr)

print(f"List after sorting it -> {arr}")

print("#" * 5 + " Testing Merge Sort Using Numpy Arr " + "#" * 5)

arr: numpy.ndarray = [10, 7, 1, 8, 2, 5, 3, 11, 4, 0]

print(f"List before sorting it -> {arr}")

sorter.efficient_merge_sort(arr)

print(f"List after sorting it -> {arr}")

print("#" * 5 + " Counting Sort Method (Integer Sorting Algorithm) " + "#" * 5)

arr: list[int] = [10, 7, 1, 8, 2, 5, 3, 11, 4, 0]

print(f"List before sorting it -> {arr}")

sorter.counting_sorting(arr)

print(f"List after sorting it -> {arr}")

print("#" * 5 + " Testing Sorting Algorithms on large list of integers (N=1,000,000) " + "#" * 5)

size: int = 10000
max_value: int = 1000000

arr: list[int] = rand_int_list_generator(max_value, size, False)

start = timer()
print(f"sorter.quick_sort(arr)) : {sorter.quick_sort(arr)}")
end = timer()
print(f"It took {end-start} seconds")
# print(arr)

# WARNING: this custom merge sort implementation in python takes forever on large lists

arr: list[int] = rand_int_list_generator(max_value, size, False)

start = timer()
print(f"sorter.merge_sort(arr)) : {sorter.merge_sort(arr)}")
end = timer()
print(f"It took {end-start} seconds")

arr: numpy.ndarray = rand_int_list_generator(max_value, size, True)

start = timer()
print(f"sorter.efficient_merge_sort(arr)) : {sorter.efficient_merge_sort(arr)}")
end = timer()
print(f"It took {end-start} seconds")

arr: list[int] = rand_int_list_generator(max_value, size, False)

start = timer()
print(f"sorter.counting_sort(arr)) : {sorter.counting_sorting(arr)}")
end = timer()
print(f"It took {end-start} seconds")


print("#" * 5 + " Testing Three Way Quick Sort Method " + "#" * 5)

arr: list[int] = [1, 2, 4, 3, 5, 7, 9, 8, 11, 10]

pivot: int = 5

print(f"List before sorting it -> {arr}")

sorter.three_way_quick_sort(arr, pivot)

print(f"List after sorting it using {pivot} as pivot -> {arr}")
