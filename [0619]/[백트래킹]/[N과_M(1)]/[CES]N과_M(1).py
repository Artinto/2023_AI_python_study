n, m = list(map(int, input().split()))
L = []
def S():
    if len(L)==m:
        print(' '.join(map(str,L)))
        return
    for i in range (1, n+1):
        if i not in L:
            L.append(i)
            S()
            L.pop()
S()
