from typing import TypeVar, Generic
import numpy
import numpy.typing

T = TypeVar("T")

class CollectionsSorter(Generic[T]):
    """
    A custom helper class to sort collections using a variety
    """
    def __init__(self) -> None:
        super().__init__()

    # Best -> Time: O(N) [Partially sorted list] Space: O(2), average -> O(N^2) Space: O(2)
    def insertion_sort(self, list: list[T]) -> None:
        """
        A custom implementaiton of the insertion sort algorithm
        """
        j: int = 0
        for i in range(len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and list[j] > key:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key

    # Best -> Time: O(LOG N) Space: O(1), Worst case -> O(N^2) Space: O(1)
    def quick_sort(self, list: list[T]) -> None:
        self.quick_sorter(list, 0, len(list) - 1)

    def quick_sorter(self, list: list[T], left: int, right: int) -> None:
        index: int = self.partition(list, left, right)
        if left < index - 1:
            self.quick_sorter(list, left, index - 1)
        if index < right:
            self.quick_sorter(list, index, right)

    def partition(self, list: list[T], left: int, right: int) -> int:
        pivot: int = list[(left + right) // 2]
        while left <= right:
            # Finding the value that does not belong on the left-hand side of the list
            while list[left] < pivot:
                left += 1
            # Finding the value that does not belong on the right-hand side of the list
            while list[right] > pivot:
                right -= 1
            if left <= right:
                # Swaps values
                temp: T = list[left]
                list[left] = list[right]
                list[right] = temp
                left += 1
                right -= 1

        return left
    
    # Best -> Time: O(LOG N) Space: O(N), Worst case -> O(N^2) Space: O(n)
    # However considering python implementation of list, it won't perform as expected
    # Python list uses a contiguous data buffer of pointers which points to python objects
    # which in turn references its values. More info at: https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
    def merge_sort(self, list: list[T]) -> None:
        helper: list[T] = [] * len(list)
        self.merge_sorter(list, helper, 0, len(list) - 1)

    def merge_sorter(self, list: list[T], helper: list[T], left: int, right: int) -> None:
        if left < right:
            middle: int = (left + right) // 2
            self.merge_sorter(list, helper, left, middle)
            self.merge_sorter(list, helper, middle + 1, right)
            self.merge(list, helper, left, right, middle)

    def merge(self, list: list[T], helper: list[T], left: int, right: int, middle: int) -> None:
        # Populating helper with list's elements
        helper = [element for element in list]
        # defining pointers to list and helper list
        current_index: int = left
        helper_left: int = left
        helper_right: int = middle + 1

        while helper_left <= middle and helper_right <= right:
            if helper[helper_left] < helper[helper_right]:
                list[current_index] = helper[helper_left]
                helper_left += 1
            else:
                list[current_index] = helper[helper_right]
                helper_right += 1
            current_index += 1
        # Inserting the remaining values at the left-hand side since the right-hand side values were
        # already in the list
        remaining: int = middle - helper_left

        for i in range(remaining+1):
            list[current_index + i] = helper[helper_left + i]

    def efficient_merge(self, list: numpy.ndarray, helper: numpy.ndarray, left: int, right: int, middle: int) -> None:
        # Populating helper with list's elements
        # helper = [element for element in list]
        helper = numpy.fromiter(list, dtype=numpy.int64, count=len(list))
        # defining pointers to list and helper list
        current_index: int = left
        helper_left: int = left
        helper_right: int = middle + 1

        while helper_left <= middle and helper_right <= right:
            if helper[helper_left] < helper[helper_right]:
                list[current_index] = helper[helper_left]
                helper_left += 1
            else:
                list[current_index] = helper[helper_right]
                helper_right += 1
            current_index += 1
        # Inserting the remaining values at the left-hand side since the right-hand side values were
        # already in the list
        remaining: int = middle - helper_left

        for i in range(remaining+1):
            list[current_index + i] = helper[helper_left + i]

    # Merge Sort implementation using NumPy Arrays
    def efficient_merge_sort(self, list: numpy.ndarray) -> None:
        helper: numpy.ndarray = numpy.empty(len(list))
        self.efficient_merge_sorter(list, helper, 0, len(list) - 1)

    def efficient_merge_sorter(self, array: numpy.ndarray, helper: numpy.ndarray, left: int, right: int) -> None:
        if left < right:
            middle: int = (left + right) // 2
            self.efficient_merge_sorter(array, helper, left, middle)
            self.efficient_merge_sorter(array, helper, middle + 1, right)
            self.efficient_merge(array, helper, left, right, middle)

    # Worst case -> Time: O(A + B) Space: O(A + B) 
    def counting_sorting(self, list: list[int]) -> None:
        """
        A custom implementation of counting sort. 
        This sort algorithms works only for integers
        """
        # identifying the max value to initializes a frequency table with max_value length + 1
        max_value: int = list[0] 

        for i in range(len(list)):
            max_value = max(max_value, list[i])

        freq_table: list[int] = [0] * (max_value + 1)


        for i in range(len(list)):
            freq_table[list[i]] += 1

        index: int = 0

        for i in range(len(freq_table)):
            while freq_table[i] > 0:
                list[index] = i
                index += 1
                freq_table[i] -= 1

    # Also known as the dutch flag sort
    def three_way_quick_sort(self, list: list[T], pivot: int) -> None:
        """
        Partitions a given array using a given pivot value
        """
        left: int = 0
        right: int = len(list) - 1
        i: int = 0
        while i <= right:
            if list[i] > pivot:
                self.swap(list, i, right)
                right -= 1
            elif list[i] < pivot:
                self.swap(list, i, left)
                i += 1
                left += 1
            else:
                i += 1


    def swap(self, list: list[T], left: int, right: int) -> None:
        """
        Swaps two element in a given list
        """
        temp: T = list[left]
        list[left] = list[right]
        list[right] = temp

                

        


