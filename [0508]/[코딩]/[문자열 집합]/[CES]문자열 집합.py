import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = set([input() for i in range(N)])
cnt = 0
for j in range(M):
    t =input()
    if t in s:
        cnt+=1
print(cnt)
