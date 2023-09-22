import unittest
from data_structures import sum_segment_tree

arr: list[int] = [3, -7, 44, 78, 3, -22, 9]

instance: sum_segment_tree = sum_segment_tree(arr)

class SumSegmentTreeTest(unittest.TestCase):
    
    def test_print_two_dim_tree_method(self):
        print("#" * 5 + " Testing Print Two Dim Tree Method")
        instance.print_two_dim_tree()

    def test_get_sum_method_one(self):
        start: int = 0
        end: int = 3
        print("#" * 5 + f" Testing get_sum(start_index: {start}, end_index: {end}) Method")
        print(f"get_sum({start}, {end}) = {instance.get_sum(start, end)}")
        self.assertEqual(instance.get_sum(start, end), 118)

    def test_get_sum_method_two(self):
        start: int = 3
        end: int = 5
        print("#" * 5 + f" Testing get_sum(start_index: {start}, end_index: {end}) Method")
        print(f"get_sum({start}, {end}) = {instance.get_sum(start, end)}")
        self.assertEqual(instance.get_sum(start, end), 59)

    def test_update_value_method(self):
        index: int = 1
        new_value: int = 0
        print("#" * 5 + f" Testing update_value(index: {index}, new_value: {new_value}) Method")
        instance.update_value(index, new_value)
        instance.print_two_dim_tree()

    def test_update_value_method_two(self):
        index: int = 5
        new_value: int = 45
        print("#" * 5 + f" Testing update_value(index: {index}, new_value: {new_value}) Method")
        instance.update_value(index, new_value)
        instance.print_two_dim_tree()
        start: int = 4
        end: int = 6
        print("#" * 5 + f" Testing get_sum(start_index: {start}, end_index: {end}) Method")
        print(f"get_sum({start}, {end}) = {instance.get_sum(start, end)}")
        self.assertEqual(instance.get_sum(start, end), 57)


if __name__ == '__main__':
    unittest.main()