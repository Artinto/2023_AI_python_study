import sys
input = sys.stdin.readline
N = int(input())
temp = dict()

for i in range(N):
    a, b = map(str, input().split())
    if b == "enter":
        temp[a] = b
    else:
        del temp[a]
temp = sorted(temp.keys(), reverse=True)

for j in temp:
    print(j)
