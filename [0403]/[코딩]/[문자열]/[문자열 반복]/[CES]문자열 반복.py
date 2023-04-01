N = int(input())
for i in range(N):
    a, b = input().split()
    a = int(a)
    b = str(b)
    for j in range(len(b)):
        print(a*b[j], end='')
    print()
