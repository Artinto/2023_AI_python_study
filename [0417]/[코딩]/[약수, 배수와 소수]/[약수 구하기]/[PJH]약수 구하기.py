N, K = map(int, input().split())

divisors = []
for i in range(1, N+1): # 1부터 N+1로 범위를 잡아 0은 포함되지 않도록 함
    if N % i == 0:
        divisors.append(i)

if len(divisors) < K:
    print(0)
else:
    print(divisors[K-1])
