import sys
sys.setrecursionlimit(10000)

# Reading command-line arguments passed
n:int = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# Function to calculate factorial using a recursive approach
def factorial_rec(n: int)->int:
  if n < 2:
    return 1
  return n * factorial_rec(n-1)

# Output factorial function result
print(f"{n}! = {factorial_rec(n)}")

