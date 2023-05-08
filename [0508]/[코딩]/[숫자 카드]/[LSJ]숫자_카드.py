import sys
N = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
ans={}
for i in range(N):
    ans[cards[i]]=0
for j in range(M):
    if numbers[j] in ans:
        print(1, end=' ')
    else:
        print(0, end=' ')
