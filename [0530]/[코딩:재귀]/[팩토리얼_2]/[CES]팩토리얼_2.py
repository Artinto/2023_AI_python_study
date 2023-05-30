N = int(input())
P = 1
for i in range(1, N+1):
    P*=i
print(P)

import math 


def factorial_2(N):
    return math.factorial(N)
    

if __name__ == "__main__":
    N = int(input())
    print(factorial_2(N=N))
