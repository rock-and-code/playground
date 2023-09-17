
class Math(object):
    """
    A custom class to implements some mathematical functions
    To practice number theory.
    Reference: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
    """
    def __init__(self) -> None:
        """
        Default constructor
        """
        pass

    def power_recurvise(self, base: int, power: int) -> int:
        """
        Calculates a power based on a given base and power. Naive approach
        TIME: O(N)
        """
        # Base case
        if power != 0:
            return base * self.power_recurvise(base, power - 1)
        return 1
    
    def power_iterative(self, base: int, power: int) -> int:
        """
        Calculates a power using a iterative approach of a given base and power. Naive approach
        TIME: O(N)
        """
        result: int = 1
        for _ in range(power):
            result *= base
        return result
    
    def binary_exponentiation_recursive(self, base: int, power: int) -> int:
        """
        Optimized power calculator algorithm based on whether power is even or odd
        TIME: O(LOG N)
        """
        if power == 0:
            return 1
        elif power % 2 == 0:
            return self.binary_exponentiation_recursive(base*base, power // 2)
        else:
            return base * self.binary_exponentiation_recursive(base*base, (power-1)//2)
    

    def binary_exponentiation_iterative(self, base: int, power: int) -> int:
        """
        Optimized power calculator algorithm based on whether power is even or odd
        TIME: O(LOG N)
        """
        result: int = 1
        while power > 0:
            if power % 2 == 1:
                result *= base
            base*=base
            power//=2
        return result
    
    def mcd_naive(self, a: int, b: int) -> int:
        """
        Returns the maximum common divisor of two given interger. Naive approach
        TIME: MIN(A,B)
        """
        min_val: int = min(a, b)
        for i in range(min_val, 0, -1):
            if a % i == 0 and b % i == 0:
                return i
            
    def euclidian_mcd(self, a: int, b: int) -> int:
        """
        Euclidians algorithm. TIME: LOG(MAX(A, B))
        """
        if b == 0:
            return a
        return self.euclidian_mcd(b, a%b)