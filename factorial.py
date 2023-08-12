import sys

# reading command-line argument passed or assinging default argument for the fatorial function
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# function to calculate factorial
def factorial_rec(n: int)-> int:
    if n < 2:
        return 1
    return n * factorial_rec(n-1)

# output factorial function result
print(f"{n}! = {factorial_rec(n)}")
