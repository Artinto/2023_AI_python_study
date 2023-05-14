import sys
N = int(sys.stdin.readline())
S = []
for i in range(N):
    L = int(sys.stdin.readline())
    if L == 0:
        del L[-1] # 질문
    else:
        S.append(L)
print(sum(S))
