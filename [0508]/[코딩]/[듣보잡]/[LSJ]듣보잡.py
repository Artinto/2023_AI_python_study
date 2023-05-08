import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nolisten = set()
nolook = set()
for _ in range(N):
    nolisten.add(input())
for _ in range(M):
    nolook.add(input())
nothing = sorted(list(nolisten & nolook))
print(len(nothing))
print(*nothing, sep="")
