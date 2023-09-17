import unittest
from my_math import Math

instance = Math()

BASE: int = 0
POWER: int = 0

class TestMathMethods(unittest.TestCase):

    def test_power_recursive(self):
        BASE = 10
        POWER = 2
        print(f"### Testing power_recursive({BASE}, {POWER}) method")
        self.assertEqual(instance.power_recurvise(BASE, POWER), 100)
        print(f"power_recursive({BASE}, {POWER}) = {instance.power_recurvise(BASE,POWER)}")

    def test_power_iterative(self):
        BASE = 10
        POWER = 2
        print(f"### Testing power_iterative({BASE}, {POWER}) method")
        self.assertEqual(instance.power_iterative(BASE, POWER), 100)
        print(f"power_iterative({BASE}, {POWER}) = {instance.power_iterative(10,2)}")

    def test_binary_exponentiation_recursive(self):
        BASE = 3
        POWER = 10
        print(f"### Testing binary_exponentiation_recursive({BASE}, {POWER}) method")
        self.assertEqual(instance.binary_exponentiation_recursive(BASE, POWER), BASE**POWER)
        print(f"power_recursive({BASE}, {POWER}) = {instance.binary_exponentiation_recursive(BASE,POWER)}")

    def test_binary_exponentiation_iterative(self):
        BASE = 3
        POWER = 10
        print(f"### Testing binary_exponentiation_iterative({BASE}, {POWER}) method")
        self.assertEqual(instance.binary_exponentiation_iterative(BASE, POWER), BASE**POWER)
        print(f"power_recursive({BASE}, {POWER}) = {instance.binary_exponentiation_iterative(BASE,POWER)}")

    def test_mcd_naive(self):
        A: int = 10
        B: int = 6
        print(f"### Testing mcd_naive({A}, {B}) method")
        self.assertEqual(instance.mcd_naive(A, B), 2)
        print(f"mcd_naive({A}, {B}) = {instance.mcd_naive(A,B)}")

    def test_euclidian_mcd(self):
        A: int = 20
        B: int = 15
        print(f"### Testing euclidian_mcd({A}, {B}) method")
        self.assertEqual(instance.mcd_naive(A, B), 5)
        print(f"euclidian_mcd({A}, {B}) = {instance.euclidian_mcd(A,B)}")

if __name__ == '__main__':
    unittest.main()