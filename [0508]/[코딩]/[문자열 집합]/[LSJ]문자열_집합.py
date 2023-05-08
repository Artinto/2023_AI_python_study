import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
ans = 0
for i in range(N):
    S.add(input())
for _ in range(M):
    test = input()
    if test in S:
        ans+=1
print(ans)
