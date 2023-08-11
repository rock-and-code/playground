import sys
from timeit import default_timer as timer
sys.setrecursionlimit(10000)

n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# fibonnaci sequence using recursive approach without DP
def fib_naive(n: int)->int:
  if n < 2:
    return n
  return fib_naive(n-1) + fib_naive(n-2)

cache: dict = {}

# fibonnaci sequence using dynamic programming
def fib(n: int)->int:
  global cache
  if n < 2:
    return n
  if n in cache:
    return cache[n]
  cache[n] = fib(n-1) + fib(n-2)
  return cache[n]

# fibonnaci sequence using iterative programming
def fib_iterative(n: int)->int:
  if n < 2:
    return n
  prevprev:int = 0
  prev:int = 1
  cur:int
  for i in range(2,n+1):
    cur = prev + prevprev
    prevprev = prev
    prev = cur
  return cur


# output fib function result
if len(sys.argv) > 2 and sys.argv[2][0] == "d":
  start = timer()
  print(f"fib({n}) : {fib(n)}")
  end = timer()
  print(f"It took {end-start} seconds")
elif len(sys.argv) > 2 and sys.argv[2][0] == "n":
  start = timer()
  print(f"fib({n}) : {fib_naive(n)}")
  end = timer()
  print(f"It took {end-start} seconds")
elif len(sys.argv) > 2 and sys.argv[2][0] == "i":
  start = timer()
  print(f"fib({n}) : {fib_iterative(n)}")
  end = timer()
  print(f"It took {end-start} seconds")
else:
  print(f"fib({n}) : {fib(n)}")

  

