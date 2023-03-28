N, X = map(int, input().split())
number=list(map(int, input().split()))
for i in range(N):
    if number[i] < X:
        print(number[i], end=" ")
