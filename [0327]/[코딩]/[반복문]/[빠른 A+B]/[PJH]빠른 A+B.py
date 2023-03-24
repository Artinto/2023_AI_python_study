from sys import stdin # 효율을 높이기 위해 stdin을 import하여 readline()을 사용하여 효율을 높임

t = int(stdin.readline())

for _ in range(t):
    a,b = map(int, stdin.readline().split())
    print(a+b)
