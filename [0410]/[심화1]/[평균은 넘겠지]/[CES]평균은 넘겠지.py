N = int(input())
for i in range(N):
    L = list(map(int, input().split()))
    mean = sum(L[1:]) / len(L[1:])
    count = 0  # count 값을 초기화
    for j in range(L[0]):
        if mean < L[j+1]:
            count += 1 
    print(format(count / len(L[1:]) * 100, ".3f") + "%")
