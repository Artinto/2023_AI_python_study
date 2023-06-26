import sys
def adjacent(x): 
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 대각선, 양쪽에 퀸이 붙어있으면 안됨
            return False 
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
    else:       
        for i in range(N): 
            row[x] = i
            if adjacent(x): 
                dfs(x + 1)
N = int(sys.stdin.readline())
row = [0] * N
result = 0
dfs(0)
print(result)
