from stack import Stack
import unittest

stack: Stack = Stack()

class StackTest(unittest.TestCase):
    """
    Unitest for the custom stack implementation
    """
    def test_empty_method(self) -> None:
        print("#" * 5 + " Testing Empty Method " + "#" * 5)
        expResult = True
        print(f"Expected empty() result: {expResult} | empty() result: {stack.empty()}")

    def test_push_method(self) -> None:
        print("#" * 5 + " Testing Push Method " + "#" * 5)
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.print_stack() # [C B A]
        print(f"Is the stack empty? {stack.empty()}")
        self.assertEqual(stack.size, 3)
        
    def test_peek_method(self) -> None:
        print("#" * 5 + " Testing Peek Method " + "#" * 5)
        stack.push("A")
        stack.push("B")
        stack.push("C")
        expResult: str = "C"
        print(f"Expected peek() result: {expResult} | peek() result: {stack.peek()}")
        self.assertEqual(expResult, stack.peek())

    def test_pop_method(self) -> None:
        print("#" * 5 + " Testing Pop Method " + "#" * 5)
        stack.push("C")
        expResult = "C"
        print(f"Expected pop() result: {expResult} | pop() result: {stack.pop()}")
        print("Stack after popping one element from it")
        stack.push("C")
        #stack.printStack() # [B A]
        self.assertTrue(stack.pop() == "C")
        print("[", end=" ")
        for s in stack:
            print(s, end=" ")
        print("]")
    
    def test_pop_and_empty_methods(self) -> None:
        print("#" * 5 + " Testing Pop And Empty Method " + "#" * 5)
        print("Popping three elements from the stack...")
        stack.pop()
        stack.pop()
        stack.pop()
        print(f"Is the stack empty? {stack.empty()}")
        self.assertTrue(stack.empty())

if __name__ == '__main__':
    unittest.main()



