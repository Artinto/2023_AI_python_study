N, M = map(int, input().split())
seq = []

def backtracking():
    if len(seq) == M:
        print(*seq, sep=' ')
        return
    for i in range(1,N+1):
        if i not in seq:
            seq.append(i)
            backtracking()
            seq.pop()

backtracking()
