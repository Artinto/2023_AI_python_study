import sys
N = int(sys.stdin.readline())
S = []
for i in range(N):
    L = sys.stdin.readline().split()
    if L[0]=='push':
        S.append(L[1])
    elif L[0]=='pop':
        if len(S)==0:
            print(-1)
        else:
            print(S.pop())
    elif L[0]=='size':
        print(len(S))
    elif L[0]=='empty':
        if len(S)==0:
            print(1)
        else:
            print(0)
    elif L[0]=='top':
        if len(S)==0:
            print(-1)
        else:
            print(S[-1])
        
