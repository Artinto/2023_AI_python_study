N, M = map(int, input().split())
board = []
count = []
for _ in range(N):
    board.append(input())
for a in range(N-7):
    for b in range(M-7):
        draw1 = 0
        draw2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        draw1 += 1
                    if board[i][j] != 'B':
                        draw2 += 1
                else:
                    if board[i][j] != 'B':
                        draw1 += 1
                    if board[i][j] != 'W':
                        draw2 += 1
        count.append(min(draw1, draw2))
print(min(count))
