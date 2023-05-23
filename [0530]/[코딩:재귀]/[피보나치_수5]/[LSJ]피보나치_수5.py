#from functools import lru_cache
#@lru_cache
def fib(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
N = int(input())
print(fib(N))
# 0 1 2 3 4 5 6  7  8  9 10
# 0 1 1 2 3 5 8 13 21 34 55
