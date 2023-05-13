import sys
input = sys.stdin.readline
K = int(input())
ans=[]
for _ in range(K):
    S = int(input())
    ans.append(S)
    if S == 0:
        del ans[-2:]
print(sum(ans))
