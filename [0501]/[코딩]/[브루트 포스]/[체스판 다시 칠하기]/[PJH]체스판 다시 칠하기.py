N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_count = N * M  # 다시 칠해야 하는 정사각형의 최소 개수

for i in range(N - 7):  # 8x8 크기로 자를 수 있는 모든 경우를 탐색
    for j in range(M - 7):
        count1, count2 = 0, 0  # 맨 왼쪽 위가 흰색인 경우, 검은색인 경우의 다시 칠해야 하는 정사각형 개수를 각각 센다
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:  # 체스판 모양대로 색을 칠하는 것을 고려
                    if board[k][l] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                else:
                    if board[k][l] == 'W':
                        count1 += 1
                    else:
                        count2 += 1
        min_count = min(min_count, count1, count2)

print(min_count)
